# SecurePassAnalyzer
# 🔐 SecurePassAnalyzer – Password Strength Analyzer & Wordlist Generator

---

## 1. Introduction

With the increasing risk of cyberattacks and password breaches, understanding password strength and the risks of predictable passwords is more important than ever. This project introduces a user-friendly tool that analyzes password strength and generates targeted wordlists based on personal information, mimicking the tactics used by attackers. It helps users visualize how vulnerable their passwords might be and encourages the adoption of stronger, more secure credentials.

---

## 2. Abstract

The project focuses on enhancing password awareness and demonstrating how weak or predictable passwords can be exploited using personal data. Built using Python, this tool combines a graphical interface with advanced analysis from the `zxcvbn` library. It also offers a feature to generate custom wordlists based on user input like names, dates, or pets. These wordlists simulate real-world attack vectors. By providing instant feedback on password strength and visualizing the risks of reused or predictable patterns, the tool aims to educate users while being a practical resource for security testing.

---

## 3. Tools Used

1. **Python 3.11** – Used as the core programming language due to its simplicity and support for GUI and data processing.

2. **Tkinter and ttk** – Employed for building the graphical user interface. Tkinter provides the framework, while ttk improves the visual appearance with styled widgets.

3. **zxcvbn** – A password strength estimation library that analyzes passwords using realistic metrics, such as guessability and crack time.

4. **argparse** – Used optionally to enable command-line interface functionality for non-GUI use cases.

5. **NLTK (Natural Language Toolkit)** – Considered for enhancing wordlist generation through basic natural language processing.

6. **Visual Studio Code (VS Code)** – Used as the primary development environment, offering useful extensions and debugging capabilities.

---

## 4. Steps Involved in Building the Project

- **Step 1:** Set up a Python virtual environment and install dependencies like `zxcvbn`, `tkinter`, and optionally `nltk`.
- **Step 2:** Create a CLI and GUI interface using `argparse` and `Tkinter`, respectively.
- **Step 3:** Implement `analyzer.py` to check password strength using `zxcvbn` and return feedback and crack time.
- **Step 4:** Develop `wordlist_generator.py` to generate custom wordlists using user-provided info like name, pet, or year.
- **Step 5:** Design a clean and modern `Tkinter` GUI that takes user input and shows results or exports files.
- **Step 6:** Finalize by organizing code, testing functionality, and writing documentation and README.

---

## 5. Conclusion

SecurePassAnalyzer successfully demonstrates the importance of using strong, unique passwords. It gives users immediate insight into how easily their passwords can be guessed and shows how personal information can be leveraged in targeted attacks. By combining educational feedback and wordlist generation, the tool serves as both a learning aid and a practical security testing resource. This project highlights how security awareness and simple tools can empower users to make better password choices.

---

## Output Example

- Wordlist exported to: `output/wordlist.txt`
- Sample input:  
  - Password: `john123`  
  - Info: `john rex 2001` → Generated: `john2001`, `rex@123`, etc.

---
