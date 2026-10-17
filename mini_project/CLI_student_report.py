report = []
while True:
    print("1) Add student records(Name, ID, Marks)\n 2) View all students.\n 3) Search student by ID.\n 4) Calculate class average.")
    n = int(input("enter option number : "))
    if n==1:
        a = input("enter student name : ")
        b = int(input("enter student ID : "))
        c = int(input("enter student marks : "))
        student_details= {
            "name " : a,
            "id" : b,
            "marks" : c
        }
        report.append(student_details)
    elif n==2:
        print(report)

    elif n==3:
        d = int(input("enter student ID : "))
        for i in report:
            if i.get("id")==d:
                print(i)

    elif n==4:
        sum = 0
        for i in report:
            sum += i["marks"]
        print(sum/len(report))

    elif n==5:
        break

    else:
         print("Invalid choice.")
         
         