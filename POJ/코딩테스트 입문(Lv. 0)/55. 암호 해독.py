def solution(cipher, code):
    return ''.join(cipher[i] for i in range(code-1, len(cipher), code))

# 아! 인덱싱으로도 가능하구나
def solution(cipher, code):
    return cipher[code-1::code]