# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    
    file = open(filename, 'r')
    read_file = file.read()
    print(read_file)
    return read_file
    
    


def count_words():
    # print("COUNT WORDS")

    # [assignment] Add your code here
    text = read_file_content("story.txt")

    # replacing new lines with empty space
    text = text.replace('\n', ' ')
    # converting the result of text to lowercase and also coverting result into a list
    split_text = text.lower().split(' ')
    # intialise an empty dictionary to get the unique words
    unique_words = {}

    # for loop to loop the data of our list(split_text)
    for i in split_text:
        # checking if the doesn't already exist in our unique_words dictionary
        if not i in unique_words.keys():
            # making sure there are no empty strings, if not, add to unique_words
            if not i.strip():
                # if empty string is found, skip
                continue
            #adding our unique words as keys in the dictionary while also adding the first count as the value of the word as the key
            unique_words[i] = 1            
        else:
            # else if word has already been found in the split_text list, increase the count
            unique_words[i] += 1

    print(unique_words)
    return unique_words
    
read_file_content('story.txt')
count_words()
