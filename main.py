from user import User

with open('C:\\Users\\saris\\Desktop\\all_users.csv', 'r') as open_file:   #kapatma işlemine gerek yok bu modda açmak daha mantıklı.
    try:
        current_id = int(input('enter your id here : '))
        for line in open_file:
            if str(current_id) in line.split(",")[0]:
                name = line.split(",")[1]
                print(f"Welcome, {name}") 
                user = User(line.split(",")[0], line.split(",")[1], line.split(",")[2], line.split(",")[3], line.split(",")[4], line.split(",")[5])

            else:
                print(f"Sorry, {current_id} ID does not exist")
    except ValueError:
            print('invalid id')

current_password = input(f'Enter your password {name} : ')
if user.password == current_password:
    print(f'{name} password is correct')
else:
    print(f'{name} password is incorrect')




