import time
from bg_task_queue import BackgroundTaskQueue

tq = BackgroundTaskQueue(verbose=True, max_worker=2)

# add function using decorator
@tq.task
def task_a(i):
    time.sleep(1)
    print(f'Task_a({i}) Finished')

# or add manually
def task_b(a=0):
    time.sleep(3)
    print(f'Task_b({a}) Finished')

tq.task(task_b)

tq.add_task("task_a", 100)
tq.add_task("task_b", a=200)
tq.add_task("task_a", 300)
tq.add_task("task_a", 400)

while True:
    summary = {"pending": 0, "running": 0, "stopped": 0, "errored": 0, "success": 0}
    tasks = tq.get_all_tasks()
    for t in tq.get_all_tasks():
        print(t)
        summary[t.status] += 1
    print(summary)
    time.sleep(1)