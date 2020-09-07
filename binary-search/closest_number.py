def closest_number(arr, target):
    start = 0
    end = len(arr) - 1
    res = -1
    diff = float("inf")
    while start <= end:
        mid = start + (end - start) // 2
        print(mid, arr[mid], diff)
        if arr[mid] >= target:
            c_diff = abs(target - arr[mid])
            if diff > c_diff:
                diff = c_diff
                res = arr[mid]
            end = mid - 1

        else:
            c_diff = abs(target - arr[mid])
            if diff > c_diff:
                diff = c_diff
                res = arr[mid]
            start = mid + 1

    return res


arr1 = [2, 4,5, 6, 7, 8, 8, 9]

print(closest_number(arr1, 4))
