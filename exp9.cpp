/*
✅ Step 1: uppercase.l (Flex file)
%{
#include "y.tab.h"
#include <iostream>
#include <cctype>
%}

%option noyywrap

%%

[a-z]    { return LOWERCASE; }  // Match lowercase letters
[A-Z]    { return UPPERCASE; }  // Match uppercase letters
[ \t\n]+ ; // Ignore whitespace


.        { return UNKNOWN; }  // Match any other characters

%%
✅ Step 2: uppercase.y (Yacc file)

%{
#include <iostream>
#include <cctype>
using namespace std;

%}

%token LOWERCASE
%token UPPERCASE
%token UNKNOWN

%%

sentence:
    sentence character  { cout << $2; }
  | character            { cout << $1; }
  ;

character:
    LOWERCASE  { cout << (char)(toupper(yytext[0])); }  // Convert lowercase to uppercase
  | UPPERCASE  { cout << yytext; }  // Keep uppercase as is
  | UNKNOWN    { cout << yytext; }  // Output non-alphabetic characters as is
  ;

%%

int main() {
    cout << "Enter a sentence: ";
    yyparse();  // Start parsing
    cout << endl;
    return 0;
}

void yyerror(const char *s) {
    cerr << "Error: " << s << endl;
}


🧰 Step 3: Compile and Run
bison -d uppercase.y  // Generate parser code
flex uppercase.l      // Generate lexer code
g++ lex.yy.c uppercase.tab.c -o uppercase

./uppercase

hello world!

HELLO WORLD!

*/
