type addr = int

type t = (string * addr) list

let empty : t = []

(* add : string -> addr -> t -> t *)
let add (st: string) (a: addr) (mem: t) : t =
  let mem' = List.remove_assq st mem in
    (st, a) :: mem'

(* find : string -> t -> addr *)
let rec find (st: string) (mem: t) : addr =
  match mem with
    | [] -> failwith ("Free identifier: " ^ st)
    | (h, v) :: t -> if h = st then v else find st t

