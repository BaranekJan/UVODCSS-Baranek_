numbers = []
karel = 
print("Zadejte přirozená čísla po kazdem cisle zmacknete enter (ukončete zadáním -1):")

while True:
    num = int(input())
    if num == -1:
        break
    if num > 0:
        numbers.append(num)

if not numbers:
    print("Nebyla zadána žádná přirozená čísla.")
else:
    total = 0
    count = 0
    
    for number in numbers:
        total += number
        count += 1

    ap = total / count
    
    count_smaller = 0
    count_greater = 0
    
    for number in numbers:
        if number < ap:
            count_smaller += 1
        elif number > ap:
            count_greater += 1
    
    print("AP:", ap)

    if count_greater > count_smaller:
        print ("zadali jste o",count_greater,"vetsich cisel nez je prumer")
    else:
        print ("zadali jste",count_smaller,"mensich cisel nez je prumer")