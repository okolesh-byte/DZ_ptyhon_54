def count_negative(lst, index=0):
    if index == len(lst):
        return 0

    count = count_negative(lst, index + 1)

    if lst[index] < 0:
        count += 1

    return count


numbers = [-2, 3, 8, -11, -4, 6]
n = count_negative(numbers)
print(f"n = {n}")