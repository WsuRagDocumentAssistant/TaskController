#================================================
# Task.py
#================================================

from ..datas import works
from .exception import FuncCreateException

#────────────────────────────────────────────────

class Task:
    def __init__(self, work_names):
        if not work_names:
            raise FuncCreateException("연결할 work가 하나도 지정되지 않음")

        self.func_lst = []
        for name in work_names:
            if not (name in list(works.keys())):
                raise FuncCreateException(f"등록되지 않은 work: '{name}'")
            self.func_lst.append(works[name])

    def __call__(self, *args, **kwargs):
        head, tail = self.func_lst[0], self.func_lst[1:]
        ret = head(*args, **kwargs)
        for func in tail:
            ret = func(ret)
        return ret

    @staticmethod
    def _func_create(work_names):
        if not work_names:
            raise FuncCreateException("연결할 work가 하나도 지정되지 않음")

        func_lst = []
        for name in work_names:
            if not (name in list(works.keys())):
                raise FuncCreateException(f"등록되지 않은 work: '{name}'")
            func_lst.append(works[name])
