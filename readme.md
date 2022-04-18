# Overview
This app consist of one main class - Password from Security package  
The main functionality is to check the password for security and generate secure passwords,  
represented by the two methods of this class - `generate` and `check`.

## Requirements
- python 3.8 or higher

## Installation
- Just clone this repo from github via command  
`git clone https://github.com/Fan4ik20/password_manager.git`
- Or via pip  
`pip install -i https://test.pypi.org/simple/ password-manager==1.0`

## Usage
You can use main functionality in two ways:
- Via CLI:
  - 2 cli commands:
    - python password.py --check `your password`  
    - python password --generate `length` (minimum 14)
- Directly in your code
  - example:  
    `# If you install from git.`  
    `from security.security import Password`  
    `# If you install via pip.`  
    `from password_manager.security.security import Password`  
    `# For generating.`  
    `print(Password.generate(14))  # returns a new secure password.`  
    `# For сhecking.`  
    `# Additional method returns bool value.`  
    `# True - if password is secure and False if non secure`     
    `Password.check('your_password')`

## License
MDI.

## Links
https://test.pypi.org/project/password-manager/1.0/  