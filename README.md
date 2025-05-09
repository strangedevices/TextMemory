**Replacement Trie for String Mappings**

This Python module provides a ReplacementTrie class that uses a trie data structure to store string replacement mappings and efficiently find all non-overlapping longest matches in a given text.

Some test code and directories of mappings are included

**Features**

* Insert individual string mappings from one string to another.  
* Load multiple mappings from JSON files in a specified directory.  
* Find all non-overlapping longest matches in a text based on the stored mappings.  
* Save the trie to a file and load it later using Python's pickle module.  
* Efficient matching with time complexity linear in the size of the text.

**Usage**

**Creating a New Trie**

To create a new empty trie:  
python  
trie \= ReplacementTrie()

**Inserting Mappings**

You can insert individual mappings using the insert method:  
python  
trie.insert("hello", "hi")  
trie.insert("world", "earth")

**Loading from a Directory**

To load mappings from all JSON files in a directory, use the load\_from\_directory method. Each JSON file should contain a dictionary where keys are the strings to replace, and values are the replacement strings.  
python  
trie.load\_from\_directory("/path/to/mappings")

**Note:** Ensure that the directory exists and contains valid JSON files with the correct mapping format (see Notes (\#notes) for details).

**Finding Matches in a Text**

To find all non-overlapping longest matches in a text, use the find\_matches method. It returns a list of tuples, each containing the start index, end index, matched string, and replacement string.  
python  
text \= "hello world"  
matches \= trie.find\_matches(text)  
for start, end, matched, replacement in matches:  
    print(f"Found '{matched}' at {start}:{end}, replace with '{replacement}'")

**Saving and Loading the Trie**

You can save the trie to a file and load it later:  
python  
\# Save to file  
trie.save\_to\_file("trie.pkl")

\# Load from file  
loaded\_trie \= ReplacementTrie.load\_from\_file("trie.pkl")

**Example**

Here's a simple example demonstrating the usage:  
python  
\# Create a new trie  
trie \= ReplacementTrie()

\# Insert some mappings  
trie.insert("cat", "feline")  
trie.insert("dog", "canine")  
trie.insert("bird", "avian")

\# Find matches in a text  
text \= "The cat and the dog saw a bird."  
matches \= trie.find\_matches(text)

\# Print the matches  
for start, end, matched, replacement in matches:  
    print(f"Match: '{matched}' \-\> '{replacement}' at positions {start}-{end}")

\# Output:  
\# Match: 'cat' \-\> 'feline' at positions 4-7  
\# Match: 'dog' \-\> 'canine' at positions 12-15  
\# Match: 'bird' \-\> 'avian' at positions 20-24

**Notes**

* **Case Sensitivity:** The trie is case-sensitive; mappings for "Hello" and "hello" are treated as distinct.  
* **Matching Behavior:** The find\_matches method finds the longest possible match starting at each position in the text and ensures that matches do not overlap, processing the text from left to right.  
* **JSON File Format:** JSON files for loading mappings should contain dictionaries with string keys and string values, e.g.:  
* json

{  
    "hello": "hi",  
    "world": "earth",  
    "foo": "bar"

* }  
* **Duplicate Keys:** If there are duplicate keys across different JSON files, the mapping from the last file loaded will be used, as later insertions overwrite earlier ones.  
* **Empty Strings:** The trie does not support mappings for empty strings. Attempting to insert a mapping with an empty from\_str may lead to undefined behavior.  
* **Pickle Usage:** The trie is saved and loaded using Python's pickle module. Pickle files are specific to Python and may not be compatible across different Python versions. **Warning:** Only load pickle files from trusted sources, as they can execute arbitrary code.

**Requirements**

* Python 3.x  
* Standard library modules: json, os, pickle# TextMemory

