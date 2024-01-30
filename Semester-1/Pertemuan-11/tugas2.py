from time import perf_counter

# Bubble Sort
def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

rand_array = [7, 1, 36, 26, 63, 93, 55, 16, 19, 38, 74, 65, 18, 59, 8, 43, 24, 79, 49, 35, 23, 78, 51, 2, 46, 28, 60, 76, 10, 85, 66, 29, 82, 58, 69, 75, 48, 100, 5, 32, 40, 33, 34, 90, 81, 42, 57, 44, 41, 77]

print("\nBubble Sort:")
t_start = perf_counter()
bubble_sort(rand_array)
t_end = perf_counter()
print(bubble_sort(rand_array))
print(f"\nTime Start : {t_start}")
print(f"Time End : {t_end}")
print(f"Time Elapsed : {((t_end-t_start) * 1000):.3}\n")

# Selection Sort
def selection_sort(array):
    n = len(array)
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if array[min] > array[j]:
                min = j
        
        array[i], array[min] = array[min], array[i]
    return  array

rand_array2 = [7, 1, 36, 26, 63, 93, 55, 16, 19, 38, 74, 65, 18, 59, 8, 43, 24, 79, 49, 35, 23, 78, 51, 2, 46, 28, 60, 76, 10, 85, 66, 29, 82, 58, 69, 75, 48, 100, 5, 32, 40, 33, 34, 90, 81, 42, 57, 44, 41, 77]

print("\nSelection Sort:")
t2_start = perf_counter()
selection_sort(rand_array2)
t2_end = perf_counter()
print(selection_sort(rand_array2))
print(f"\nTime Start : {t2_start}")
print(f"Time End : {t2_end}")
print(f"Time Elapsed : {((t2_end-t2_start) * 1000):.3}\n")

# Bucket Sort
rand_array3 = [7, 1, 36, 26, 63, 93, 55, 16, 19, 38, 74, 65, 18, 59, 8, 43, 24, 79, 49, 35, 23, 78, 51, 2, 46, 28, 60, 76, 10, 85, 66, 29, 82, 58, 69, 75, 48, 100, 5, 32, 40, 33, 34, 90, 81, 42, 57, 44, 41, 77]

array_dumb_groups = []

def bucket_sort(array):
    for i in range(min(rand_array3), max(rand_array3) + 15, 5):
        group_start = i
        group_end = i + 4
        # print(group_start, " - ", group_end)
        
        bucket = [number for number in rand_array3 if group_start <= number <= group_end]
        
        for k in range(1, len(bucket)):
            key = bucket[k]
            j = k - 1
            while j >= 0 and key < bucket[j]:
                bucket[j + 1] = bucket[j]
                j -= 1
            bucket[j + 1] = key
        
        array_dumb_groups.append(bucket)

    for array_dumb_group in array_dumb_groups:
        for k in range(1, len(array_dumb_group)):
            key = array_dumb_group[k]
            j = k - 1
            while j >= 0 and key < array_dumb_group[j]:
                array_dumb_group[j + 1] = array_dumb_group[j]
                j -= 1
            array_dumb_group[j + 1] = key

    combine_array = []
    for array_dumb_group in array_dumb_groups:
        combine_array.extend(array_dumb_group)

    # print(f"\nArray Belum Dikelompokkan dan Diurutkan:\n{rand_array3}")
    # print(f"\nArray Dikelompokkan dan Diurutkan:\n{array_dumb_groups}")
    print(combine_array)

print("\nBucket Sort:")
t3_start = perf_counter()
bucket_sort(rand_array3)
t3_end = perf_counter()
print(f"\nTime Start : {t3_start}")
print(f"Time End : {t3_end}")
print(f"Time Elapsed : {((t3_end-t3_start) * 1000):.3}\n")