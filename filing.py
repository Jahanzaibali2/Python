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