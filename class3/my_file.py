try:
    My_file = open("C:\\Users\\yarinf\\Desktop\\TEST\\DevOps.txt", 'r+')
    content = My_file.read()
    # My_file.write("inserted text")
    My_file.close()
    print(content)
    c = 5
except IOError:
    print('could not open file')
finally:
    print(123)

