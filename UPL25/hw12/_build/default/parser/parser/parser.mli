
(* The type of tokens. *)

type token = 
  | WHILE
  | TRUE
  | STAR
  | SEMICOLON
  | RIGHT_PARENTHESIS
  | RIGHT_BRACE
  | RETURN
  | REF
  | PLUS
  | OR
  | NUMBER of (int)
  | MINUS
  | LESSTHAN
  | LEFT_PARENTHESIS
  | LEFT_BRACE
  | IF
  | ID of (string)
  | GREATERTHAN
  | FUNDEF
  | FALSE
  | EQ
  | EOF
  | ELSE
  | DEF
  | COMMA
  | COLON
  | AND

(* This exception is raised by the monolithic API functions. *)

exception Error

(* The monolithic API. *)

val parse: (Lexing.lexbuf -> token) -> Lexing.lexbuf -> (Ast.prog)
