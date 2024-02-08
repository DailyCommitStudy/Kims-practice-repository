## 첫번째 작성 코드
# 리스트에 넣을 때 -1에 있는 값 과 같으면 버린다

def solution(arr):
    answer = [arr[0]]

    for a in arr[1:]:
        if answer[-1] != a:
            answer.append(a)

    return answer

# 다른 사람의 풀이(1)
'''
나와 거의 같지만 디테일이 다른 경우
answer을 정의할 때 빈 리스트로 할 수 있다는 점이 코드가 더 깔끔해 보이긴 하지만
if문에서 비교할 때 a를 리스트로 만들어 비교한다는 점, a[-1:]로 슬라이싱해야하는 점이(결과는 길이가 1이지만)
굳이 그래야 하나? 싶은 생각이 들었다.
달린 댓글을 인용하자면 내가 느낀대로 실제 코드로써의 효율은 불리하다고 한다. 리스트를 생성하는 것이니 메모리 할당 과정이 추가로 붙는다고..
이 코드를 통해 arr이 비었을 때 [-1:] 로 슬라이싱해도 인덱스 오류가 나지 않음을 알 수 있었다.
'''
def solution(arr):
    answer = []

    for a in arr:
        if answer[-1:] != [a]:
            answer.append(a)

    return answer


print(solution([1,1,3,3,0,1,1]))