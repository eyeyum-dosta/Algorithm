def solution(wallpaper):
    answer = []
    folder = []
    # 폴더 위치 2차원 리스트
    lux, luy = 50, 50
    rdx, rdy = 0, 0
    for line in wallpaper:
        li = []
        for letter in line:
            li.append(letter)
        folder.append(li)
    for index_y in range(len(folder)):
        for index_x in range(len(folder[0])):
            if folder[index_y][index_x] == '#':
                # 시작점
                if index_y <= luy:
                    luy = index_y
                if index_x <= lux:
                    lux = index_x
                    # 끝점
                if index_y + 1 >= rdy:
                    rdy = index_y + 1
                if index_x + 1 >= rdx:
                    rdx = index_x + 1

    return [luy, lux, rdy, rdx]
