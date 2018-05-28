grammar Drapcode;

@lexer::memebers {
     // The amount of opened braces, brackets and parenthesis.
      private int opened = 0;
}

prog: ( stat? NEWLINE )* ;

stat:   PRINT value #print
         |    ID '=' STRING #assign;

value: ID | STRING;

PRINT:	'shout' ; // prints the info to stdout
READ: 'gimme';  // takes the output from the user

ID:   ('a'..'z'|'A'..'Z')+;
STRING :  '"' ( ~('\\'|'"') )* '"';



// Digits
NUMBER: INTEGER
 | FLOAT_NUMBER
 ;

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


 // For arrays
 OPEN_BRACK : '[' {opened++;};
 CLOSE_BRACK : ']' {opened--;};

NEWLINE:	'\r'? '\n';
WS : [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines
COMMENT : '#' ~[\r\n\f]* -> skip; // truncate the comments

 // Operations
 STAR : '*';
 ADD : '+';
 MINUS : '-';
 DIV : '/';
