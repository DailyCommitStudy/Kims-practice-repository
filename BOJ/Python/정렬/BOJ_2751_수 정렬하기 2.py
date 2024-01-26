# (24.01.21) 시간복잡도가 낮은 굉장히 효율적이게 해야한다 -> 방법 더 알아보고 ㄱㄱ
# (24.01.26) sys 를 사용하니 시간초과 자체는 해결. 시간 안에 풀 수 있게 됐다.
# --> 1316ms
# (24.01.26) 조금 더 빠르게 해보기 위해 sorted() 말고 sort() 도입
# --> 1336ms.. 음.. 속도가 더.. 예.. 안좋네.. sorted()가 더 낫나보다
import sys

case = [int(sys.stdin.readline()) for i in range(int(input()))]

for c in case : print(c)
