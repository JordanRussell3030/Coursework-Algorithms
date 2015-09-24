from math import sqrt

total_marks = 0
side_a = 5
side_b = 10
side_c = sqrt(side_a * side_a + side_b * side_b)
length = input("Please input the length of side c")
if length == round(side_c, 1):
    print("Correct")
    total_marks += 2
    print(total_marks)
else:
    print("The answer is {0}".format(round(side_c, 1)))
