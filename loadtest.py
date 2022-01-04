from locust import HttpUser, TaskSet, task, constant


class UserBehavior(TaskSet):
    wait_time = constant(1)

    # @task
    #                 "rememberme": "false",
    #                 "username": "admin"
    #             }
    #
    #     with self.client.post('/user/login?new_ajax',data=body1, catch_response=True) as response:
    #
    #         # FETCH RESPONSE INTO JSON
    #         if response.status_code == 200:
    #             res = response.json()
    #             print(res)
    #
    #         else:
    #             print("login else:", response.status_code)   # def get_tests(self):
    #
    #     body1 = {
    #                 "ajaxRequest": "true",
    #                 "password": "12345678",
    #                 "rememberme": "false",
    #                 "username": "admin"
    #             }
    #
    #     with self.client.post('/user/login?new_ajax',data=body1, catch_response=True) as response:
    #
    #         # FETCH RESPONSE INTO JSON
    #         if response.status_code == 200:
    #             res = response.json()
    #             print(res)
    #
    #         else:
    #             print("login else:", response.status_code)


class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    # host = "https://www.bookmundi.com"
    host = "https://bookmundi:Bookstage2018@staging.bookmundi.com"
    min_wait = 0
    max_wait = 100

