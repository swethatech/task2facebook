#Given an array arr[] of positive integers of size N. Reverse every sub-array group of size K.
def reverse(arr, n, k):
    i = 0

    while (i < n):

        left = i

        right = min(i + k - 1, n - 1)

        while (left < right):
            arr[left], arr[right] = arr[right], arr[left]
            left += 1;
            right -= 1
        i += k
arr = [5,6,8,9]
k = 3
n = len(arr)
reverse(arr, n, k)

for i in range(0, n):
   print(arr[i], end =" ")
