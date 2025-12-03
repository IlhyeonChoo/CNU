let%test _ =
try
  let _ = Hw9.interp (ParserMain.parse "1 1") [] in false
with
|Failure msg -> msg = "Not a function: 1"

let%test _ =
try
  let _ = Hw9.interp (ParserMain.parse "1 + true") [] in false
with
|Failure msg -> msg = "Not a number: 1 + true"

let%test "add" = Hw9.interp (ParserMain.parse "let addx = (fun n1 n2 -> n1 + n2) in addx 5 3") [] = NumV 8

let%test "con" = Hw9.interp (ParserMain.parse "if 1 < 2 then 1 else 2") [] = NumV 1

let%test "bo" =
try
  let _ = Hw9.interp (ParserMain.parse "if 1 then 1 else 2") [] in false
with
|Failure msg -> msg = "Not a bool: 1"

let%test "lesse" =
try
  let _ = Hw9.interp (ParserMain.parse "true < 2") [] in false
with
|Failure msg -> msg = "Not a number: true < 2"

let%test "sub" = Hw9.interp (ParserMain.parse "let subx = (fun n1 n2 -> n1 - n2) in subx 5 2") [] = NumV 3

let%test "sube" =
try
  let _ = Hw9.interp (ParserMain.parse "5 - true") [] in false
with
|Failure msg -> msg = "Not a number: 5 - true"

let%test "less" = Hw9.interp (ParserMain.parse "if 2 < 1 then 1 else 2") [] = NumV 2
