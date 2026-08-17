#================================================
# provided_work.py
#================================================

from ..add_work_deco import work_regist

#────────────────────────────────────────────────

@work_regist("test1")
def sum10(num,*args,**kwargs):
    if num is None : return 10
    return num+10

@work_regist("test2")
def mul3(num,*args,**kwargs):
    if num is None: return 0
    return num*3