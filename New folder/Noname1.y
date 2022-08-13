%{
#include<stdio.h>

int regs[26];
int base;

%}

%token DIGIT LETTER

%left '|'
%left '&'
%left '+' '-'
%left '*' '/' '%'


%%      
expr:expr'+'term{printf(" \ne + t");}|expr'-'term {printf("\ne - t");}|term {printf("\nt");}
term:term'*'factor{printf("\nt * f");}|term'/'factor {printf("\nt / f");}|factor {printf("\nf");}
factor:DIGIT {printf("\nD");}|LETTER {printf("\nL");}

%%
main()
{
printf("\nenter expression");
 yyparse();
 printf("\n Result Parse succesfully");
 getch();
}

yyerror(s)
char *s;{



}

yywrap()
{
  return(1);
}