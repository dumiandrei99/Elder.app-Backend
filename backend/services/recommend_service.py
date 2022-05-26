from ..repositories.user_prefference_repository import UserPrefferenceRepository
import pandas as pd


class RecommendService:
    def recommend_groups(self, user):
        # get all the user prefferences from the DB and transform it from Objects to a list containg each prefference
        user_prefferences = UserPrefferenceRepository.get_all_user_prefferences()
        user_prefferences_list = []

        for user_prefference in user_prefferences:
            to_list = [user_prefference.uuid_user.uuid, user_prefference.uuid_prefference.prefference_name, 1 if user_prefference.liked == True else 0]
            user_prefferences_list.append(to_list)
        
        # transform the list to DataFrame in order to start applying the recommending algorithm
        df = pd.DataFrame(user_prefferences_list, columns = ['userUUID', 'prefference', 'liked'])
        print(df)
        
        return "OK"