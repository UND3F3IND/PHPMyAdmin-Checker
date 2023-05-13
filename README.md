┊ 𝗣𝗵𝗽𝗠𝘆𝗔𝗱𝗺𝗶𝗻 𝗟𝗼𝗴𝗶𝗻 𝗖𝗿𝗲𝗱𝗲𝗻𝘁𝗶𝗮𝗹 𝗩𝗮𝗹𝗶𝗱𝗮𝘁𝗼𝗿 ┊

The phpMyAdmin Login Credential Validator is a Python script that validates login credentials for phpMyAdmin. It reads a file containing phpMyAdmin login credentials in a specific format, checks the validity of each credential, and writes the valid credentials to an output file.

【Prerequisites】

•Python 3.x

•Requests library (pip install requests)

【Usage】

1-Ensure that your input file follows the required format: HOST/phpmyadmin/|USER|PASS, where HOST represents the URL of the phpMyAdmin login page, and |USER| and |PASS| represent placeholders for the username and password, respectively.

2-Run the script by executing the following command:

✎﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏ @cmd: python phpmyadmin_validator.py


3-Follow the prompts to provide the paths to the input file and output file.

4-The script will process the input file, validate the login credentials, and write the valid credentials to the output file.


【Example Input File】

An example input file (input.txt) may look like this:

https://example.com/phpmyadmin/|user1|password1

https://example.com/phpmyadmin/|user2|password2

https://example.com/phpmyadmin/|user3|password3


【Example Output File】

After running the script, the valid credentials will be written to the output file (output.txt). The output file will contain the following lines:

https://example.com/phpmyadmin/|user1|password1

https://example.com/phpmyadmin/|user3|password3

【Acknowledgements】

This script utilizes the Requests library for making HTTP requests. For more information about the library, visit Requests Documentation.
