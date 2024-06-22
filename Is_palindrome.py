def is_palindrome(s):
    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()
    # Check if the string is equal to its reverse
    return s == s[::-1]

def main():
    print("Welcome to Palindrome Checker!")
    while True:
        user_input = input("Enter a string to check for palindrome (or 'exit' to quit): ")
        
        if user_input.lower() == 'exit':
            break
        
        if is_palindrome(user_input):
            print(f"'{user_input}' is a palindrome!")
        else:
            print(f"'{user_input}' is not a palindrome.")

if __name__ == "__main__":
    main()
