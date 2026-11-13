# log-analyzer
---
## Aim: 
Learn how security analysts investigate authentication logs to identify suspicious login activity, repeated failed login attempts, and potentially compromised accounts from a *fictional* log file.
## Pre-requisites
- Basic Python knowledge
- Basic log-authentication knowledge
- Code editor + Python installed on your computer
## Working
1. This basic python code uses *Python file reading*, *loops* and *conditionals* to read through the file, store *IP's* and *usernames* in temporary variables for *that iteration*, and then are stored in a *list*.
2. Its important to store the `auth_log.txt` file in the *current working directory* of Python interpretor. The current working directory can be changed using `os` module and `os.chwd("file_path")`.
--- 