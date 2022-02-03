# Conditional are defined in terms of Boolean values True and False

print("justin" == "Justin")
print("justin" == "justin")

list_a = [1,2,3]
list_b = [1,2,3]
list_c = [4,5,6]

print(list_a==list_b)
print(list_b==list_c)
print(list_a!=list_c)

obj_a = True
obj_b = False

print(obj_a == obj_b)
print(not obj_a == obj_b) #use not for inverse

print(3**3 == 9)
print(3**3 != 27)

list = [1,2,3,4,5,6,7,8,9,10]

for i in list:
    if (i%2==0):
        print("even")
    elif (i==1):
        print("neither prime nor composite")
    else:
        print(i)

list_d = ["Samarth", 123, "Khatri", 456, 789]
list_e = []
list_f = []

for i in list_d:
    if isinstance(i, int): # isinstance for comparison
        list_e.append(i)
    elif isinstance(i, str):
        list_f.append(i)

print(list_d)
print(list_e)
print(list_f)

x=0
for items in list_d:
    print(list_d[x])
    x += 1



# y=0
# list_d = ["Samarth", 123, "Khatri", 456, 149]
# list_e = []
# list_f = []
#
# for item in list_d:
#     if isinstance(item, int):
#         list_e.append(item)
#         list_d.pop(y)
#     elif isinstance(item, str):
#         list_f.append(item)
#         list_d.pop(y)
#     y +=1
#
# print(list_d)
# print(list_e)
# print(list_f)

a = ['Samarth', 108, 'Khatri', 107, 110]
b = []
c = []
x = 0
while x < len(a):
    if isinstance(a[x],int):
        b.append(a[x])
        a.pop(x)
        x -= 1
    elif isinstance(a[x],str):
        c.append(a[x])
        a.pop(x)
        x -= 1
    x += 1

print(a)
print(b)
print(c)
