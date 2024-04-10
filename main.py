# Get the indices of a sorted list in Python

a_list = ['a', 'b', 'd', 'c']

indices = sorted(
    range(len(a_list)),
    key=lambda index: a_list[index]
)

print(indices)  # 👉️ [0, 1, 3, 2]


sorted_list = [a_list[index] for index in indices]
print(sorted_list)  # 👉️ ['a', 'b', 'c', 'd']