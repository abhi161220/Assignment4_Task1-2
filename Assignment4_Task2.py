
data = input("Enter text to write to the file: ")

with open("output.txt", "w") as file:
    written_file = file.write(data+"\n")
    print("Data successfully written to output.txt\n")

new_data = input("Enter additional text to append: ")
with open("output.txt", "a") as file:
    append_file = file.write(new_data)
    print("Data successfully appended.\n")

with open("output.txt", "r") as file:
    reading = file.read()
    print("Final content of output.txt:")
    print(reading)





