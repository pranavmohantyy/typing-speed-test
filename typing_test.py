import time
import json

with open('texts.json') as f:
    texts = json.load(f)

print("Select difficulty level:")
print("1. Easy\n2. Medium\n3. Hard")
difficulty = input("Enter the number of your choice: ")

if difficulty == '1':
    paragraph = texts['easy'][0]
elif difficulty == '2':
    paragraph = texts['medium'][0]
elif difficulty == '3':
    paragraph = texts['hard'][0]
else:
    print("Invalid choice. Defaulting to easy.")
    paragraph = texts['easy'][0]

print(paragraph)

print("Select time mode:")
print("1. 30 seconds\n2. 1 minute\n3. 2 minutes")
time_mode = input("Enter the number of your choice: ")

if time_mode == '1':
    time_limit = 30
elif time_mode == '2':
    time_limit = 60
elif time_mode == '3':
    time_limit = 120
else:
    print("Invalid choice. Defaulting to 30 seconds.")
    time_limit = 30

input("Press Enter to start typing...")
start_time = time.time()
user_input = input("Type the paragraph above:")

...