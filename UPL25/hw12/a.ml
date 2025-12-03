  let%test _ = 
    let prog : string = 
    "
      def x = 0;
      def y = 1;
      def z = x + y;
    "
    in
    let e, m = Hw12.interp_prog (ParserMain.parse prog) in
    
