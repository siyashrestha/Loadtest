from locust import HttpUser, TaskSet, task, constant


class UserBehavior(TaskSet):
    wait_time = constant(1)

    @task
    # def get_tests(self):
    #     self.client.post('/user/login?new_ajax',{
    #                                                 "ajaxRequest": "true",
    #                                                 "password": "Test@12345",
    #                                                 "rememberme": "false",
    #                                                 "username": "testqa.bookmundi@gmail.com"
    #                                             })

    @task
    def get_tests(self):
        self.client.post('/nepal',{
                                "ajaxRequest": "true",
                                # "password": "Test@12345",
                                # "rememberme": "false",
                                # "username": "testqa.bookmundi@gmail.com"
                              })
        self.client.post('/asia',{
                                "ajaxRequest": "true",
                              })
        self.client.post('/india',{
                                "ajaxRequest": "true",
                              })
        self.client.post('/argentina',{
                                "ajaxRequest": "true",
                              })
        self.client.post('/nepal?departure_month=2022-01-01',{
                                "ajaxRequest": "true",
                              })
        self.client.post('/asia?privatetours=1',{
                                "ajaxRequest": "true",
                              })
        self.client.post('/europe?luxurytours=1',{
                                "ajaxRequest": "true",
                              })
        self.client.post('/africa?aid=1326',{
                                "ajaxRequest": "true",
                              })
        self.client.post('/africa?age=more-than-40',{
                                "ajaxRequest": "true",
                              })
        self.client.post('/polar/a675-bm?discount=1',{
                                "ajaxRequest": "true",
                              })

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    # host = "https://www.bookmundi.com"
    host = "https://bookmundi:Bookstage2018@staging.bookmundi.com"
    min_wait = 0
    max_wait = 100

