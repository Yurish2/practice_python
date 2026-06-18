#nested dictionary

Student ={

    "name" : "superman",
    "subject" :{
        "math" : 0,
        "science" : 90,
        "eng" : 0,
    }

}

#to print every keys in dictionary
# print(Student)

#to print specific key

# print(Student["subject"])

#to print from the nested dict

print(Student["subject"]["math"])