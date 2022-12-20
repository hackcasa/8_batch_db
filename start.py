

data = [1,2,3,4,5,6]


row = 6
space = row - 1
star = 1
i = 1
while i <= row:
    #print space
    k = 1
    while k <= space:
        print(' ', end="")
        k = k+1

    #print start
    j = 1
    while j <= star:
        print('*', end="")
        j = j+1
    
    print('\n')

    i = i+1
    space = space - 1
    star = star + 2

#i = 1 *


#no of row = 6 
#no of start /row 1,3,5,7,9,11

# i = 1, j = 1
# i = 2, j = 3 
# i = 3, j = 5 
# i = 4, j = 7 #
# i = 5, j = 9
# i = 6, j = 11


#      *
#     ***
#    *****
#   *******
#  *********
# ***********
