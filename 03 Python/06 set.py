s = set()

s.add(1)  # s.append(1)
s.add(1)
s.add(2)
s.add(3)
s.add(4)

print(f"Set is {s}")

s.remove(2)
print(f"Set is {s}, after remove")
print(f"2 is in {2 in s}")
print(f"3 is in {3 in s}")