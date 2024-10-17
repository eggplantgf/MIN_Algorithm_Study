def solution(board):
    n = len(board)
    answer = []
    arr = []
    filtered_arr = []
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        arr.append([i + x, j + y])
    
    # 중복 제거
    for v in arr:
        if v not in answer:
            answer.append(v)
            
    # 리스트 경계 확인
    for v in answer:
        if 0 <= v[0] < n and 0 <= v[1] < n:
            filtered_arr.append(v)
    
    return n * n - len(filtered_arr)
