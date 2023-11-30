grammar tfGrammar;

program: statement+;

statement: assignment | if_statement;

assignment: ID '=' expr ';';

if_statement: 'if' expr 'then' statement+ 'end';

expr: INT
    | ID
    | '(' expr ')'
    | op=('*' | '/' | '+' | '-') expr expr
    ;

ID: [a-zA-Z]+;
INT: [0-9]+;
WS: [ \t\r\n]+ -> skip;
