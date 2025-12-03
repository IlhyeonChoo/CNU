(* interp_expr : Ast.expr -> (Env.t, Mem.t)-> Value.t *)
let rec interp_expr (ast: Ast.expr) ((env: Env.t), (mem: Mem.t)) : Value.t =
  match ast with
    | Num n -> NumV n 
    | Ref str -> AddrV (Env.find str env)
    | Id n -> Mem.find n mem
    | Bool b -> BoolV b 
    | Add (e1, e2) ->
      begin
        match (interp_expr e1 (env, mem), interp_expr e2 (env, mem)) with
          | NumV n1, NumV n2 -> NumV (n1 + n2)
          | _ -> failwith (Format.asprintf "Not a number: %a + %a" Ast.pp_expr e1 Ast.pp_expr e2)
      end
    | Sub (e1, e2) ->
      begin
        match (interp_expr e1 (env, mem), interp_expr e2 (env, mem)) with
          | NumV n1, NumV n2 -> NumV (n1 - n2)
          | _ -> failwith (Format.asprintf "Not a number: %a - %a" Ast.pp_expr e1 Ast.pp_expr e2)
      end
    | Lt (e1, e2) ->
      begin
        match (interp_expr e1 (env, mem), interp_expr e2 (env, mem)) with
          | NumV n1, NumV n2 -> BoolV (n1 < n2)
          | _ -> failwith (Format.asprintf "Not a number: %a < %a" Ast.pp_expr e1 Ast.pp_expr e2)
      end
    | Gt (e1, e2) ->
      begin
        match (interp_expr e1 (env, mem), interp_expr e2 (env, mem)) with
          | NumV n1, NumV n2 -> BoolV (n1 > n2)
          | _ -> failwith (Format.asprintf "Not a number: %a > %a" Ast.pp_expr e1 Ast.pp_expr e2)
      end
    | Eq (e1, e2) ->
      begin
        match (interp_expr e1 (env, mem), interp_expr e2 (env, mem)) with
          | NumV n1, NumV n2 -> BoolV (n1 = n2)
          | BoolV b1, BoolV b2 -> BoolV (b1 = b2)
          | _ -> BoolV false
      end
    | And (e1, e2) ->
      begin
        match (interp_expr e1 (env, mem), interp_expr e2 (env, mem)) with
          | BoolV b1, BoolV b2 -> BoolV (b1 && b2)
          | _ -> failwith (Format.asprintf "Not a bool: %a && %a" Ast.pp_expr e1 Ast.pp_expr e2)
      end
    | Or (e1, e2) ->
      begin
        match (interp_expr e1 (env, mem), interp_expr e2 (env, mem)) with
          | BoolV b1, BoolV b2 -> BoolV (b1 || b2)
          | _ -> failwith (Format.asprintf "Not a bool: %a || %a" Ast.pp_expr e1 Ast.pp_expr e2)
      end

(* interp_stmt : Ast.stmt -> Fstore.t -> (Env.t, Mem.t) -> (Env.t, Mem.t) *)
let rec interp_stmt (ast: Ast.stmt) (memf: Fstore.t) ((env: Env.t), (mem: Mem.t)) : (Env.t * Mem.t) =
  match ast with
  | DefStmt (str, e) -> ((Env.add str (AddrManager.new_addr ()) env), Mem.add (AddrManager.new_addr ()) (interp_expr e (env, mem)) mem )
  | StoreStmt (e1, e2) ->
    begin
      match interp_expr e1 (env, mem) with
        | AddrV addr -> (env, Mem.add addr (interp_expr e2 (env, mem)) mem)
        | _ -> failwith (Format.asprintf "Not an address: %a" Ast.pp_expr e1)
    end
  | LoadStmt (str, e) ->
    begin 
      match interp_expr e (env, mem) with
        | AddrV addr -> (env, Mem.add (Env.find str env) (Mem.find addr mem) mem)
        | _ -> failwith (Format.asprintf "Not an address: %a" Ast.pp_expr e)
    end
  | IfStmt (e, stl1, stl2) -> 
    begin
      match interp_expr e (env,mem) with
        | BoolV b -> if b then interp_stmtl stl1 mem else interp_stmtl stl2 mem
        | _ -> failwith (Format.asprintf "Not a bool: %a" Ast.pp_expr e)
    end    
  | LoadStmt (e, stl) ->
    begin
      match interp_expr e (env,mem) with
        | BoolV b -> if b then interp_stmt ast (interp_stmtl stl mem) else mem
        | _ -> failwith (Format.asprintf "Not a bool: %a" Ast.pp_expr e)
    end
  | IfStmt (e, stl1, stl2) ->
      begin 
        match interp_expr e (env, mem) with
        | BoolV true -> interp_stmtl stl1 memf (env, mem)
        | BoolV false -> interp_stmtl stl2 memf (env, mem)
        | _ -> failwith (Format.asprintf "Not a bool: %a" Ast.pp_expr e)
      end
  | LoopStmt (e, stl) ->
      let rec loop (env, mem) =
        match interp_expr e (env, mem) with
        | BoolV true -> loop (interp_stmtl stl memf (env, mem))
        | BoolV false -> (env, mem)
        | _ -> failwith (Format.asprintf "Not a bool: %a" Ast.pp_expr e)
      in loop (env, mem)
  | ReturnStmt e -> (env, Mem.add (AddrManager.ret_addr) (interp_expr e (env, mem)) mem)
  | CallStmt (st1, st2, el) -> (* 함수 인자와 각 expr 연결 *)
    let rec mat (fs: string list) (el: expr list) ((env: Env.t), (mem: Mem.t)) : (Env.t * Mem.t) =
      begin 
        match (fs, el) with
        | [], [] -> (env, mem)
        | (hfs, tfs), (hel, tel) ->
          let env' = Env.add hfs (AddrManager.new_addr ()) env in
          let mem' = Mem.add (Env.find hfs env') (interp_expr hel (env', mem)) mem in
          mat tfs tel (env', mem') 
        | _, _ -> failwith (F.asprintf "The number of arguments not matched: actual %d, expected %d" (List.length args) (List.length pl))
      end
    in
    let (fsl, fal) = Fstore.find st2 memf in
    let (env', mem') = mat fsl el (env, mem) in
    let (_, mem'') = interp_stmtl fal memf (env', mem') in
    (env, mem'')

(* interp_stmtl : Ast.stmt list -> Fstore.t -> (Env.t, Mem.t) -> (Env.t, Mem.t) *)
and interp_stmtl (ast: Ast.stmt list) (memf: Fstore.t) ((env: Env.t), (mem: Mem.t)) : (Env.t * Mem.t) =
  match ast with
    | [] -> mem
    | h::t -> interp_stmtl t memf (interp_stmt h mem (env, mem))
      
(* interp_fundef: Ast.def -> Fstore.t -> Fstore.t *)
let interp_fundef (ast: Ast.def) (memf: Fstore.t) : Fstore.t =
  match ast with
    | Fundef (name, stl, stmtl) -> Fstore.add name stl stmtl memf

let rec interp_fundefl (ast: Ast.def list) (memf: Fstore.t) : Fstore.t =
  match ast with
    | [] -> memf
    | h::t -> interp_fundefl t (interp_fundef h memf)


(* interp_prog : Ast.prog -> (Env.t, Mem.t) *)
let interp_prog (ast: Ast.prog) : (Env.t * Mem.t) =
  match ast with
    | Program (fdl, stl) -> 
      let memf = interp_fundefl fdl Fstore.empty in
      interp_stmtl stl memf (Env.empty, Mem.empty)


