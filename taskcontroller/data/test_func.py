#================================================
# provided_work.py
#================================================

from ..add_work_deco import work_regist

#────────────────────────────────────────────────

@work_regist("test1")
def sum10(*args,**kwargs):
    if args is None : return 10
    return args[0]+10

@work_regist("test2")
def mul3(*args,**kwargs):
    if args is None: return 0
    return args[0]*3