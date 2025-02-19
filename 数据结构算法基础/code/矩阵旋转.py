# from copy import deepcopy
#
# # matrix = [
# #   [5, 1, 9, 11],
# #   [2, 4, 8, 10],
# #   [13, 3, 6, 7],
# #   [15,14,12,16]
# # ]
#
# matrix1 = [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ]
#
#
# def rotate1(matrix):
#     """
#     :type matrix: List[List[int]]
#     :rtype: None Do not return anything, modify matrix in-place instead.
#     """
#     """
#     原地旋转
#     """
#     n = len(matrix)
#     arr = deepcopy(matrix)
#     for i in range(n):
#         for j in range(n):
#             arr[j][n - 1 - i] = matrix[i][j]
#
#     matrix[:] = arr  # 题目要求返回原数组，原地旋转
#     return arr
#
# print(rotate1(matrix1))


matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

def rotate(matrix):
    """
    原地旋转
    关键等式：matrix[col][n−row−1] = matrix[row][col],
    即：matrix[row][col] 旋转后应该在 matrix[col][n−row−1]
    反复套用等式，得到：
        matrix[j][n - 1 - i] = matrix[i][j]
        matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
        matrix[n - 1 - j][i]= matrix[n - 1 - i][n - 1 - j]
        matrix[i][j] = matrix[n - 1 - j][i]
    因为每次枚举涉及旋转4个位置，枚举时：
    n若为偶数，i和j都只需枚举一半，即n/2，即四分之一大小矩阵，就能覆盖全部旋转
    n若为奇数，i枚举(n+1)/2, j枚举n/2，中心位置旋转后不变，也能覆盖全部旋转
    """
    n = len(matrix)
    for i in range(n // 2):
        for j in range((n+1) // 2):
            temp = matrix[j][n - 1 - i] # 首先保存第一个被覆盖的值
            # 反复套用matrix[col][n−row−1] = matrix[row][col],
            matrix[j][n - 1 - i] = matrix[i][j]
            matrix[i][j] = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
            matrix[n - 1 - i][n - 1 - j] = temp
rotate(matrix)
print(matrix)


# matrix = [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ]
# def rotate(matrix):
#     n = len(matrix)
#     for i in range(n // 2):
#         for j in range((n + 1) // 2):
#             matrix[i][j], matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1] \
#                 = matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1], matrix[i][j]
#
# rotate(matrix)
# print(matrix)

