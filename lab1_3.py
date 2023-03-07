
studentName = input("Enter your name.\n")
lab = int(input("Enter your Lab Score\n"))
midterm = int(input("Enter your Midterm result.\n"))
final = int(input("Enter your Final result.\n"))

print("Name: " + studentName)
print("\nLab:", lab)
print("\nMidterm:", midterm)
print("\nFinal:", final)
print("\nLast Score:", ((lab / 4) + (midterm * 35 / 100) + (final * 4 / 10)))
