'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    # Your code here
    # z = []
    # it = 0

    # while it < len(arr):
    #     if arr[it] is 0:
    #         z.append(arr.pop(it))
    #     else:
    #         it += 1
    # arr.extend(z)
    # return arr
    count = len(arr) - 1

    for i in range(len(arr)):
        if i >= count:
            return arr
        if arr[i] == 0:
            while (arr[count] == 0) and (count > i):
                count -= 1

            if i == count:
                return arr
            else:
                arr[i], arr[count] = arr[count], arr[i]
                count -= 1
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]
    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
