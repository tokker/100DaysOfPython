with open("Input/Letters/starting_letter.txt") as starting_file:
    starting_letter = starting_file.read()

with open("Input/Names/invited_names.txt") as names_file:
    names = names_file.read().splitlines()

for name in names:
    letter_with_name = starting_letter.replace("[name]", name)
    with open(f"letter_for_{name}.txt", "w") as output_file:
        output_file.write(letter_with_name)

