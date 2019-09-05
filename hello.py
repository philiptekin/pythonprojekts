x = eval(input('Enter a number : '))
g = 0.0 
felmellanrum = 0.01
nyaG = felmellanrum**2
gissningar = 0

while (abs(g**2 - x)) >= felmellanrum:
    g += nyaG
    gissningar += 1

print("gissningar " , gissningar)
if abs(g**2-x) >= felmellanrum:
    print('fail ' , x)
else:
    print(g , " rot som är nära " , x)