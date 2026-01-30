# Problem 30: 
def area_of_circle(radius):
    pi = 3.14
    area = pi * radius * radius
    return area

r = 5   # changed from "5" (string) to 5 (int)
print(f"Area: {area_of_circle(r)}")