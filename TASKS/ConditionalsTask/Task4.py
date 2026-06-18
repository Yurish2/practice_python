name=input("enter your name :").lower()

if name=="yurish":

    date=int(input("Please enter your date of birth :"))

    Cdate=int(input("enter the current year :"))

    age=(Cdate-date)+10

    print("your after 10 year is"+ str(age)) 



else:
    print("invalid name")
        