# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1, "done":1}

def read_file_content(filename):
    # here I am trying to open the file.
    with open(filename) as f:
        # once the file is opened I want to read from the file and store the strings in a variable called contents
        contents = f.read()
        # here I am trying to convert the strings to a list
        contents = contents.split(" ")
        # I am returning the list to be used in another function
        return contents


def count_words(path):
    # here i am calling the function that read the file and storing the list as a variable called text
    text = read_file_content(path)
    # I am creating an empty dictionary to hold the text and the amount of time the appeared. For now it is empty
    bag = {}
    # Now I am looping the text and storing each of them as value
    for value in text:
        # if the value has a length greater than 0. that is the value has a content not just an empty string
        if(len(value)) != 0:
            # Here I want to remove spaces around the value
            value = value.strip()
            # I want to remove some special characters around the value
            value = value.strip("?\n.,")
            # here I am checking if my dictionary contains a key called value
            if value in bag.keys():
                # if yes I will increase the value of the dictionary key by 1
                bag[value] += 1
            else:
                # if no I will create the key in the dictionary with a value of 1
                bag[value] = 1

    # i am returing the dictionary of bag
    return(bag)


# here I am calling the function count_words which will call the function read_file_content and passing the file it should read
print(count_words("./story.txt"))
