from ..repositories.user_prefference_repository import UserPrefferenceRepository
from ..repositories.user_repository import UserRepository
from ..repositories.user_in_group_repository import UserInGroupRepository
import pandas as pd


class RecommendService:

    def __group_objects_to_list(self):
        # get all the groups from the DB and transform it from Objects to a list containing each group
        users_in_groups = UserInGroupRepository.get_all_users_in_groups()
        users_in_groups_list = []
        for user_in_group in users_in_groups:
            to_list = [user_in_group.uuid_user.uuid, user_in_group.uuid_group.uuid, user_in_group.group_name]
            users_in_groups_list.append(to_list)
        
        return users_in_groups_list
    
    def __user_prefferences_to_list(self):
        # get all the user prefferences from the DB and transform it from Objects to a list containg each prefference
        user_prefferences = UserPrefferenceRepository.get_all_user_prefferences()
        user_prefferences_list = []

        for user_prefference in user_prefferences:
            to_list = [user_prefference.uuid_user.uuid, user_prefference.uuid_prefference.prefference_name, 1 if user_prefference.liked == True else 0]
            user_prefferences_list.append(to_list)
        
        return user_prefferences_list

    def recommend_groups(self, logged_in_username):
       
        # get all the user prefferences from the DB and transform it from Objects to a list containg each prefference
        user_prefferences_list = self.__user_prefferences_to_list()
        # get all the groups from the DB and transform it from Objects to a list containing each group
        users_in_groups_list = self.__group_objects_to_list()
                
        # transform the list to DataFrame in order to start applying the recommending algorithm
        df_user_prefferences = pd.DataFrame(user_prefferences_list, columns = ['userUUID', 'prefference', 'liked'])
        df_users_in_groups = pd.DataFrame(users_in_groups_list, columns=['userUUID', 'groupUUID', 'group_name'])
    
        # user prefferences processing
        matrix = df_user_prefferences.pivot_table(index='userUUID', columns='prefference', values='liked')

        mean = matrix.mean(axis=1)
        matrix_norm = matrix.subtract(mean, axis='rows')

        # calculate user similarity with Pearson correlation

        user_similarity = matrix_norm.T.corr()
        user_similarity = user_similarity.round(4)

        # the user for which we are trying to recommend for will have a 1.0 similarity (maximum), so we drop him from the user_similarity dataframe
        logged_in_uuid = UserRepository.get_uuid_by_username(logged_in_username)
        user_similarity.drop(index=logged_in_uuid, inplace=True)

        # pick top N number of similar users

        n = 3

        # Set Pearson similarity threashold 

        user_similarity_threshold = 0.1

        # Sort top n similar users
        similar_users = user_similarity[user_similarity[logged_in_uuid]>user_similarity_threshold][logged_in_uuid].sort_values(ascending=False)[:n]
        # Transform it to a dataframe
        similar_users_df = pd.DataFrame({'userUUID':similar_users.index, 'similarity': similar_users.values})
        # Transform the dataframe to a dictionary for later use
        similar_users_dict = dict(zip(similar_users_df.userUUID, similar_users_df.similarity))


        # group processing

        similar_users_uuids = list(similar_users_dict.keys())
        # get the groups that the user we are recommending for have already joined (if any)
        groups_logged_in_user_is_in = list(df_users_in_groups[df_users_in_groups.userUUID == logged_in_uuid ].loc[:,'group_name'])

        # get groups that similar users are in 
        groups_similar_users_are_in = df_users_in_groups[df_users_in_groups.userUUID.isin(similar_users_uuids)]
        groups_similar_users_are_in = list(groups_similar_users_are_in.loc[:,'group_name'])
        
        # count the appearances of each group and save it in a dictionary (the more appearances the more likely the user is to join that group)
        groups_to_recommend_to_user = {item:groups_similar_users_are_in.count(item) for item in groups_similar_users_are_in}
        groups_to_recommend_to_user = dict(groups_to_recommend_to_user)

        # delete the groups in which the user is already enrolled from the recommandation list
        for key in groups_logged_in_user_is_in:
            if key in groups_to_recommend_to_user.keys():
                del groups_to_recommend_to_user[key]
                
        return groups_to_recommend_to_user