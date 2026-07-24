from math import sin,cos,pi

x = float(input("Enter the x coordinate: "))
y = float(input("Enter the y coordinate: "))
r = float(input("Enter the radius: "))
d = float (input("Enter the theta in degress: "))

theta = d * pi / 180

x_coordinate = cos(theta)
y_coordinate = sin(theta)
x_coordinate = x / r
y_coordinate = y / r
print("The Answer is x-coordinate",x_coordinate)
print("The Answer is y-coordinate",y_coordinate)