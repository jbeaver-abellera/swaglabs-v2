# import time
# from locust import HttpUser, task, between
# from utils.Constants import Constants
#
# class loadTest(HttpUser):
#     wait_time = between(1, 5)
#
#     @task
#     def swaglabs(self):
#         self.client.get(url= Constants.WEBSITE_URL, name="swaglabs")
#
#     @task
#     def the_internet(self):
#         self.client.get(url="https://the-internet.herokuapp.com/", name="the-internet")