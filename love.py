import time
import random
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

message = "Karthick Loves Poojaa"
colors = [Fore.RED, Fore.MAGENTA, Fore.CYAN, Fore.YELLOW, Fore.GREEN, Fore.BLUE]

def sparkle_text(text):
    for char in text:
        color = random.choice(colors)
        print(color + char, end="", flush=True)
        time.sleep(0.1)
    print(Style.RESET_ALL)

def sparkle_animation(text, repeat=3):
    for _ in range(repeat):
        sparkle_text(text)
        time.sleep(0.5)

# Run the animation
print("\n✨ Sparkling Message ✨\n")
sparkle_animation(message)

print("\nLove shines brighter than code... 💖")
