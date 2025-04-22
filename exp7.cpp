/*
 File: lexer.l (Flex File)
 %{
#include <iostream>
using namespace std;
%}

%option noyywrap

%%

"+"         { cout << "PLUS\t\t" << yytext << endl; }
"-"         { cout << "MINUS\t\t" << yytext << endl; }
"*"         { cout << "TIMES\t\t" << yytext << endl; }
"/"         { cout << "DIVIDE\t\t" << yytext << endl; }
"="         { cout << "ASSIGN\t\t" << yytext << endl; }
";"         { cout << "SEMI\t\t" << yytext << endl; }
"("         { cout << "LPAREN\t\t" << yytext << endl; }
")"         { cout << "RPAREN\t\t" << yytext << endl; }

[0-9]+      { cout << "NUMBER\t\t" << yytext << endl; }
[a-zA-Z_][a-zA-Z0-9_]* { cout << "IDENTIFIER\t" << yytext << endl; }

[ \t\n]+    ;  // Ignore whitespace

.           { cout << "UNKNOWN\t\t" << yytext << endl; }

%%

int main() {
    yylex();
    return 0;
}
 Sample Input to Test
You can run this on a file or paste into input:

c
Copy
Edit
a = 10 + 5;
b = a * 3;
How to Compile and Run
bash
Copy
Edit
flex lexer.l
g++ lex.yy.c -o lexer
./lexer < input.txt
Sample output
IDENTIFIER	a
ASSIGN		=
NUMBER		10
PLUS		+
NUMBER		5
SEMI		;
IDENTIFIER	b
ASSIGN		=
IDENTIFIER	a
TIMES		*
NUMBER		3
SEMI		;

*/