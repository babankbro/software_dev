# define the list
names = ["Harry", "Sarayut", "Mr. B", "Mr. A"]
print("#3 List", names)
print("#4 Item", names[1])

names.sort()
print("#7 Sorted List", names)

names.sort(reverse=True)
print("#10 Reverse Sorted List", names)

names.append("XXX") #add  , set remove list pop
print("#13 List", names)
