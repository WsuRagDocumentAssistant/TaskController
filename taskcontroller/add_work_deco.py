#================================================
# add_work_deco.py
#================================================

from .datas import works, work_lst

#────────────────────────────────────────────────

def work_regist(work_name : str):
    """
    [함수를 works에 저장하는 데코레이터]
    if 인자 is None : 일 때를 함수 상위에 꼭 정의해 주세요
    """
    def workfunc(func):
        works[work_name] = func
        work_lst.append(work_name)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return workfunc
        