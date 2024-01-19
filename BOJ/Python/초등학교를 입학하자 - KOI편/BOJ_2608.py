## 진짜 예~전에 못 풀었던 것 해결했다~ 굿~ ^^

# 보통 큰 숫자를 왼쪽, 작은 숫자를 오른쪽에. 그 값은 모든 숫자의 값을 더한 값이 된다
# LX = 50 + 10, MLI = 1000 + 50 + 1 = 1051

# V, L, D 한 번만
# I, X, C, M 연속해서 세 번만
# 만약 위 조건에 걸려서 못할 경우는 작은 수를 왼쪽에 두면서 표현하는 수밖에 없음.

# 작은 숫자가 큰 숫자의 왼족에 오는 경우는 IV = 4, IX = 9, XL = 40, XC = 90 CD = 400 CM = 900. 얘네도 한 번만
# 같이 쓸 수 없음 IV, IX / XL, XC / CD, CM
# 가능한 가장 적은 개수의 로마 숫자들로 표현

# 일의 자릿수부터 계산해줘야 하는 거 아닌가
# 1~3 -> I로, 4면 IV, 5면 V, 6 VI, 7 VII, 8 VIII, 9 VIV, 10 IXI
# 10이면 IXI(9+1), VIVI X 1, 4, 5, 9

# 235 -> CCXXXV
# 2493 -> MMCD'XC'III
# 만약, 그 수가 1~3이면 1이 들어가는 숫자로 커버 가능
# 그 수가 4라면 작은 수 - 큰 수 를 해줘야함. ex) 40이면, 10 50을 해줘야한다는 것
# 1~3 (I*n) / 4 (IV) / 5 (V) / 6 ~ 8 (V + I*n) / 9 (IX)


nums = {'I':1, 'V':5,'X':10, 'L':50, 'C':100, 'D':500, 'M':1000,
       'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
nums_r = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M',
            4:'IV', 9:'IX', 40:'XL', 90:'XC', 400:'CD', 900:'CM'}


def conv(a):
    i, res = 0, 0
    while i < len(a):
        # 만약 자신의 오른쪽에 있는 애보다 작으면 두 자릿수
        if i < len(a)-1 and nums[a[i]] < nums[a[i+1]]:
            res += nums[a[i:i+2]]
            i += 2
        else:
            res += nums[a[i]]
            i += 1
    return res

# 아라비아 숫자 합
s = conv(input()) + conv(input())
print(s)

res = []
s = str(s)[::-1]    # 가장 마지막 자릿수부터 접근
# 거꾸로 입력되기 때문에 순서에
for i in range(len(s)): # 10의 n승 별 반복
    c = int(s[i])

    # 각 숫자별로 매핑
    if c < 4: res.append(nums_r[1 * (10**i)] * c)
    elif c == 4: res.append(nums_r[4 * (10**i)])
    elif c == 5: res.append(nums_r[5 * (10**i)])
    elif c < 9: res.append(nums_r[5 * (10**i)] + nums_r[1 * (10**i)]  * (c-5))
    else : res.append(nums_r[9 * (10**i)])

print("".join(res[::-1]))