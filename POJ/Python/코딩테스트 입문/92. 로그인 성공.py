# def solution(id_pw, db):
#     id = [i[0] for i in db]
#     pw = [i[1] for i in db]
#
#     if id_pw[0] in id:
#         if db[id.index(id_pw[0])][1] == id_pw[1]:
#             return "login"
#         else:
#             return "wrong pw"
#     else:
#         return "fail"

## 두 번째
# 딕셔너리 활용
def solution(id_pw, db):
    d = dict(db)

    if id_pw[0] in d.keys():
        if d[id_pw[0]] == id_pw[1]:
            return "login"
        else:
            return "wrong pw"
    else:
        return "fail"

print(solution(["meosseugi", "1234"], [["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]]))