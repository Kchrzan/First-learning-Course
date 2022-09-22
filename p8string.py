name = "Daniel"
name1 = "aDaniela"
name2 = "     Daniel      "
# print(len(name))
# print(name.capitalize())
# print(name.upper())
# print(name.lower())

print(name[0:]) # wyświetla litere przypisaną dop indeksu, zaczynamy od 0

channel = "jak nauczyć się programowania"

print(channel.split(" "))

join_string = "-"
print(join_string.join(['jak', 'nauczyć', 'się', 'programowania']))

print(name.startswith("D"))
print(name.startswith("d"))

print(name.endswith("L"))
print(name.endswith("l"))

print(name.rstrip("l"))
print(name.lstrip("D"))

print(name1.strip("a"))

print(name2)
print(name2.strip())

first_name = "Daniel"
last_name = "Ziemba"

print(first_name + " " + last_name)

join_string = " "
print(join_string.join([first_name, last_name]))

james_bond = 7
print(str(james_bond).zfill(3))