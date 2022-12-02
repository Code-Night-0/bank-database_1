with open('C:\\Users\\saris\\Desktop\\all_users.csv', 'r') as open_file:   #kapatma işlemine gerek yok bu modda açmak daha mantıklı.
    #open_file.write('A string to write')
    print(open_file.readlines())
