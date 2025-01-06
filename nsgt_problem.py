def remove_nsgt_once(word):
    # Define the sequence of characters to remove
    to_remove = ['n', 's', 'g', 't']
    
    # Convert the word to a list for easier manipulation
    word_list = list(word)
    
    # Initialize a flag to track which characters to remove
    remove_index = 0
    
    # Iterate over the list and remove the characters in the sequence once
    for i in range(len(word_list)):
        if word_list[i] == to_remove[remove_index]:
            word_list[i] = ''  # Remove the character
            remove_index += 1  # Move to the next character in 'n', 's', 'g', 't'
            if remove_index == len(to_remove):
                break  # Stop once all characters are removed
    
    # Join the list back to a string
    return ''.join(word_list)

# Test the function
word = "nssghtah"
result = remove_nsgt_once(word)
print(result)  # Expected output: 'niga'
