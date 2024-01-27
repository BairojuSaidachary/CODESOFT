# Password Generator and Strength Checker

This Python script provides a simple yet customizable password generator and strength checker. Users can specify the desired length of the password and choose which character types to include (uppercase letters, lowercase letters, digits, and/or special characters). The script then generates a password based on the user's preferences and evaluates its strength.

## How to Use

1. Run the script in a Python environment.
2. Enter the desired length of the password when prompted.
3. Answer "y" or "n" for each character type to include or exclude.
4. The script will then generate a password and display it along with its strength.

## Script Details

### `generate_password` Function

```python
def generate_password(
    length,
    include_uppercase=True,
    include_lowercase=True,
    include_digits=True,
    include_special=True,
):
```
- This function generates a password based on the specified length and character types.


## `check_strength` Function
```python
def check_strength(
    password, include_uppercase, include_lowercase, include_digits, include_special
):

    return strength
```
- This function checks the strength of the generated password based on included character types.
 ## Running the Script
```python
if __name__ == "__main__":
    main()
```

- The main() function prompts the user for input, generates a password, and displays its strength.

<p style=text-align:center>©️ Developed by <strong>@BairojuSaidachary</strong></p>