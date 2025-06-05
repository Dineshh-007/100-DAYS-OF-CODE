# numbers = [1,2,3]
# new_numbers = [n + 1 for n in numbers]
# print(new_numbers)

# Output: [2,3,4]

# ------------------------  LIST COMPREHENSION ---------------------------------
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_names = [name for name in names if len(name) < 5]
# print(short_names)
# long_names = [name.upper() for name in names if len(name) > 5]
# print(long_names)   #All names will be in uppercase

# list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
# numbers = [int(n) for n in list_of_strings]
# result = [r for r in numbers if r%2 == 0]
# print(result)   #Even numbers will be printed

#----------------------------  DICTIONARY COMPREHENSION -------------------------

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# import random
# students = {student : random.randint(1,100) for student in names}
# print(students)
# passed_students={student:marks for (student , marks) in students.items() if marks > 30}
# print(passed_students)
#
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = sentence.split()
# print(result)

# weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
#
# weather_f = { day : (c *9/5)+32 for (day,c) in weather_c.items()}
#
# print(weather_f)