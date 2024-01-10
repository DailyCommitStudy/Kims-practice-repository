# 그룹 단어인 경우 -> abc, happy, a
# 그룹 단어가 아닌 경우 -> abab, aba, hapa 처럼 앞서 나온 단어가 뒤에도 나오는 경우

count = 0
n = int(input())
for _ in range(n):
    case = list(input())

    for c in set(case): # case의 유니크한 알파벳 별로 반복
        idx = case.index(c)
        # c의 첫 인덱스와 개수만큼 슬라이싱 -> 슬라이싱 결과, 두 개 이상의 알파벳 포함이면 그룹 단어가 아니다
        if len(set(case[idx:idx+case.count(c)])) > 1:
            count += 1
            break

print(n-count)