
#      *
#     ***
#    *****
#   *******
#  *********
# ***********


# simple start
def print_star(star,space):
    print(" "*space,'*'* star)
    if star > 10:
        return

    print_star(star+2,space-1)
    return 

#reverse star
def print_star(star,space):
    print(" "*space,'*'* star)
    if star > 10:
        return

    print_star(star+2,space-1)

    return 



print_star(1,9)



#stack last in first out
#queue first in first out