# 1. 앞 사람이 말한 단어의 마지막 문자로 시작해야 함
# 2. 이전에 등장했던 단어는 사용할 수 없다
# 3. 한 글자인 단어는 인정되지 않는다
# n번째 사람이 n번째 단어를 말하고..
# 몇 번째 사람인지는 어덯게? -> i%n+1
# 몇 번째로 말한 건지는 어떻게? -> i//n

def solution(n, words):
    answer = [0, 0]

    for i, s in enumerate(words):
        if i == 0: continue
        if s[0] != words[i - 1][-1] or s in words[:i] or len(s) < 2:
            answer = [i % n + 1, i // n + 1]
            break

    return answer
