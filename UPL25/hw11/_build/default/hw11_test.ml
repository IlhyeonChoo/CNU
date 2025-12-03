let%test _ = Hw11.interp_prog (ParserMain.parse "x = 3;") = [("x", Store.NumV 3)]

let%test _ =
try
  let _ = Hw11.interp_prog (ParserMain.parse "x = 3;\ny = 4;\nif x {\nx = x - 2;\n}") in false
with
| Failure msg -> msg = "Not a bool: x"
let%test _ =
try
  let _ = Hw11.interp_expr (Ast.Add (Ast.Num 1, Ast.Bool true)) [] in false
with
| Failure msg -> msg = "Not a number: 1 + true"

let%test _ = Hw11.interp_expr (Ast.Eq (Ast.Num 1, Ast.Bool true)) [] = Store.BoolV false
let%test _ = Hw11.interp_expr (Ast.Eq (Ast.Num 1, Ast.Num 1)) [] = Store.BoolV true
let%test _ = Hw11.interp_expr (Ast.Eq (Ast.Bool true, Ast.Bool true)) [] = Store.BoolV true

(* let%test _ = Hw11.interp_prog (ParserMain.parse "x = 1;\ny = 0;\nwhile (x < 3) {\n y = x + y;\n x = x + 1;\n}") = [("x", Store.NumV 3);("y", Store.NumV 3)] *)
let%test _ = Hw11.interp_stmt (Ast.LoopStmt (Ast.Lt (Ast.Name "x", Ast.Num 5), [Ast.AssignStmt ("x", Ast.Add (Ast.Name "x", Ast.Num 1))])) [("x", Store.NumV 1)] = [("x", Store.NumV 5)]

let%test _ =
try
  let _ = Hw11.interp_stmt (Ast.LoopStmt (Ast.Num 1, [Ast.AssignStmt ("x", Ast.Add (Ast.Name "x", Ast.Num 1))])) [("x", Store.NumV 1)] in false
with
| Failure msg -> msg = "Not a bool: 1"

let%test "if" = Hw11.interp_stmt (Ast.IfStmt (Ast.Gt (Num 2, Num 5), [Ast.AssignStmt ("x", Ast.Add (Num 1, Num 2))], [Ast.AssignStmt ("y", Ast.Sub (Num 5, Num 2))])) [] = [("y", Store.NumV 3)]

let%test "ifG" = Hw11.interp_stmt (Ast.IfStmt (Ast.Gt (Num 5, Num 2), [Ast.AssignStmt ("x", Ast.Add (Num 1, Num 2))], [Ast.AssignStmt ("y", Ast.Sub (Num 5, Num 2))])) [] = [("x", Store.NumV 3)]

let%test "orif" = Hw11.interp_stmt (Ast.IfStmt (Ast.Or (Bool true, Bool false), [Ast.AssignStmt ("x", Ast.Add (Num 1, Num 2))], [Ast.AssignStmt ("y", Ast.Sub (Num 5, Num 2))])) [] = [("x", Store.NumV 3)]

let%test "orif" = Hw11.interp_stmt (Ast.IfStmt (Ast.Or (Bool false, Bool true), [Ast.AssignStmt ("x", Ast.Add (Num 1, Num 2))], [Ast.AssignStmt ("y", Ast.Sub (Num 5, Num 2))])) [] = [("x", Store.NumV 3)]


let%test "orfal" = Hw11.interp_stmt (Ast.IfStmt (Ast.Or (Bool false, Bool false), [Ast.AssignStmt ("x", Ast.Add (Num 1, Num 2))], [Ast.AssignStmt ("y", Ast.Sub (Num 5, Num 2))])) [] = [("y", Store.NumV 3)]

let%test "andtr" = Hw11.interp_stmt (Ast.IfStmt (Ast.And (Bool true, Bool true), [Ast.AssignStmt ("x", Ast.Add (Num 1, Num 2))], [Ast.AssignStmt ("y", Ast.Sub (Num 5, Num 2))])) [] = [("x", Store.NumV 3)]

let%test "andfal" = Hw11.interp_stmt (Ast.IfStmt (Ast.And (Bool false, Bool true), [Ast.AssignStmt ("x", Ast.Add (Num 1, Num 2))], [Ast.AssignStmt ("y", Ast.Sub (Num 5, Num 2))])) [] = [("y", Store.NumV 3)]

let%test "failsub" = 
try
  let _ = Hw11.interp_expr (Ast.Sub (Ast.Bool true, Ast.Num 1)) [] in false
with
| Failure msg -> msg = "Not a number: true - 1"

let%test "failLt" =
  try
  let _ = Hw11.interp_expr (Ast.Lt (Ast.Bool true, Ast.Num 1)) [] in false
  with
    | Failure msg -> msg = "Not a number: true < 1"

let%test "failGt" =
  try
  let _ = Hw11.interp_expr (Ast.Gt (Ast.Bool true, Ast.Num 1)) [] in false
  with
    | Failure msg -> msg = "Not a number: true > 1"

let%test "failOr" =
  try
  let _ = Hw11.interp_expr (Ast.Or (Ast.Bool true, Ast.Num 1)) [] in false
  with
    | Failure msg -> msg = "Not a bool: true || 1"

let%test "failAnd" =
  try
  let _ = Hw11.interp_expr (Ast.And (Ast.Bool true, Ast.Num 1)) [] in false
  with
    | Failure msg -> msg = "Not a bool: true && 1"

let%test "Eqnf" = Hw11.interp_expr (Ast.Eq (Ast.Num 1, Ast.Num 2)) [] = BoolV false
let%test "Eqbf" = Hw11.interp_expr (Ast.Eq (Ast.Bool true, Ast.Bool false)) [] = BoolV false


