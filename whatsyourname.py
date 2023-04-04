# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    # Write your code here
    print(__name__)
    print("Hello " + first + " " + last + "! You just delved into python.")

if __name__ == '__main__':
    first_name = input("Input first name: ")
    last_name = input("Input last name: ")
    print_full_name(first_name, last_name)
    print_full_name("Ross", "Taylor")
    
    #Comment
    