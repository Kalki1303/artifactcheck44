import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 5)
    #host= "http://localhost:8089/"

    @task
    def hello_world(self):
        response = self.client.get("/api/endpoint")
        assert response.status_code == 200,f"request failed"
        #("https://docs.locust.io/en/stable/quickstart.html")
       