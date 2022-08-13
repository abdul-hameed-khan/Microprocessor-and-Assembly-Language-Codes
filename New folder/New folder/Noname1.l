%option noyywrap
%{
	#include<stdio.h>
%}

%%


[a-zA-z] printf("Identifier");
.         printf("not an identifier");



%%
int main()
{
yylex();
	return 0;
}