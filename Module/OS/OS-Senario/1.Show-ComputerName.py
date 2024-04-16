import os

def get_computer_name():
    computer_name = os.environ.get('COMPUTERNAME')
    if computer_name:
        print("Computer name:", computer_name)
    else:
        print("Computer name not found.")

# نمایش نام کامپیوتر
get_computer_name()
