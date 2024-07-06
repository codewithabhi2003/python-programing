def addmission():
    course = input("which course you want to enroll ")
    if course == "bsc.it":
        percentage = int(input("what is your 12th percentage? : "))
        subject = input("what subject do you have? : ")
        if subject == "maths" and percentage >= 50:
            print("you are enrolled in bsc.it")
        else:
            print("you are not eligible for bsc.it")
    else:
        print("sorry we don't offer that course")


addmission()