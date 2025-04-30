lista = [1, 2, 'hola', 3.2, ['a','b']]
s = 'hola carlo tankea'
ls = list(s)
lss = s.split(' ')
print(ls)
print(lss)

l1 = ['do']
l2 = ['mi']
l3 = ['re']
l4 = ['si']
list = l1+l2+l3
list2 = l3+l1
# do mi do re
list[2] = l1[0]
list += l3
print(list)

nums = [3, 5, 2, 1]
nums = sorted(nums)
print(nums)
nums.reverse()
print(nums)
