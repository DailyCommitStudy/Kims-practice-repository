def solution(progresses, speeds):
    answer = []

    # 작업 시작
    while progresses:
        # 작업 진행
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        # 맨 첫 기능이 완성되면 직후 완성된 기능과 함께 배포
        cnt = 0
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1

        if cnt > 0:
            answer.append(cnt)

    return answer