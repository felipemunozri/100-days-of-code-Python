# we can define data types for variables using the syntax var_name: datatype
# age: int
# name: str
# height: float
# is_human: bool


# we can also define the data type that a function returns using the -> datatype sintax
def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False


if police_check(19):
    print("You may pass.")
else:
    print("Pay a fine.")
    