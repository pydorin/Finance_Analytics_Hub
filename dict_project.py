import matplotlib.pyplot as plt

available_parts = {
    "1": "computer",
    "2": "monitor",
    "3": "keyboard",
    "4": "mouse",
    "5": "hdmi cable",
    "6": "dvd drive",
}

current_choice = None
computer_parts = {}  # create an empty dict

while current_choice != "0":
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        if current_choice in computer_parts:
            print(f"Removing {chosen_part}")
            computer_parts.pop(current_choice)
        else:
            print(f"Adding {chosen_part}")
            computer_parts[current_choice] = chosen_part
        print(f"Your dictionary contains: {computer_parts}")
    else:
        if current_choice != "0":
            print("Please choose from the list")
            for key, value in available_parts.items():
                print(f"{key}: {value}")
            print("0: to finish")

    current_choice = input("> ")

# Creating the bar chart
parts_count = {part: list(computer_parts.values()).count(part) for part in available_parts.values()}
plt.bar(parts_count.keys(), parts_count.values())
plt.xlabel('Computer Parts')
plt.ylabel('Frequency')
plt.title('Frequency of Computer Parts Chosen')
plt.show()
