type t = (Env.addr * Value.t) list
  
let empty : t = []

(* val add : Env.addr -> Value.t -> t -> t *)
(* val find : Env.addr -> t -> Value.t *)

let add (a: Env.addr) (vl: Value.t) (mem: t) : t =
  let mem' = List.remove_assq a mem in
    (a, vl) :: mem'

let rec find (a: Env.addr) (mem: t) : Value.t =
  match mem with
    | [] -> failwith ("Free identifier: " ^ a)
    | (ad, v) :: t -> if ad = a then v else find a t

