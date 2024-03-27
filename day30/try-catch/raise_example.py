height = float(input("Height (m): "))
weight = int(input("Weight (Kg): "))

# if user inputs a height too big it will be calculated OK and no error would appear, but it is illogical, so we raise
# our own exception, and for that we use the ValueError clause
if height > 3:
    raise ValueError("Human height should not be over 3 meters.")
else:
    bmi = weight / height ** 2
    print(bmi)
