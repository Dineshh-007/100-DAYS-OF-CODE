# with open('my_file.txt') as file:
#     contents = file.read()
#     print(contents)   ------> To read the my_file.txt


#  ---------------------------ABSOLUTE FILE PATH---------------------------
# with open("/Users/dineshe/Desktop/WEB DEVELOPMENT/my_file.txt") as file:
#     contents = file.read()
#     print(contents)



#  ---------------------------RELATIVE FILE PATH---------------------------
with open("../../../WEB DEVELOPMENT/my_file.txt") as file:
    contents = file.read()
    print(contents)