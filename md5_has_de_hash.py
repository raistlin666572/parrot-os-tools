
import hashlib



def dragon_ascii():
    # ANSI escape code for green text
    green = "\033[92m"
    reset = "\033[0m"  # Reset to default color

    art = r"""


                         .__          __  .__  .__         
           ____________  |__| _______/  |_|  | |__| ____   
           \_  __ \__  \ |  |/  ___/\   __\  | |  |/    \  
            |  | \// __ \|  |\___ \  |  | |  |_|  |   |  \ 
            |__|  (____  /__/____  > |__| |____/__|___|  / 
                       \/        \/                    \/  

                       __====-_  _-====__
                _--^^^#####//      \\#####^^^--_
             _-^##########// (    ) \\##########^-_
            -############//  |\^^/|  \\############-
          _/############//   (@::@)   \\############\_
        /#############((      \\//      ))#############\
       -###############\\     (oo)     //###############-
     -#################\\    / "" \    //#################-
    -###################\\  /  _  \  //###################-
   -#####################\\/  / \  \//#####################-
   _#/|##########/\######(   |  |   )######/\##########|\#_
   |/ |#/\#/\#/\/  \#/\##\  |  |  /##/##/\#/\#/\#/\#| \
    |/  V  V   V     V   V   |  |   V   V   V   V   V \| 
                    
    """
    
    print(green + art + reset)

if __name__ == "__main__":
    dragon_ascii()




    import hashlib

def text_to_md5(text):
    """Converts a string to its MD5 hash."""
    return hashlib.md5(text.encode()).hexdigest()

def md5_to_string(md5_hash, possible_strings):
    """Attempts to reverse and find the original string from its MD5 hash."""
    for candidate in possible_strings:
        if text_to_md5(candidate) == md5_hash:
            return candidate
    return None

def main():
    # User menu for string conversion
    print("Choose an option:")
    print("1: Convert string to MD5")
    print("2: Find original string from MD5")
    
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        # User input for string conversion
        user_input = input("Enter a string to convert to MD5: ")
        md5_hash = text_to_md5(user_input)
        print(f"MD5 Hash: {md5_hash}")

    elif choice == '2':
        # User input for MD5 hash conversion
        md5_hash = input("Enter an MD5 hash to find the original string: ")

        # Simulated possible strings for demonstration purposes
        possible_strings = ["hello", "world", "test", "data", "example"]

        # Attempt to find the original string from the MD5 hash
        found_string = md5_to_string(md5_hash, possible_strings)
        
        if found_string:
            print(f"Original string found from MD5: {found_string}")
        else:
            print("Original string not found in the list.")

    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
