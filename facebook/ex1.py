#Given an array having both positive and negative integers.
# The task is to compute the length of the largest subarray with sum 0.
def maxLen(arr):

    max_len = 0


    for i in range(len(arr)):

        curr_sum = 0


        for j in range(i, len(arr)):

            curr_sum += arr[j]

            if curr_sum == 0:
                max_len = max(max_len, j - i + 1)

    return max_len

arr = [15, -2, 2, -8, 1, 7, 10, 13]

print(maxLen(arr))