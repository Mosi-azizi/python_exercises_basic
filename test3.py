def diagonalDifference(arr):
    n = len(arr)
    print(n)
    left_to_right_sum = 0
    right_to_left_sum = 0

    # Iterate over the matrix and accumulate the sums
    for i in range(n):
        left_to_right_sum += arr[i][i]
        right_to_left_sum += arr[i][n - i - 1]

    # Calculate the absolute difference
    diff = abs(left_to_right_sum - right_to_left_sum)

    return diff
arr = [[1, 2, 3],
       [4, 5, 6],
       [9, 8, 9]]

result = diagonalDifference(arr)
print(result)