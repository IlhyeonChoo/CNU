(* interp_expr : Ast.expr -> Store.t -> Store.value *)
let rec interp_expr (ast: Ast.expr) (mem: Store.t) : Store.value =
  match ast with
    | Num n -> NumV n 
    | Name n -> Store.find n mem
    | Bool b -> BoolV b 
    | Add (e1, e2) ->
      begin
        match (interp_expr e1 mem, interp_expr e2 mem) with
          | NumV n1, NumV n2 -> NumV (n1 + n2)
          | _ -> failwith (Format.asprintf "Not a number: %a + %a" Ast.pp_expr e1 Ast.pp_expr e2)
      end
    | Sub (e1, e2) ->
      begin
        match (interp_expr e1 mem, interp_expr e2 mem) with
          | NumV n1, NumV n2 -> NumV (n1 - n2)
          | _ -> failwith (Format.asprintf "Not a number: %a - %a" Ast.pp_expr e1 Ast.pp_expr e2)
      end
    | Lt (e1, e2) ->
      begin
        match (interp_expr e1 mem, interp_expr e2 mem) with
          | NumV n1, NumV n2 -> if n1 < n2 then BoolV true else BoolV false 
          | _ -> failwith (Format.asprintf "Not a number: %a < %a" Ast.pp_expr e1 Ast.pp_expr e2)
      end
    | Gt (e1, e2) ->
      begin
        match (interp_expr e1 mem, interp_expr e2 mem) with
          | NumV n1, NumV n2 -> if n1 > n2 then BoolV true else BoolV false 
          | _ -> failwith (Format.asprintf "Not a number: %a > %a" Ast.pp_expr e1 Ast.pp_expr e2)
      end
    | Eq (e1, e2) ->
      begin
        match (interp_expr e1 mem, interp_expr e2 mem) with
          | NumV n1, NumV n2 -> if n1 = n2 then BoolV true else BoolV false
          | BoolV b1, BoolV b2 -> if b1 = b2 then BoolV true else BoolV false
          | _ -> BoolV false
      end
    | And (e1, e2) ->
      begin
        match (interp_expr e1 mem, interp_expr e2 mem) with
          | BoolV b1, BoolV b2 -> if b1 && b2 then BoolV true else BoolV false
          | _ -> failwith (Format.asprintf "Not a bool: %a && %a" Ast.pp_expr e1 Ast.pp_expr e2)
      end
    | Or (e1, e2) ->
      begin
        match (interp_expr e1 mem, interp_expr e2 mem) with
          | BoolV b1, BoolV b2 -> if b1 || b2 then BoolV true else BoolV false
          | _ -> failwith (Format.asprintf "Not a bool: %a || %a" Ast.pp_expr e1 Ast.pp_expr e2)
      end


(* interp_stmt : Ast.stmt -> Store.t -> Store.t *)
let rec interp_stmt (ast: Ast.stmt) (mem: Store.t) : Store.t =
  match ast with
  | AssignStmt (str, e) -> Store.add str (interp_expr e mem) mem
  | IfStmt (e, stl1, stl2) -> 
    begin
      match interp_expr e mem with
        | BoolV b -> if b then interp_stmtl stl1 mem else interp_stmtl stl2 mem
        | _ -> failwith (Format.asprintf "Not a bool: %a" Ast.pp_expr e)
    end    
  | LoopStmt (e, stl) ->
    begin
      match interp_expr e mem with
        | BoolV b -> if b then interp_stmt ast (interp_stmtl stl mem) else mem
        | _ -> failwith (Format.asprintf "Not a bool: %a" Ast.pp_expr e)
    end

(* interp_stmtl : Ast.stmt list -> Store.t -> Store.t *)
and interp_stmtl (ast: Ast.stmt list) (mem: Store.t) : Store.t =
  match ast with
    | [] -> mem
    | h::t -> interp_stmtl t (interp_stmt h mem)
      


(* interp_prog : Ast.prog -> Store.t *)
let interp_prog (ast: Ast.prog) : Store.t =
  match ast with
    | Program stl -> interp_stmtl stl []


