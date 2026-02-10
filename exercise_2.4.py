
x = float(input("Enter a distance x in ly: "))* 9.461e15
v = float(input("Enter a speed v as a fraction of the speed of light c: "))

c = 3e8
t = x/(v*c)
tprime = t*(1-((v*c)**2)/(c**2))**(1/2)
print("Time elapsed on Earth=", t/60/60/24/365, ";Time elapsed in spaceship=", tprime/60/60/24/365)