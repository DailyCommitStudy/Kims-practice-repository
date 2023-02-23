n = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7",
     "eight": "8", "nine": "9"}

# 왜 틀렸을까 흠.. 아맞다! replace! ㅇㅈㄹ
# def solution(numbers):
#     answer = ''
#     for i in range(len(numbers)-3):
#         for j in range(3, 6):
#             try:
#                 answer += n[numbers[i:i+j]]
#                 if answer[-1] == n[numbers[i:]] : break
#             except:
#                 continue
#     return answer

def solution(numbers) :
    for k in n :
        numbers = numbers.replace(k, n[k])
    return int(numbers)

print(solution("onetwothreefourfivesixseveneightnine"))