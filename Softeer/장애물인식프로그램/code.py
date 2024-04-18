import sys

# x, y 방향으로 1이 있는 경우 블록으로 묶는다.
def make_block(x, y, block_num, is_visited):
    block_cnt[block_num] += 1

    if y < N-1:
        # y + 방향으로
        if map_list[x][y+1] == '1' and is_visited[x][y+1] == False:
            is_visited[x][y+1] = True
            make_block(x, y+1, block_num, is_visited)
    if x < N-1:
        # X + 방향으로
        if map_list[x+1][y] == '1' and is_visited[x+1][y] == False:
            is_visited[x+1][y] = True
            make_block(x+1, y, block_num, is_visited)

    if y > 0:
        # y - 방향으로
        if map_list[x][y-1] == '1' and is_visited[x][y-1] == False:
            is_visited[x][y-1] = True
            make_block(x, y-1, block_num, is_visited)
    if x > 0:
        # X - 방향으로
        if map_list[x-1][y] == '1' and is_visited[x-1][y] == False:
            is_visited[x-1][y] = True
            make_block(x-1, y, block_num, is_visited)



if __name__ == "__main__":
    N = int(input())

    # 지도 값 로드
    map_list = []
    for _ in range(N):
        map_list.append(input())

    # 방문처리용
    visit_map = []
    # 블록 갯수 기록용
    block_cnt = []

    # 방문 전체 False
    for _ in range(N):
        visit_map.append([False]*len(map_list[0]))


    for i in range(N):
        for j in range(N):
            # 이미 방문한 경우 (i, j는 커지기만 하므로 이미 방문한 경우 block으로 이미 체크된 케이스임)
            if visit_map[i][j]:
                continue
            else:
                visit_map[i][j] = True

            # 처음 만나는 장애물이다.
            if map_list[i][j] == '1':
                block_cnt.append(0)
                make_block(i, j, len(block_cnt)-1, visit_map)

    print(len(block_cnt))
    for cnt in sorted(block_cnt):
        print(cnt)
