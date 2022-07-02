def get_new_lock(lock, N):
    new_lock = [[0] * (N * 3) for _ in range(N * 3)]
    for i in range(N) :
        for j in range(N) :
            new_lock[i + N][j + N] = lock[i][j]
    return new_lock

def rotate_matrix_by_90_degree(key):
    row = len(key)
    col = len(key[0])
    result = [[0] * row for _ in range(col)]
    for i in range(row) :
        for j in range(col) :
            result[j][row-i-1] = key[i][j]
    return result

def check(new_lock):
    lock_len = len(new_lock) // 3
    for i in range(lock_len, lock_len * 2) :
        for j in range(lock_len, lock_len * 2) :
            if new_lock[i][j] != 1 :
                return False
    return True
    
    
def solution(key, lock):
    M = len(key)
    N = len(lock)
    # 자물쇠의 크기를 기존의 3배로 변환
    new_lock = get_new_lock(lock, N)
    
    # 4가지 방향 모두 키를 돌려가면서 확인
    for rotation in range(4) :
        key = rotate_matrix_by_90_degree(key)
        for x in range(N * 2) :
            for y in range(N * 2) :
                # 자물쇠에 키 끼워넣어보기
                for i in range(M) :
                    for j in range(M) :
                        new_lock[x + i][y + j] += key[i][j]
                # 키가 자물쇠에 들어맞는지 검사
                if check(new_lock) == True :
                    return True
                # 자물쇠에서 열쇠 빼기
                for i in range(M) :
                    for j in range(M) :
                        new_lock[x + i][y + j] -= key[i][j]
    return False
