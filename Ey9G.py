import numpy as np

input_matrix  = np.array([[2, 3, 1, 6],[1, 4, 8, 2],[2, 4, 10, 4],[2, 5, 6, 1]])
filter_matrix = np.array([[2, 0, 1],[1, 1, 0],[0, 2, 1]])
output_data   = []

print("入力データ")
print(input_matrix)
print("フィルターデータ")
print(filter_matrix)

for i in range(0, 2):
  row_data = []
  for j in range(0, 2):
    product_array = input_matrix[i:3+i, j:3+j]*filter_matrix
    row_data.append(np.sum(product_array))
  output_data.append(row_data)

output_matrix = np.matrix(output_data)

print("出力データ")
print(output_matrix)
