from locust import HttpUser, task, between, events

class APILoadUser(HttpUser):
    wait_time = between(0.1, 0.3)

    @task
    def ping(self):
        r = self.client.get("/ping")
        r.raise_for_status()

@events.quitting.add_listener
def _(environment, **kwargs):
    if (environment.stats.total.fail_ratio > 0.01 or
        environment.stats.total.avg_response_time > 500):
        environment.process_exit_code = 1
