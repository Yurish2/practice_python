
info ={

    "name" :"hari",
    "age" : "32",
    "sub" : ["math" ,"eng" ,"nep"],
    "class" : (11,22, 33, 75),
    "is_nothero" : True ,
    20 : "correct"
}

#prints only the keys
# print(info.keys())

#prints only values
# print(info.values())

#prints the values and keys in tupple 

# print(list(info.items())) #type casting( tuples into list)

# print(info["name2"]) #gives error
# print(info.get("name 2")) #doesnot give error -> gives none

new_dict ={"name" :"shyam" , "address":"pokhara"}
info.update(new_dict)

print(info)