#================================================
# task_controller.py
#================================================

from multiprocessing import Queue
from multiprocessing import Process

#------------------------------------------------

from .datas import tasks
from .data.task import Task

#────────────────────────────────────────────────

class TaskController(Process):
    _initialized = False

    def __init__(self, result_queue : Queue = None):
        super().__init__()

        self.task_queue = Queue()
        self.result_queue = result_queue


    def __call__(self):
        self.run()
   
    def run(self):
        task_name = self.task_queue.get()
        self.result_queue.put(Task(tasks[task_name]))
