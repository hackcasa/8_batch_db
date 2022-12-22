'''Given an array of integers nums and an integer target, return indices of the 
two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and 
you may not use the same element twice.
You can return the answer in any order.'''


# def sum2(nums, k):
#     for i in nums:
#         for j in nums[1:]:
#             if i+j == k:
#                 return [i,j]



# def sum21(nums,k):
#     map={}

#     for i in range(len(nums)):
#         num = nums[i]
#         comp = k - num
#         map[comp] = i
    
#     for i in range(len(nums)):
#         num = nums[i]
#         if num in map:
#             return [nums[i], nums[map[num]]]
    

# nums = [1,6,2,3,8,3,2]
# k = 4
# print(sum21(nums,k))

# def sum3(nums,k):
#     for num in nums:
#         rem = k-num
#         two_no = sum21(nums[1:],rem)

#         return (num, two_no)



# nums = [1,6,2,3,8,3,2]
# k = 6
# print(sum3(nums,k))

#find 3 no of sum k




# arr = [[1,2,3],
#         [4,5,2],
#         [1,2,1],
#         ]


# max = 0
# for i in arr:
#     for j in i:
#         if j > max:
#             max = j

# print(max)



# arr = [1,2,3,5,7,3,2,4]

# def find_max():
#     max = 0
#     for i in arr:
#         if i > max:
#             maz = i

#     return max




#     4,7,1,3,5,7,4,5,7,8

#     4 - 7 -> 7
#     7 - 1 -> 1


#     7 - 8 -> 8

#      4,7,1,3,5 - 7,8 - 5

#      4,7,1,3,5  - 7,4,5,7,8 -> 7,4,5,7,8
#      7,4 - 7,8 -> 7,8
#      7 - 8 -> 8
#      8 - 5 -> 8


#question reduce the array and remove max in each loop
#add removed max of each loop and return 

arr = [[1,2,3],
        [4,5,2],
        [1,2,1],
        ]

5


arr = [[1,2],
        [4,2],
        [1,1],
        ]

4

arr = [[1],
        [2],
        [1],
        ]

2


