%{
#include<stdio.h>

int regs[26];
int base;

%}

%start expr

%union { int a; }


%token DIGIT LETTER

%left '|'
%left '&'
%left '+' '-'
%left '*' '/' '%'


%%      
expr: expr'+'term{printf("addition expression");}|expr'-'term {printf("subtraction expression");}|term {printf("no rule");}
term:term'*'factor{printf("multipliction expression");}|term'/'factor|factor
factor:DIGIT|LETTER

%%
main()
{
printf("\nenter expression");
 yyparse();
 printf("Result");
 getch();
}

yyerror(s)
char *s;
{
  fprintf(stderr, "%s\n",s);
}

yywrap()
{
  return(1);
}