def solution(grid):
    """
    grid: 2차원 리스트(크기 N x M)
          각 원소는 {-1, 0, 1} 중 하나.
             -1 = 오른쪽 위(행 r-1, 열 c+1)
              0 = 오른쪽   (행 r,   열 c+1)
             +1 = 오른쪽 아래(행 r+1, 열 c+1)

    반환값:
      (original_max, changed_max)
        - original_max : 아무 칸도 바꾸지 않았을 때, 오른쪽 끝 열에서 최다 도착 경로 수
        - changed_max  : 정확히 한 칸의 방향을 변경했을 때 가능한 최댓값
    """
    import sys
    sys.setrecursionlimit(10**7)
    
    N = len(grid)
    if N == 0:
        return (0, 0)
    M = len(grid[0])
    if M == 0:
        return (0, 0)
    
    #-----------------------------------------------------------
    # 1. dp_in[r][c] : 왼쪽 끝 열(c=0)에서 (r,c)에 도달하는 경로의 수
    #    - 모든 (r,0)을 시작점(경로 수 = 1)으로 둔다고 가정
    #-----------------------------------------------------------
    dp_in = [[0]*M for _ in range(N)]
    
    for r in range(N):
        dp_in[r][0] = 1  # 왼쪽 끝 열은 각 행에서 시작 가능하다고 가정
    
    # 이동을 전파
    for c in range(M-1):
        for r in range(N):
            paths = dp_in[r][c]
            if paths == 0:
                continue
            d = grid[r][c]  # -1, 0, +1
            nr = r + d
            nc = c + 1
            if 0 <= nr < N:
                dp_in[nr][nc] += paths
    
    #-----------------------------------------------------------
    # 2. final_dest[r][c] : (r,c)에서 시작했을 때,
    #    기존 grid 방향으로 끝까지 이동하면 오른쪽 끝 열의 어느 행에 도착하는가
    #    (도달 불가능하면 -1)
    #-----------------------------------------------------------
    final_dest = [[-2]*M for _ in range(N)]  # -2: 아직 계산 안 함, -1: 도달불가, >=0: 도착행
    
    def get_final_dest(r, c):
        """ (r,c)의 최종 도착 행 인덱스(없으면 -1)를 반환 """
        # 이미 계산된 경우
        if final_dest[r][c] != -2:
            return final_dest[r][c]
        
        # while 루프를 통해 추적
        cur_r, cur_c = r, c
        while True:
            d = grid[cur_r][cur_c]
            if cur_c == M-1:
                # 오른쪽 끝 열에 이미 도착
                final_dest[cur_r][cur_c] = cur_r
                return cur_r
            
            nr = cur_r + d
            nc = cur_c + 1
            if not (0 <= nr < N and 0 <= nc < M):
                # 범위를 벗어나면 도달 불가능
                final_dest[cur_r][cur_c] = -1
                return -1
            
            # 만약 다음 칸의 final_dest가 이미 확정(-2가 아닌)되어 있다면
            if final_dest[nr][nc] != -2:
                end_r = final_dest[nr][nc]
                # 여기서도 동일한 결과
                final_dest[cur_r][cur_c] = end_r
                return end_r
            else:
                # 아직 확정 안 됐으면, 거기로 이동하여 while 계속
                cur_r, cur_c = nr, nc
    
    # 모든 칸에 대해 final_dest 계산
    for r in range(N):
        for c in range(M):
            if final_dest[r][c] == -2:
                get_final_dest(r, c)
    
    #-----------------------------------------------------------
    # 3. 오른쪽 끝 열 각 행에 도착하는 경로 수 count[r_end] 계산
    #-----------------------------------------------------------
    count = [0]*N
    for r in range(N):
        for c in range(M):
            if dp_in[r][c] == 0:
                continue
            end_r = final_dest[r][c]
            if end_r >= 0:
                count[end_r] += dp_in[r][c]
    
    original_max = max(count)  # 아무 칸도 변경하지 않았을 때 최대 도착 경로 수
    
    #-----------------------------------------------------------
    # 4. 한 칸을 변경했을 때의 최대 도착 경로 수
    #
    #   (r,c)의 방향을 new_d(-1,0,1 중 하나)로 바꾼다고 하면:
    #   - dp_in[r][c] 개의 경로가 원래 final_dest[r][c]에 기여하던 것을 빼고,
    #   - 새로 추적한 도착점에 dp_in[r][c]만큼 더해줌.
    #-----------------------------------------------------------
    changed_max = original_max
    
    def get_final_dest_with_override(r, c, override_dir):
        """(r,c)에서 첫 이동만 override_dir로 이동, 그 뒤부턴 기존 grid 그대로"""
        nr = r + override_dir
        nc = c + 1
        if not (0 <= nr < N and 0 <= nc < M):
            return -1
        # 그 다음부터는 기존 final_dest[nr][nc] 사용
        return final_dest[nr][nc]
    
    import copy
    
    for r in range(N):
        for c in range(M):
            paths_here = dp_in[r][c]
            if paths_here == 0:
                continue
            
            old_dir = grid[r][c]
            old_final = final_dest[r][c]  # 변경 전 (r,c)의 최종 도착 행
            
            for new_dir in [-1, 0, 1]:
                if new_dir == old_dir:
                    continue  # 바뀌지 않으면 의미 없음
                
                new_final = get_final_dest_with_override(r, c, new_dir)
                
                # count[] 복사 후 값 갱신
                new_count = copy.copy(count)
                
                # 원래 기여 빼기
                if old_final >= 0:
                    new_count[old_final] -= paths_here
                # 새 기여 더하기
                if new_final >= 0:
                    new_count[new_final] += paths_here
                
                # 현재 변경에 대한 최댓값
                changed_max = max(changed_max, max(new_count))
    
    return (original_max, changed_max)
print(solution([[0, 0, 1, 0]]))