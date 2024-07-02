def generate_greeting(first_name, last_name):
    return F"Hello, {first_name} {last_name}! Welcome."

def main():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    
    greeting_message = generate_greeting(first_name, last_name)
    print(greeting_message)

if __name__ == "__main__":
    main()
