print("containers:lists")
nums=list(range(5))
print("list 'nums' contains:",nums)
nums[4]="abc"
print("list can contain elements of different  types.Example:",nums)
nums.append("xyz")
print("'nums' after inserting new elements at the end:")
print("sublists:")
print("a slice from index2 to 4:",nums[2:4])
print("a slice from the start to index 2:",nums[2:])
print("a slice of the whole list:",nums[:])
nums[4:]=[8,9]
print("after assigning a new sublist to 'nums':")
for idx,i in enumerate(nums):
    print('%d:%s'%(idx+1,i))
even_squares=[x**2 for x in nums if x%2==0]
print("list of squares of even numbers from 'nums':",even_squares)
