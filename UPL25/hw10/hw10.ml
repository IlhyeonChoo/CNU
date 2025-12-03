let rec interp (ast: Ast.expr) (mem: Store.t) : Store.value =
  match ast with
    | Num n -> NumV n
    | Bool b -> BoolV b
    | Id st ->
        begin
          match (Store.find st mem) with
            | FreezedV (e1, memf) -> interp e1 memf
            | _ -> Store.find st mem
        end
    | Add (e1, e2) -> 
      (match (interp e1 mem, interp e2 mem) with
        | NumV n1, NumV n2 -> NumV (n1 + n2)
        | _ -> failwith (Format.asprintf "Not a number: %a + %a" Ast.pp e1 Ast.pp e2))
    | Sub (e1, e2) ->
      (match (interp e1 mem, interp e2 mem) with
        | NumV n1, NumV n2 -> NumV (n1 - n2)
        | _ -> failwith (Format.asprintf "Not a number: %a - %a" Ast.pp e1 Ast.pp e2))
    | LetIn (st, e1, e2) ->
      interp e2 (Store.add st (interp e1 mem) mem)
    | RLetIn (st, e1, e2) -> 
      begin
        match interp e1 mem with
          | ClosureV (st', ce1, mem') ->
            let rec mem'' = (st, Store.ClosureV (st' , ce1, mem'')) :: List.remove_assq st mem' in
              interp e2 mem''
          | _ -> failwith (Format.asprintf "Not a function: %a" Ast.pp e1)
      end
    | App (e1, e2) ->
      (match interp e1 mem with
        | ClosureV (st, ce1, mem') -> interp ce1 (Store.add st (FreezedV (e2, mem)) mem')  (* C1, C2 는 안되는건가? C2가 파라메터 없다면? 무조건 있어야해서 unit 같은게 있다고 하신거 같긴한데 *)
        | _ -> failwith (Format.asprintf "Not a function: %a" Ast.pp e1))
    | Lambda (st, e2) -> 
        ClosureV (st, e2, mem)
    | Cond (exprbool, exprture, exprfal) ->
      (match (interp exprbool mem) with
        | BoolV bo -> if bo = true then interp exprture mem else interp exprfal mem
        | _ -> failwith (Format.asprintf "Not a bool: %a" Ast.pp exprbool))
    | LessThan (e1, e2) -> 
      match (interp e1 mem, interp e2 mem) with
        | NumV n1, NumV n2 -> if n1 < n2 then BoolV true else BoolV false
        | _, _ -> failwith (Format.asprintf "Not a number: %a < %a" Ast.pp e1 Ast.pp e2) 

