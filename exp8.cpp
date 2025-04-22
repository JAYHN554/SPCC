/*
 Step 1: wordcounter.l (Lex file)
 %{
#include "y.tab.h"
%}

%option noyywrap

%%

[a-zA-Z]+      { return WORD; }
[ \t\n]+       ;   // Skip whitespace
.              ;   // Ignore other characters

%%Step 2: wordcounter.y (Yacc file)
yacc
%{
#include <iostream>
using namespace std;

int word_count = 0;
%}

%token WORD

%%

sentence:
    sentence WORD  { word_count++; }
  | WORD           { word_count++; }
  ;./wordcounter


%%

int main() {
    cout << "Enter a sentence: ";
    yyparse();
    cout << "Number of words: " << word_count << endl;
    return 0;
}

void yyerror(const char *s) {
    cerr << "Error: " << s << endl;
}
Step 3: Compile and Run
bison -d wordcounter.y
flex wordcounter.l

g++ lex.yy.c wordcounter.tab.c -o wordcounter

This is a test sentence

Number of words: 5

*/