legth_side_a = int(input("enter the length of the side a in cm"))
legth_side_b = int(input("enter the length of the side b in cm"))
legth_side_c = int(input("enter the length of the side c in cm"))
if legth_side_a + legth_side_b < legth_side_c or legth_side_a +legth_side_c < legth_side_b or legth_side_b + legth_side_c < legth_side_a:
    print("the length of the sides of a triangle triangle inequality, the triangle does not exist")
elif legth_side_a == legth_side_b == legth_side_c:
    print("triangle is equilateral")
elif legth_side_a == legth_side_b or legth_side_a == legth_side_c or legth_side_b == legth_side_c:
    print("triangle is isosceles")
else:
    print("triangle is general")