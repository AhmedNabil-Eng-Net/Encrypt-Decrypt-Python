# 🔐 Encrypt & Decrypt in Python

A command-line encryption tool built with Python using a simple substitution-based encryption system.

## ✨ Features

* 🔐 Encrypt text using a randomly generated key
* 🔓 Decrypt text using the matching key
* 🔑 View the current encryption key
* 💾 Save the current key to a file
* 📂 Load and validate a saved key
* 🔄 Generate a new random key
* ⚠️ Handle unsupported characters
* 🎨 Colored command-line output

## 🛠️ Technologies

* Python
* `string` module
* `random` module
* `os` module
* `time` module
* `colorama`

## 📦 Installation

Install the required external package:

```bash
pip install colorama
```

## 🚀 How to Run

Run the program with:

```bash
main.py
```

> Replace `main.py` with your actual Python file name if it is different.

## 🎮 How to Use

When the application starts, a random encryption key is generated automatically.

Choose an option from the menu:

```text
1. Encrypt a text 🔐
2. Decrypt a text 🔓
3. Show key 🔑
4. Save key 💾
5. Load key 📂
6. Generate New Key 🔄
7. Exit 🚪
```

### 🔐 Encrypt Text

Enter the text you want to encrypt:

```text
💬 Enter a text to encrypt: Hello Python
```

The program uses the current key to replace each supported character with its mapped character.

### 🔓 Decrypt Text

Use the matching key to restore the original text:

```text
💬 Enter a text to decrypt: ...
```

### 💾 Save & 📂 Load Key

A generated key can be saved to a file and loaded later.

This allows encrypted text to be decrypted again after restarting the program, as long as the correct key is available.

## 🔑 How the Encryption Works

The program creates a shuffled copy of the supported characters.

For example:

```text
Original → Shuffled

A → q
B → 7
C → $
D → x
```

An encryption dictionary maps each original character to its encrypted character:

```python
encryption_key = dict(zip(chars, keys))
```

A reverse dictionary is used for decryption:

```python
decryption_key = dict(zip(keys, chars))
```

## 📚 What I Practiced

This project helped me practice:

* Functions and parameters
* Dictionaries
* `zip()`
* `.copy()`
* `.shuffle()`
* `.index()`
* Lists and strings
* File handling
* Exception handling
* Input validation
* Key generation and management
* Working with external Python packages

## ⚠️ Note

This project uses a simple substitution-based cipher for **learning and experimentation**. It is not intended to provide modern, secure encryption for protecting sensitive information.

## 👨‍💻 Author

**Ahmed Nabil**
