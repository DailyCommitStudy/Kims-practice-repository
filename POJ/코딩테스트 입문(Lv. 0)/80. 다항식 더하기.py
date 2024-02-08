# 하.. 이걸 이렇게 더럽게.. 근데 그럴 수밖에 없는듯
def solution(polynomial):
    x, a = 0, 0
    for i in polynomial.split(' + '):
        if 'x' in i:
            if i == 'x':x += 1
            else:x += int(i[:-1])
        else: a += int(i)

    if x > 0 and a > 0:answer = f'{x}x + {a}'
    elif a == 0: answer = f'{x}x'
    else:answer = f'{a}'

    if answer[:2] == '1x': answer = 'x' + answer[2:]

    return answer

# isdigit을 써보자~! 다른 사람 코드 참고
def solution(polynomial):
    x, a = 0, 0
    for i in polynomial.split(' + '):
        if i.isdigit() : a += int(i)
        else : x += int(i[:-1]) if i != 'x' else 1

    if x == 0 : return str(a)
    elif x == 1 : return f'x + {a}' if a > 0 else 'x'
    else : return f'{x}x + {a}' if a > 0 else f'{x}x'


print(solution('5x + 12x + 10 + 3'))