import time

paragraph = "The quick brown fox jumps over the lazy dog."
print(paragraph)

input("Press Enter to start typing...")
start_time = time.time()
user_input = input("Type the paragraph above:")
elapsed_time = time.time() - start_time

words = len(user_input.split())
wpm = (words / (elapsed_time / 60)) if elapsed_time > 0 else 0

# Calculate accuracy
expected_chars = len(paragraph)
typed_chars = len(user_input)
errors = sum(1 for i, c in enumerate(paragraph) if i < typed_chars and c != user_input[i])
accuracy = (1 - errors / expected_chars) * 100 if expected_chars > 0 else 0

print(f"Your WPM: {wpm:.2f}")
print(f"Your accuracy: {accuracy:.2f}%")