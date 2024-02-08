def solution(lines):
    # 선분의 왼쪽 끝점 기준 오름차순 정렬
    lines.sort(key=lambda x: x[0])
    answer = set()

    for i in range(2):
        for j in range(i + 1, 3):
            answer.update(range(max(lines[i][0], lines[j][0]), min(lines[i][1], lines[j][1])))

    return len(answer)