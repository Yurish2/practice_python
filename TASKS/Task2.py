name=input("enters your name :").lower()

#if the name is correct the program will execute to second line and if it doesnot match it eill be invalid

if name=="yurish":

    date=int(input("now enter your dob:"))

    print("your date :"+str(date))

    tdate=int(input("enter todays date:")) 

    age=tdate-date

    print("your age is :"+ str (age))

    if age < 25 :

        print("time xa")

    else :

        print("time xaina")

else :

    print("invald name")