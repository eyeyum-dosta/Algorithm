def solution(name, yearning, photo):
    answer = []
    table = {}
    #각 사람의 추억점수를 해쉬테이블로 저장
    for i in range(len(name)):
        table[name[i]] = yearning[i]

    for i in range(len(photo)):
        point = 0
        for j in photo[i]:
            if j in name:
                point += table[j]
            else:
                continue
        answer.append(point)

    return answer