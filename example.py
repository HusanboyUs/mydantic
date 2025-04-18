# import requests
# import pytest


# @pytest.fixture(scope='function', autouse=False)
# def setup_environment():
#     base_url = "https://release-gs.qa-playground.com/api/v1/setup"
#     headers = {
#         "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6IldGZlRBQ0hzYUhvQ3VML1MiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL215a290cWJvY2t6dnphY2NjdWJ6LnN1cGFiYXNlLmNvL2F1dGgvdjEiLCJzdWIiOiJiNjJiNTQzZS1kYWNlLTRjMWItODFkNS0xOTc4NGExMWJmNWIiLCJhdWQiOiJhdXRoZW50aWNhdGVkIiwiZXhwIjoxNzQ1NTk1OTQ3LCJpYXQiOjE3NDQ5OTU5NDcsImVtYWlsIjoid29uZWdpeDY5NkBub3JvYXNpcy5jb20iLCJwaG9uZSI6IiIsImFwcF9tZXRhZGF0YSI6eyJwcm92aWRlciI6ImVtYWlsIiwicHJvdmlkZXJzIjpbImVtYWlsIl19LCJ1c2VyX21ldGFkYXRhIjp7ImVtYWlsIjoid29uZWdpeDY5NkBub3JvYXNpcy5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiZnVsbF9uYW1lIjoiSm9obiIsInBob25lX3ZlcmlmaWVkIjpmYWxzZSwic3ViIjoiYjYyYjU0M2UtZGFjZS00YzFiLTgxZDUtMTk3ODRhMTFiZjViIn0sInJvbGUiOiJhdXRoZW50aWNhdGVkIiwiYWFsIjoiYWFsMSIsImFtciI6W3sibWV0aG9kIjoiZW1haWwvc2lnbnVwIiwidGltZXN0YW1wIjoxNzQzODY0NTIzfV0sInNlc3Npb25faWQiOiI4NGM3ZmU2OS0zMTRlLTQyYWQtYjY0My1hZDU1NzU0ZTgyMDEiLCJpc19hbm9ueW1vdXMiOmZhbHNlfQ.LyvGl9xrUmvln66JpKAepcmTSq1_TkrkS2tDqrvKG_A",
#         "X-Task-Id": "API-1"
#     }
#     res = requests.post(base_url, headers=headers)
#     assert res.status_code == 205


# @pytest.mark.usefixtures("setup_environment")
# class TestDeletUsers:

#     base_url = "https://release-gs.qa-playground.com/api/v1"
#     headers = {
#         "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsImtpZCI6IldGZlRBQ0hzYUhvQ3VML1MiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL215a290cWJvY2t6dnphY2NjdWJ6LnN1cGFiYXNlLmNvL2F1dGgvdjEiLCJzdWIiOiJiNjJiNTQzZS1kYWNlLTRjMWItODFkNS0xOTc4NGExMWJmNWIiLCJhdWQiOiJhdXRoZW50aWNhdGVkIiwiZXhwIjoxNzQ1NTk1OTQ3LCJpYXQiOjE3NDQ5OTU5NDcsImVtYWlsIjoid29uZWdpeDY5NkBub3JvYXNpcy5jb20iLCJwaG9uZSI6IiIsImFwcF9tZXRhZGF0YSI6eyJwcm92aWRlciI6ImVtYWlsIiwicHJvdmlkZXJzIjpbImVtYWlsIl19LCJ1c2VyX21ldGFkYXRhIjp7ImVtYWlsIjoid29uZWdpeDY5NkBub3JvYXNpcy5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiZnVsbF9uYW1lIjoiSm9obiIsInBob25lX3ZlcmlmaWVkIjpmYWxzZSwic3ViIjoiYjYyYjU0M2UtZGFjZS00YzFiLTgxZDUtMTk3ODRhMTFiZjViIn0sInJvbGUiOiJhdXRoZW50aWNhdGVkIiwiYWFsIjoiYWFsMSIsImFtciI6W3sibWV0aG9kIjoiZW1haWwvc2lnbnVwIiwidGltZXN0YW1wIjoxNzQzODY0NTIzfV0sInNlc3Npb25faWQiOiI4NGM3ZmU2OS0zMTRlLTQyYWQtYjY0My1hZDU1NzU0ZTgyMDEiLCJpc19hbm9ueW1vdXMiOmZhbHNlfQ.LyvGl9xrUmvln66JpKAepcmTSq1_TkrkS2tDqrvKG_A",
#         "X-Task-Id": "API-1"
#     }


#     def test_delete_user(self, setup_environment):
#         request = requests.get(self.base_url + "/users", headers=self.headers)
#         assert request.status_code == 200, "cannot send request to the server"
#         response = request.json()
#         all_users = response["meta"]["count"]
#         user_to_delete = response["users"](0)
#         user_uuid = response["users"]["count"]
        

# payload = {'meta': {'total': 11},
#             'users': [{'avatar_url': '', 'email': 'alex@gmail.com', 'name': 'Alex', 'nickname': 'alex', 'uuid': 'c72b500e-0b77-4c02-ab9c-96add2a2f2bb'}, {'avatar_url': '', 'email': 'john@gmail.com', 'name': 'John', 'nickname': 'john', 'uuid': '2d27a7f9-08e2-48b2-ba26-35dc50f40230'}, {'avatar_url': '', 'email': 'kate@gmail.com', 'name': 'Kate', 'nickname': 'kate', 'uuid': 'e617ab93-1542-4df5-90a9-acee9e391add'}, {'avatar_url': '', 'email': 'leona@gmail.com', 'name': 'Leona', 'nickname': 'leona', 'uuid': 'b125d38e-1cce-454d-83ae-b25c69f79ccc'}, {'avatar_url': '', 'email': 'mario@gmail.com', 'name': 'Mario', 'nickname': 'mario', 'uuid': '2185d5b7-8f15-4aa2-9956-3e7650202613'}, {'avatar_url': '', 'email': 'roman@gmail.com', 'name': 'Roman', 'nickname': 'roman', 'uuid': 'a364eaf5-04e2-4161-b9f9-e3019407eff2'}, {'avatar_url': '', 'email': 'said@gmail.com', 'name': 'Said', 'nickname': 'said', 'uuid': '7ec37161-6cd3-4c83-8c50-22669b55f761'}, {'avatar_url': '', 'email': 'sam@gmail.com', 'name': 'Sam', 'nickname': 'sam', 'uuid': '0e54c9db-0052-4865-b5c6-146f7429e93a'}, {'avatar_url': '', 'email': 'sasha@gmail.com', 'name': 'Sasha', 'nickname': 'sasha', 'uuid': '5bb7c0ca-c275-4be2-83f3-26449ae76297'}, {'avatar_url': '', 'email': 'sergey@gmail.com', 'name': 'Sergey', 'nickname': 'sergey', 'uuid': 'c36e1856-a261-492b-9cdc-49a8121161ed'}]}

# print(payload["users"][0]["uuid"])