let%test _ = 
try
  let _ = Hw10.interp (ParserMain.parse "1 + false") [] in false
with
|Failure msg -> msg = "Not a number: 1 + false"

let%test _ = 
try
  let _ = Hw10.interp (ParserMain.parse "let rec x = 3 in x") [] in false
with
|Failure msg -> msg = "Not a function: 3"

let%test _ = 
try
  let _ = Hw10.interp (ParserMain.parse "true true") [] in false
with
|Failure msg -> msg = "Not a function: true"

let%test _ = 
try
  let _ = Hw10.interp (ParserMain.parse "if 1 then 2 else 3") [] in false
with
|Failure msg -> msg = "Not a bool: 1"

let%test _ = 
try
  let _ = Hw10.interp (ParserMain.parse "let owo = 3 < false in owo + 1") [] in false
with
|Failure msg -> msg = "Not a number: 3 < false"

let%test "id" = Hw10.interp (ParserMain.parse "let x = 5 in x") [] = NumV 5

let%test "la" = Hw10.interp (ParserMain.parse "let f = (fun x y -> y + y) (1 + true) in f 1") [] = NumV 2

(* let%test "rec" = Hw10.interp (ParserMain.parse "let rec add = (fun x -> if x = 1 then x else add (x - 1)) in add 5") [] = NumV 15 *)

let%test "su1" = Hw10.interp (ParserMain.parse "3 - 1") [] = NumV 2

let%test "su2" = 
try
  let _ = Hw10.interp (ParserMain.parse "3 - false") [] in false
with
|Failure msg -> msg = "Not a number: 3 - false"

let%test "re" = Hw10.interp (ParserMain.parse "let rec adx = (fun x y -> if 0 < x then (adx (x - 1) (y + x)) else y) in adx 5 0") [] = NumV 15

