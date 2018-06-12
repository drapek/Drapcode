grammar Drapcode;


// Some fragments are commented because it will be develop it the near future but now it could obfuscate the actual problem
// Digits
//NUMBER: INTEGER
// | FLOAT_NUMBER
// ;

fragment DIGIT : [0-9];

INTEGER:   DIGIT+
            | '0'+
            ;

FLOAT_NUMBER: INT_PART? FRACTION ;


fragment INT_PART
 : DIGIT+
 ;

fragment FRACTION
 : '.' DIGIT+
 ;

//// Terminals
//// For arrays
//OPEN_BRACK : '[';
//CLOSE_BRACK : ']';


// Operations
MULT : '*';
DIV : '/';
ADD : '+';
MINUS : '-';

// Global
EQ : '=';
COLON: ':';

WHILE: 'while';
WHILE_END: 'endwhile';
IF: 'if';
IF_END: 'endif';
PRINT: 'shout'; // prints the info to stdout
READ: 'gimme';  // takes the output from the user
//FUNC: 'func';
//FUNC_END: 'endfunc';
//COMMA: ',';

// Conditions
EQUALS: '==';
GREAT_THAN: '>';
GREAT_EQ_THAN: '>=';
LESS_THAN: '<';
LESS_EQ_THAN: '<=';
DIFFERENT: '!=';

ID:   ('a'..'z'|'A'..'Z' | '_')+;
STRING :  '"' ( ~('\\'|'"') )* '"';

NEWLINE: ('\r\n' | '\n' | '\r');
WS : [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines
COMMENT : '#' ~[\r\n\f]* -> skip; // truncate the comments

//prog: ((stmt | function)? NEWLINE )*;
prog: block;

stmt:  while_cond #while
     |  if_cond #if
     | ID EQ var_def #assign
     | PRINT ID #print
     | READ ID #read;
    /* | ID #func_call; */

while_cond: WHILE condition COLON blockwhile WHILE_END;
if_cond: IF condition COLON blockif IF_END;
blockwhile: block;
blockif: block;
block: (stmt? NEWLINE )*;

var_def: expr0 /*| NUMBER | STRING | array*/;

expr0: expr1 #single0
       | expr1 ADD expr1 #add
       ;

expr1: expr2 #single1
       | expr2 MINUS expr2 #sub
       ;

expr2: expr3 #single2
       | expr3 MULT expr3 #mult
       ;

expr3: expr4 #single3
       | expr4 DIV expr4 #div
       ;

expr4:
       INTEGER #int
       | FLOAT_NUMBER #float
       | ID #expr_id
       | '(' expr0 ')' #par
       ;

var_num: ID | INTEGER ;

condition:   var_num EQUALS var_num #cond_eq
           | var_num GREAT_THAN var_num #cond_gt
           | var_num GREAT_EQ_THAN var_num #cond_gte
           | var_num LESS_THAN var_num #cond_lt
           | var_num LESS_EQ_THAN var_num #cond_lte
           | var_num DIFFERENT var_num #cond_diff // eg. 2.0 != var_a
           ;

//array: OPEN_BRACK (VAR_NUMERIC COMMA)+ CLOSE_BRACK; // eg. [1.2, 2.0, 2, 5]
//ARRAY_APPEAL: ID OPEN_BRACK INTEGER CLOSE_BRACK;  // eg. arr[1]
//function: FUNC ID params COLON block FUNC_END;
//params: (var (COMMA var)*)?;

