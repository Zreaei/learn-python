# array = []
# buck1 = []
# buck2 = []
# buck3 = []
# buck4 = []
# buck5 = []

# while True:
#     try:
#         a = int(input("masukan angka: "))
#         array.append(a)
#     except ValueError:
#         break

# # for i in range(0,len(array)+10,5):
# #     array_dumb = []
# #     array_dumb.append(i)
# #     array_dumb.append(i+4)

# #     print(array_dumb)

# for i in range(0,len(array)):
#     if array <= 5:
#         array.append(buck1)
#     elif array <= 10:
#         array.append(buck2)
#     elif array <= 15:
#         array.append(buck3)
#     elif array <= 20:
#         array.append(buck4)
#     elif array <= 25:
#         array.append(buck5)

# print(buck1)

# Bucket Sort in Python

# array = []

# def bucketSort(array):
#     bucket = []

#     # Create empty buckets
#     for i in range(len(array)):
#         bucket.append([])

#     return array

# while True:
#     try:
#         a = int(input("masukan angka: "))
#         array.append(a)
#     except ValueError:
#         break

# print(bucketSort(array))

    # # Insert elements into their respective buckets
    # for j in array:
    #     index_b = int(10 * j)
    #     bucket[index_b].append(j)

    # # Sort the elements of each bucket
    # for i in range(len(array)):
    #     bucket[i] = sorted(bucket[i])

    # # Get the sorted elements
    # k = 0
    # for i in range(len(array)):
    #     for j in range(len(bucket[i])):
    #         array[k] = bucket[i][j]
    #         k += 1
    # return array


# array = [.42, .32, .33, .52, .37, .47, .51]
# print("Sorted Array in descending order is")
# print(bucketSort(array))

# Fix
# Bucket Sort
rand_array3 = [7, 1, 36, 26, 63, 93, 55, 16, 19, 38, 74, 65, 18, 59, 8, 43, 24, 79, 49, 35, 23, 78, 51, 2, 46, 28, 60, 76, 10, 85, 66, 29, 82, 58, 69, 75, 48, 100, 5, 32, 40, 33, 34, 90, 81, 42, 57, 44, 41, 77]

array_dumb_groups = []

def bucket_sort(array):
    for i in range(min(rand_array3), max(rand_array3) + 15, 5):
        group_start = i
        group_end = i + 4
        print(group_start, " - ", group_end)
        
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

    print(f"\nArray Belum Dikelompokkan dan Diurutkan:\n{rand_array3}")
    print(f"\nArray Dikelompokkan dan Diurutkan:\n{array_dumb_groups}")
    print(f"\nArray Dikelompokkan dan Diurutkan:\n{combine_array}")

print("\nBucket Sort:")
bucket_sort(rand_array3)