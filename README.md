# Project-24
NATO Alphabet Converter
# NATO Phonetic Alphabet Converter 📻

A Python program that converts any word into its NATO phonetic alphabet equivalent. Enter a word and get the corresponding code words used in aviation and military communications.

## Requirements

```bash
pip install pandas
```

## Project Structure
nato-alphabet/
│
├── main.py
└── nato_phonetic_alphabet.csv

## CSV File Format

`nato_phonetic_alphabet.csv`:
```csv
letter,code
A,Alfa
B,Bravo
C,Charlie
D,Delta
E,Echo
F,Foxtrot
G,Golf
H,Hotel
I,India
J,Juliett
K,Kilo
L,Lima
M,Mike
N,November
O,Oscar
P,Papa
Q,Quebec
R,Romeo
S,Sierra
T,Tango
U,Uniform
V,Victor
W,Whiskey
X,X-ray
Y,Yankee
Z,Zulu
```

## How to Run

```bash
python main.py
```

## How It Works

1. Loads NATO phonetic alphabet from CSV file
2. Creates a dictionary mapping each letter to its code word
3. Prompts user to enter a word
4. Converts each letter to its NATO phonetic equivalent
5. Displays the result as a list
6. Loops continuously until program is closed

## Example Usage
Enter a word: HELLO
['Hotel', 'Echo', 'Lima', 'Lima', 'Oscar']
Enter a word: Python
['Papa', 'Yankee', 'Tango', 'Hotel', 'Oscar', 'November']
Enter a word: SOS
['Sierra', 'Oscar', 'Sierra']
Enter a word: 123
Invalid input.
Enter a word: ABC!
Invalid input.
Enter a word:

## Features

✅ **Case-insensitive** - Accepts lowercase or uppercase input  
✅ **Input validation** - Only accepts alphabetic characters  
✅ **Dictionary comprehension** - Efficient data structure creation  
✅ **List comprehension** - Clean conversion logic  
✅ **Pandas integration** - CSV data handling  
✅ **Continuous loop** - Convert multiple words without restarting  

## Code Breakdown

### Creating the Dictionary
```python
# Uses dictionary comprehension with pandas iterrows()
alpha_dict = {row.letter:row.code for (index, row) in df.iterrows()}
# Result: {'A': 'Alfa', 'B': 'Bravo', ...}
```

### Converting the Word
```python
# Uses list comprehension to map each letter
new_word = [alpha_dict[letter] for letter in user_word]
```

### Input Validation
```python
if user_word.isalpha():  # Only letters allowed
    # Process word
else:
    print("Invalid input.")
```

## What the NATO Phonetic Alphabet Is

The NATO phonetic alphabet is the most widely used spelling alphabet, designed to:
- **Avoid confusion** between similar-sounding letters
- **Ensure clarity** in radio and telephone communications
- **Standardize** verbal communication internationally

### Common Uses:
- Aviation communications
- Military operations
- Emergency services
- Customer service (spelling names, confirmation codes)
- Ham radio operators

## Customization

### Different Output Format
```python
# Print on separate lines
for code in new_word:
    print(code)

# Print as string
print(" ".join(new_word))
# Output: Hotel Echo Lima Lima Oscar
```

### Add Exit Option
```python
while converting:
    user_word = input("Enter a word (or 'quit' to exit): ").upper()
    if user_word == "QUIT":
        break
    if user_word.isalpha():
        new_word = [alpha_dict[letter] for letter in user_word]
        print(new_word)
    else:
        print("Invalid input.")
```

### Save Results to File
```python
with open("output.txt", "a") as file:
    file.write(f"{user_word}: {new_word}\n")
```

## Error Handling

| Input | Result |
|-------|--------|
| **"HELLO"** | ✅ `['Hotel', 'Echo', 'Lima', 'Lima', 'Oscar']` |
| **"hello"** | ✅ `['Hotel', 'Echo', 'Lima', 'Lima', 'Oscar']` (auto-uppercase) |
| **"123"** | ❌ "Invalid input." (numbers not allowed) |
| **"ABC!"** | ❌ "Invalid input." (special characters not allowed) |
| **"A B C"** | ❌ "Invalid input." (spaces not allowed) |

## What I Learned

- **Pandas basics** - Reading CSV files with `pandas.read_csv()`
- **DataFrame iteration** - Using `.iterrows()` to loop through rows
- **Dictionary comprehension** - Creating dictionaries in one line
- **List comprehension** - Transforming data efficiently
- **String methods** - `.upper()` for case normalization, `.isalpha()` for validation
- **Data structure mapping** - Creating lookup dictionaries from CSV data
- **Input validation** - Checking input before processing
- **Infinite loops** - Using `while True` with validation

This project demonstrated practical data processing and user interaction patterns.

## Real-World Applications

- **Customer service tools** - Spelling names and confirmation codes clearly
- **Aviation training apps** - Learning phonetic alphabet
- **Emergency dispatch systems** - Clear communication protocols
- **Radio communication simulators** - Practice standard phraseology

Perfect for anyone needing to spell words clearly over the phone! ☎️
