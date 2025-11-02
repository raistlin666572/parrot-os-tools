




def dragon_ascii():
    # ANSI escape code for blue text
    blue = "\033[94m"
    reset = "\033[0m"  # Reset to default color

    art = r"""


                        _____|  | _____.__.
                       /  ___/  |/ <   |  |
                       \___ \|    < \___  |
                      /____  >__|_ \/ ____|
                       \/     \/\/     

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
    
    print(blue + art + reset)

if __name__ == "__main__":
    dragon_ascii()




def decimal_to_binary():
    """Convert a decimal number input to binary."""
    while True:
        decimal = input("What is the decimal number? ")
        try:
            # Convert the input to an integer
            decimal_input = int(decimal)

            # Check if the number is non-negative
            if decimal_input < 0:
                print("Please enter a non-negative integer.")
                continue







            
            binary_output = bin(decimal_input)[2:]
            return binary_output  # Return the binary representation
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def user_binary_input():
    """Prompt the user for binary input, convert it to decimal, and return it."""
    while True:
        user_binar = input("What is the binary input? ")
        try:
            # Convert the binary string to an integer (decimal)
            binary_integer = int(user_binar, 2)
            return binary_integer  # Return the decimal 
        except ValueError:
            print("Invalid input. Please enter a valid binary number.")









            # Main logic outside of a function
while True:
    user = input("Choose conversion: a = decimal to binary, b = binary to decimal, or q = quit: ")

    if user == "b":
        decimal_result = user_binary_input()
        print(f"{decimal_result} is the decimal number.")
    elif user == "a":
        binary_result = decimal_to_binary()
        print(f"{binary_result} is the binary number.")
    elif user.lower() == "q":  # Allow user to quit with 'q'
        print("Exiting the program.")
        break
    else:
        print("Invalid option. Please choose 'a', 'b', or 'q'.")



        
def display_ip_classes():
    """Display the characteristics of IP address classes A, B, and C."""
    
    # Create a comparison table
    ip_classes = [
        {
            "Aspect": "Leading Bits",
            "Class A": "0xxxxxxx",
            "Class B": "10xxxxxx",
            "Class C": "110xxxxx"
        },
        {
            "Aspect": "First Octet Range",
            "Class A": "1 to 126",
            "Class B": "128 to 191",
            "Class C": "192 to 223"
        },
        {
            "Aspect": "Default Subnet Mask",
            "Class A": "255.0.0.0 (or /8)",
            "Class B": "255.255.0.0 (or /16)",
            "Class C": "255.255.255.0 (or /24)"
        },
        {
            "Aspect": "Number of Networks",
            "Class A": "128 (0-127, with reserved ranges)",
            "Class B": "16,384 (128-191)",
            "Class C": "2,097,152 (192-223)"
        },
        {
            "Aspect": "Hosts per Network",
            "Class A": "16,777,214",
            "Class B": "65,534",
            "Class C": "254"
        },
        {
            "Aspect": "Use Case",
            "Class A": "Very large networks (e.g., ISPs, large corporations)",
            "Class B": "Medium-sized networks (e.g., universities, large companies)",
            "Class C": "Small networks (e.g., small businesses, home networks)"
        }
    ]
    
    # Print the table in a formatted way
    for entry in ip_classes:
        print(f"{entry['Aspect']:30} | {entry['Class A']:30} | {entry['Class B']:30} | {entry['Class C']:30}")
        print('-' * 130)  # Separator line

# Main logic with user input
if __name__ == "__main__":
    while True:
        user_input = input("Would you like to know about IP classes? (y/n): ").strip().lower()
        if user_input == 'y':
            display_ip_classes()
        elif user_input == 'n':
            print("Exiting the program.")
            break
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")








def ip_to_hex(ip_address):
    """Convert an IPv4 address to its hexadecimal representation."""
    try:
        # Split the IP address into octets
        octets = ip_address.split('.')
        
        # Check if the IP address has exactly 4 octets
        if len(octets) != 4:
            return "Invalid IP address format."
        
        # Convert each octet to hexadecimal
        hex_octets = [format(int(octet), '02X') for octet in octets]
        
        # Combine hex octets into a single string separated by dots
        hex_ip = '.'.join(hex_octets)
        
        return hex_ip
    except ValueError:
        return "Invalid IP address"

def hex_to_ip(hex_address):
    """Convert a hexadecimal IP address back to its decimal format."""
    try:
        # Split the hexadecimal address into octets
        hex_octets = hex_address.split('.')
        
        # Convert each hex octet to decimal
        decimal_octets = [str(int(octet, 16)) for octet in hex_octets]
        
        # Combine decimal octets into a single string
        decimal_ip = '.'.join(decimal_octets)
        
        return decimal_ip
    except ValueError:
        return "Invalid hexadecimal address"

if __name__ == "__main__":
    while True:
        # Ask the user for the conversion type
        conversion_option = input("Type '1' to convert IP to Hex, '2' for Hex to IP, or 'exit' to quit: ")
        
        if conversion_option.lower() == 'exit':
            print("Exiting the program.")
            break

        if conversion_option == '1':
            user_ip = input("Enter an IPv4 address: ")
            hex_result = ip_to_hex(user_ip)
            print(f"The hexadecimal representation of {user_ip} is: {hex_result}")
        
        elif conversion_option == '2':
            user_hex = input("Enter a hexadecimal IP address: ")
            decimal_result = hex_to_ip(user_hex)
            print(f"The decimal representation of {user_hex} is: {decimal_result}")
        
        else:
            print("Invalid option. Please choose '1', '2', or 'exit'.")


