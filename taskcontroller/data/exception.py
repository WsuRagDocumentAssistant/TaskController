#================================================
# exception.py
#================================================


def 

class FuncCreateException(Exception):
    def __init__(self, msg:str):
        base = "[함수 생성 오류] " + msg
        super().__init__(base)