x1 = int(input("x1: "))
x2 = int(input("x2: "))   
y1 = int(input("y1: "))   
y2 = int(input("y2: "))
if (1 <= x1 <= 8) and (1 <= x2 <= 8) and (1 <= y1 <= 8) and (1 <= y2 <= 8):
    if (x1 + x2 + y1 + y2) % 2 == 0:
        print("YES!")

else:
     print("enter number from range(1, 8)!")
