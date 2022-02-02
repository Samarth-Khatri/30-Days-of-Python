# FOR LOOP
bag = [123, 456, 789, 135, 246, 579, 6810]

print(len(bag))

for items in bag:
    print(items)

i=0
for item in bag:
    i+=1
    print(i)

for item in bag:
    if item == 6810:
        print("Found Item")


# WHILE LOOP
j=1
while j<=10:
    print(j)
    j+=1
