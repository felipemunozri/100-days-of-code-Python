# # My code
# names_list = []
#
# with open("./input/Names/invited_names.txt") as invited_names:
#     for name in invited_names:
#         names_list.append(name.replace("\n", ""))  # remove end of line characters
#
# for name in names_list:
#     with open("./input/Letters/starting_letter.txt", mode="r") as starting_letter:
#         original_content = starting_letter.read()
#         new_content = original_content.replace("Dear", f"Dear {name}")
#         with open(f"output/ready_to_send/letter_for_{name.lower()}.txt", mode="w") as file:
#             file.write(new_content)

# Answer
PLACEHOLDER = "[name]"
with open("./input/Names/invited_names.txt") as names_list:
    names = names_list.read()

with open("./input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./output/ready_to_send/letter_for_{name}.txt", "w") as completed_letter:
            completed_letter.write(new_letter)
