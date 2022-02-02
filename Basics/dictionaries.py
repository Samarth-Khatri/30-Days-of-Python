#Dictionaries and Tuples

a_dict = {"abc": "A string"}
print(a_dict)

a_dict = {"abc": "A string", "xyz": "Another sring"}
print(a_dict)

a_dict["abc"] = "A new string"
print(a_dict)

print(a_dict["xyz"])

abc = {0: "first"}
abc[1] = "second"
print(abc)


tup = ()
tup = ("xyz", "xyz")

print(tup)

new_tup = (("abc xyz", "123") , ("hello"))
print(new_tup)
print(new_tup[0])
print(new_tup[0][0])
print(new_tup[0][0][0])

new_tup += (("another", "456"),) #Adiing new tupple
print(new_tup)
