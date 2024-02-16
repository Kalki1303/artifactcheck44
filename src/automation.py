import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 5)
    #host= "http://localhost:8089/"
    

    @task
    def hello_world(self):
        self.url ="https://postman-echo.com/get?test=123"
        response = self.client.get(self.url)
        assert response.status_code == 200,f"request failed"
        #("https://docs.locust.io/en/stable/quickstart.html")
       