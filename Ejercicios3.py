def sumNums(nums, n):
    l = 0
    r = len(nums)-1
    while l < r:
        if (nums[l] + nums[r]) == n:
            print("Num 1: ", nums[l])
            print("Num 2: ", nums[r])
            return
        elif (nums[l] + nums[r]) < n:
            l+=1
        elif (nums[l] + nums[r]) > n:
            r-=1
    return

def aproximacionLeibniz(n):
    sum = 0
    for i in range(n):
        aux = ((-1)**i)/(2*i+1)
        sum += aux
    sum *= 4
    print(sum)
    return


nums = [2,3,7,9,11]
sumNums(nums, 16)
print("APROXIMACION PI:")
aproximacionLeibniz(100000)