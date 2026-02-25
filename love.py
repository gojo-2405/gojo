import time

# Heart pattern with the message inside
heart = [
    "  **     **   ",
    " ****   ****  ",
    "****** ****** ",
    " ***********  ",
    "  *********   ",
    "   *******    ",
    "    *****     ",
    "     ***      ",
    "      *       "
]

message = "Karthick Loves Poojaa"

# Function to print the heart with animation
def print_heart():
    for line in heart:
        print(line)
        time.sleep(0.2)

def animate_message(msg):
    print("\n")
    for char in msg:
        print(char, end="", flush=True)
        time.sleep(0.1)
    print("\n")

# Run the program
print_heart()
animate_message(message)
print("Forever bound by love & logic ❤️")
