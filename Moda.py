nums = [2,3,2,5,2,3,5,3,3]
visited = {}
mayor = -float('inf')
moda = None
for num in nums:
    if num in visited:
        visited[num] += 1
    else:
        visited[num] = 1
    if visited[num] >= mayor:
        mayor = visited[num]
        moda = num
print("Moda: ", num)
print("Repeticiones: ", mayor)