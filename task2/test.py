from text_processing.word_count import count_words
from text_processing.string_operations import reverse_text,to_uppercase,to_lowercase,perform_string_operations

input_text = input("Enter the text: ")

word_count = count_words(input_text)
reversed_text = reverse_text(input_text)
upper_text = to_uppercase(input_text)
lower_text = to_lowercase(input_text)
perform_string_operations(input_text)
print(f"Number of words: {word_count}")

print("Original text:", input_text)

print("Reversed text:", reversed_text)

print("Uppercase text:", upper_text)

print("Lowercase text:", lower_text)




