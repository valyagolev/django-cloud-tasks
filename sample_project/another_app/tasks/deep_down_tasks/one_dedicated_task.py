from django_cloud_tasks.tasks import Task


class OneBigDedicatedTask(Task):
    def run(self, name):
        return f"Chuck Norris is better than {name}"
