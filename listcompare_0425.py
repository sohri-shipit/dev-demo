color1 = "Red", "Green", "Orange", "White"
color2 = "Black", "Green", "White", "Pink"
print( set(color1) | set(color2))
a = [10,20,30,20,10,50,60,40,80,50,40]
print("remove duplicates: " , set(a))
def second_smallest(numbers):
    a1, a2 = float('inf'), float('inf')
    print("a1: ", a1, "a2: ", a2)
    for x in numbers:
        if x <= a1:
            a1, a2 = x, a1
        elif x < a2:
            a2 = x
    return a2
print(second_smallest([1, 2, -8, -2, 0]))
