# 짝수번째 -> 대문자
# 홀수번째 -> 소문자
# 문자열 전체가 아닌 단어 기준. 즉 공백이 있을 때마다 새롭게 봐야함
# 단어 사이의 공백은 1개 이상이므로 무조건 공백으로 split할 수는 없다..
# 그러면 그냥 for로 전부 반복시키면서 공백일 때마다 인덱스 초기화하는 ㄱㅔ 맞다..

# 와 split()을 하면 공백이 여러개일 때 다 사라지고 " " 로 스플릿을 해야
# 공백ㅇ ㅣ2개 이상일 때도.. 그.. 닷 ㅣ합쳤을 때 그대로 나오게 된다..
# 하..........안그래도 테스트했었는데 미친 ㅏ하..이걸 생각 못했다...


# def solution(s):
#     answer = ''
#     idx = 0
#     for c in s:
#         if c == ' ':
#             idx = 0
#             answer += ' '
#         # 짝
#         elif idx % 2 == 0:
#             answer += c.upper()
#             idx += 1
#         # 홀
#         elif idx % 2 == 1:
#             answer += c.lower()
#             idx += 1
#
#     return answer


## 다른 사람 코드
# 와.. 미친듯
# " " 로 스플릿해서 하는 게 된다고?
#
def solution(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))

print("ab   c d  e")
print("ab   c d  e".split(" "))
print(solution("ab   c d  e"))