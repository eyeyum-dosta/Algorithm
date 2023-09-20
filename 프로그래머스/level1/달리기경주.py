# 2중 for 문 - Runtime error
def solution(players, callings):
    for i in range(len(callings)):
        for j in range(len(players)):
            if callings[i] == players[j]:
                players[j - 1], players[j] = players[j], players[j - 1]

    return players

# hash테이블 구성 - PASS

def solution(players, callings):
    # 해쉬테이블 구성
    Table = {}
    for i in range(len(players)):
        Table[players[i]] = i

    # calling 순서대로 players, 해쉬테이블 재구성
    for name in callings:
        idx = Table[name]
        Table[name] -= 1
        players[idx - 1], players[idx] = players[idx], players[idx - 1]
        Table[players[idx]] = idx

    return players
