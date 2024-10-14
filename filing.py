import json 

students = {
    "names": {},
    "section": {}
}

def input_data():
    i = 1
    while True:
        name = input(f"Enter the name of student {i}: ")
        section = input(f"{students}'s section: ")
        
        students["names"][f'student{i} name'] = name
        students["section"][f'student{i} class'] = section

        i += 1

        chc = input("\nDo you want to add another record? Y/N: ")
        if chc.lower() in ['y', 'yes']:
            continue
        else:
            break

    # print(students)

input_data()

file = open("text.txt", 'w' )
file.write(json.dumps(students))
file.close()

file = open("text.txt", 'r' )
print(file.read())
file.close()


# ------------------------------------------------------


n = 'Y'
record = []
found = False

students = open("data.txt", 'a+')
while n == 'Y' or n == 'y':

    sname = input("enter student name: " )
    smarks = int(input("enter marks: "))
    onerecord = {'Name': sname, 'Marks': smarks}
    students.seek(0,0)
    for line in students:
        line = line.strip()
        if not line:
            continue
        temp = json.loads(line)
        if temp['Name'] == sname:
            print("Record Already Exists!")
            found = True
            break
    if found != True:
        record.append(onerecord)
        students.write(json.dumps(onerecord))
        students.write('\n')        
    n = input("Enter another record?(Y/N)")

students.close()

students = open("data.txt", 'r')
record = []
for line in students:
    line = line.strip()
    if not line:
        continue
    onerecord = json.loads(line.strip())
    print(f"{onerecord}\n")
    record.append(onerecord)

# print(record)

# sname = input("Enter Sname: ")
# smarks = int(input("ENter new marks: "))

# for i in range(len(record)):
#     if record[i]['Name']==sname:
#         record[i]['Marks']=smarks


# students = open("data.txt","w")
# students.write(json.dumps(record))
# students.close()

# students = open("data.txt","r")
# data = students.read()

# record = json.loads(data)
# print(record)