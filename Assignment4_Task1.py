
try:
    with open('sample.txt','r') as file:
        read_file = file.read()
        print(read_file)

except FileNotFoundError:
    print("The file 'sample.txt' was not found")
