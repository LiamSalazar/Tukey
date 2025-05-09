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

def area(nums):
    maxArea = -1000
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            base = abs(nums[j]-nums[i])
            altura = min(nums[i], nums[j])
            currentArea = base * altura
            if currentArea >= maxArea:
                maxArea = currentArea
    print(maxArea)
    return

def parentesis(cadena):
    stack = []
    parentesis = "([{}])"
    diccionario = {")":"(", "]":"[", "}":"{"}
    for letra in cadena:
        if letra in parentesis:
            if letra in diccionario:
                top = stack.pop() if stack else '#'
                if top != diccionario[letra]:
                    return False
            else:
                stack.append(letra)
    return not stack


#nums = [2,3,7,9,11]
#sumNums(nums, 16)
#print("APROXIMACION PI:")
#aproximacionLeibniz(100)
#print("AREA")
#nums2 = [15,20,30,10,5]
#area(nums2)
p = parentesis("([])")
print(p)