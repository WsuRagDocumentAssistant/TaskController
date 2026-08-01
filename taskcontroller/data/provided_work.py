#================================================
# provided_work.py
#================================================

from ..add_work_deco import work_regist

#────────────────────────────────────────────────

@work_regist("sum10")
def sum10(num):
    if num is None : return 10
    return num+10

@work_regist("mul3")
def mul3(num):
    return num*3