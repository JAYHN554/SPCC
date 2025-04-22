# SPCC
SPCC Practical Exam
This repository contains the source code and solutions for the Software Practical Core Course (SPCC) practical exam. The practical exam focuses on demonstrating proficiency in core software engineering concepts including programming, algorithms, and basic compiler construction.

The repository includes multiple solutions built with different tools, demonstrating a variety of practical skills such as lexical analysis, syntax parsing, code generation, and data structure manipulation.

Installation and Setup
For Flex/Bison (C++):
Install Flex and Bison:

On Ubuntu:

bash
Copy
Edit
sudo apt-get install flex bison
On macOS:

bash
Copy
Edit
brew install flex bison
Compile the Lex and Yacc files:

bash
Copy
Edit
bison -d parser.y      # Generates parser code
flex lexer.l           # Generates lexer code
g++ lex.yy.c parser.tab.c -o practical_exam   # Compile both
For Python (PLY):
Install PLY using pip:

bash
Copy
Edit
pip install ply
Running the Programs
For Lex and Yacc (C++):
After compilation, run the program with:

bash
Copy
Edit
./practical_exam < input.txt
You will be prompted to enter any required input, and the program will process it accordingly.

For Python-based Solutions:
To run the Python code (e.g., lexical analyzer or code generator):

bash
Copy
Edit
python lexer.py
Individual Programs
Lexer and Parser
This section demonstrates the use of Flex (Lexical Analyzer) and Bison (Parser) for tasks like:

Tokenizing input text (words, numbers, symbols)

Parsing structured text (e.g., mathematical expressions or simple statements)

Instructions:
Define your grammar and lexical rules in lexer.l and parser.y.

Compile using Flex and Bison as described above.

Run the executable with an input file or directly via standard input.

Code Generation
This program demonstrates the generation of intermediate code or machine code using a simple algorithm in C++. For example, converting three-address code (TAC) into assembly-like instructions.

Instructions:
Modify the codegen.cpp file to change the type of code generation or to test new expressions.

Compile the program using g++ codegen.cpp -o codegen.

Run the program with appropriate input.

Python Code for Lexical Analysis
For Python solutions related to lexical analysis (using PLY), check the lexer.py script.

Tools Used
Flex: A fast lexical analyzer generator that reads a set of rules and generates a tokenizer.

Bison: A parser generator for context-free grammars, commonly used in compiler construction.

g++: The C++ compiler used to compile the C++ files.

PLY (Python Lex-Yacc): A Python library for lexical analysis and parsing.

Contributors
[Your Name] - Jay Nakashe