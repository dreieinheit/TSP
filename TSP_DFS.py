import time
import sys
t = []

INF = 1e+9
n = 16
mat = [
    [0, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80],
    [5, 0, 9, 10, 18, 21, 26, 31, 36, 41, 46, 51, 56, 61, 66, 71],
    [6, 13, 0, 12, 19, 22, 27, 32, 37, 42, 47, 52, 57, 62, 67, 72],
    [8, 8, 9, 0, 17, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70],
    [14, 18, 19, 17, 0, 13, 24, 29, 34, 39, 44, 49, 54, 59, 64, 69],
    [21, 21, 22, 20, 13, 0, 11, 16, 23, 28, 33, 38, 43, 48, 53, 58],
    [26, 26, 27, 25, 11, 11, 0, 5, 12, 17, 24, 29, 34, 39, 44, 49],
    [31, 31, 32, 30, 16, 5, 0, 4, 9, 14, 21, 26, 31, 36, 41, 46],
    [36, 36, 37, 35, 23, 12, 4, 0, 7, 12, 19, 24, 29, 34, 39, 44],
    [41, 41, 42, 40, 28, 17, 9, 7, 0, 5, 10, 17, 22, 27, 32, 37],
    [46, 46, 47, 45, 33, 24, 19, 12, 5, 0, 3, 8, 13, 18, 23, 28],
    [51, 51, 52, 50, 38, 29, 21, 16, 10, 3, 0, 2, 7, 12, 17, 22],
    [56, 56, 57, 55, 43, 34, 26, 21, 15, 8, 2, 0, 5, 10, 15, 20],
    [61, 61, 62, 60, 48, 39, 31, 26, 20, 13, 7, 2, 0, 3, 8, 13],
    [66, 66, 67, 65, 53, 44, 36, 31, 25, 18, 12, 7, 3, 0, 2, 7],
    [71, 71, 72, 70, 58, 51, 43, 38, 32, 25, 19, 14, 10, 5, 2, 0]
]

for i in range(10):

    start = time.time()  # 시작 시간 저장

    dp = [[None for _ in range(1 << n)] for _ in range(n)]  # 모든 방문 가능 경우의 수
    chk = 1

    def search(node, chk):
        if chk == (1 << n)-1:
            if mat[node][0] != 0:
                return mat[node][0]
            else:
                return INF

        if dp[node][chk] != None:
            return dp[node][chk]

        min_value = INF
        for i in range(1, n):
            if (mat[node][i] != 0) and ((chk & (1 << i)) == 0):  # 연결되어 있으며 방문한적 없을때
                min_value = min(min_value, search(
                    i, chk | (1 << i)) + mat[node][i])
        dp[node][chk] = min_value

        return min_value

    answer = search(0, chk)
    t.append(time.time() - start)  # 현재시각 - 시작시간 = 실행 시간

print(answer)
print("DFS 평균 실행시간: ", sum(t)/len(t))