# log-analyzer
---
## Overview 
A beginner-friendly cybersecurity project built using Python to analyze SSH authentication logs and identify potentially suspicious login activity.
## Objectives
- Detect repeated failed login attempts.
- Identify IP addresses generating multiple authentication failures.
- Track usernames associated with failed login attempts.
<!-- Add feature to check IP with a failure after a successfull attempt - SUS AUTH PATTERN -->
## Used Tech
- Python 3
- `Collection` module
- File handling - using Python
- *Loops* and *conditinal* statements
## Project Structure
```text
log-analyzer/
|
|— log-analyzer.py
|— auth_log.txt
|— README.md
|— .gitignore
```
## Working
1. This basic python code uses *Python file reading*, *loops* and *conditionals* to read through the file, store *IP's* and *usernames* in temporary variables for *that iteration*, and then are stored in a *dictionary*.
2. Its important to store the `auth_log.txt` file in the *current working directory* of Python interpretor. The current working directory can be changed using `os` module and `os.chdir("file_path")`.
## Limitations
- Uses *fictional* SSH authentication log.
- Currently, analyzes failed attempts only.
- Uses basic threshhold detection approach.
- Does **NOT** establish if the account has been compromised or not.
--- 