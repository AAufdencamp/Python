with open("file1.txt") as file:
    nums = file.readlines()
    print(nums)

with open("file2.txt") as file:
    nums2 = file.readlines()
    print(nums2)

nums_int = [int(n) for n in nums]
nums2_int = [int(n) for n in nums2]

print(len(nums_int)) #12
print(len(nums2_int)) #13
print(nums_int)
print(nums2_int)

result = [item for item in nums_int if item in nums2_int]
result


print(result)

#This method will be really useful: https://www.w3schools.com/python/ref_file_readlines.asp
#Remember you can check if a value exists in a list using the `in` keyword
#  https://www.w3schools.com/python/ref_keyword_in.asp
# Remember you can use the int() method in python to convert a string into an integer.

###InstructorSol###
# with open("file1.txt") as file1:
#     list1 = file1.readlines()
#
# with open("file2.txt") as file2:
#     list2 = file2.readlines()
#
# result = [int(num) for num in list1 if num in list2]
#
# print(result)