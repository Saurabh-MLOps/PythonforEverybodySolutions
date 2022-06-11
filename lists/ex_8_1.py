def chop(lst):
    del lst[0]
    del lst[-1:]
def middle(lst):
    new = lst[1:]
    del new[-1:]
    return new
list1 = [123,345,567,789]
list2 = [111,222,333,444]
choplist = chop(list1)
print(list1)                       #Prints [345, 567]
print(choplist)                    #Prints None
middlelist = middle(list2)
print(list2)                       #Prints [111, 222, 333, 444]
print(middlelist)                  #Prints [222, 333]
