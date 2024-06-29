def calculate_flames(name1, name2):
    
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")

    
    char_count = {}

    
    for char in name1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    
    for char in name2:
        if char in char_count:
            char_count[char] -= 1
        else:
            char_count[char] = -1

    
    remaining_chars = sum(abs(count) for count in char_count.values())


    categories = ["Friendship", "Love", "Affection", "Marriage", "Enemy", "Sibling"]

    
    count = 0
    while len(categories) > 1:
        count = (count + remaining_chars - 1) % len(categories)
        categories.pop(count)

  
    return categories[0]


def flames_game():
    print("Welcome to Flames Game!")
    print("Enter two names to find out the relationship between them.")

    name1 = input("Enter the first name: ")
    name2 = input("Enter the second name: ")

    relationship = calculate_flames(name1, name2)

    print(f"The relationship between {name1} and {name2} is: {relationship}")


if __name__ == "__main__":
    flames_game()
