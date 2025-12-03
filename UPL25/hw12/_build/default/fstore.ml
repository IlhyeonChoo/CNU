type t = (string * string list * Ast.stmt list) list

let empty : t = []

(* val add : string -> string list -> Ast.stmt list -> t -> t
val find : string -> t -> (string list * Ast.stmt list) *)


let add (st: string) (stl: string list) (stml: Ast.stmt list) (memf: t) : t =
  let memf' = List.remove_assq st memf in
  (st, (stl, stml)) :: memf'

let rec find (st: string) (memf: t) : (string list * Ast.stmt list) =
  match memf with
    | [] -> failwith ("Unbound function: " ^ st)
    | (h, tuple) :: t -> if h = st then tuple else find st t

