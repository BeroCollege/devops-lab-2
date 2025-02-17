usrinput = int(input("Please enter a number: "))

small = usrinput
large = usrinput

usrinput2 = int(input("Please enter a number: "))

if usrinput2 < small:
    small = usrinput2

if usrinput2 > large:
    large = usrinput2

usrinput3 = int(input("Please enter a number: "))

if usrinput3 < small:
    small = usrinput2

if usrinput3 > large:
    large = usrinput2
    
usrinput4 = int(input("Please enter a number: "))

if usrinput4 < small:
    small = usrinput2

if usrinput4 > large:
    large = usrinput2
    
usrinput5 = int(input("Please enter a number: "))
if usrinput5 < small:
    small = usrinput2

if usrinput5 > large:
    large = usrinput2
    
total = usrinput + usrinput2 + usrinput3 + usrinput4 + usrinput5
average = total / 5


print(int(average))
print(int(small))
print(int(large))