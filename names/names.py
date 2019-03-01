import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# original unoptimized code
# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# Naive. Still runs in O(n^2) because `in` is an O(n) operation.
# duplicates = []
# for name in names_1:
#     if name in names_2:
#         duplicates.append(name)

# O(min(len(s), len(t)) for average case (some intersections) or
# O(len(s) * len(t)) for worst case (everything intersects). A set is similar
# to a dict per python docs, removing the outer O(n) from the original
# solution, so we have an ~O(n) operation for the given data set.

# Alternatively, we could potentially implement something similar to what Sean
# showed off earlier in the week with a doubly linked list and a dict for
# indexing.
duplicates = set(names_1).intersection(names_2)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
