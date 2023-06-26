    goto main # questao 1 - funcao potencia
    wb 0

r ww 0        # retorno da funcao potencia
m ww 4       # argumento da potencia: base
n ww 8        # argumento da potencia: expoente
a ww 0        # argumento da funcao multiplicacao
b ww 0        # argumento da funcao multiplicacao
z ww 0        # retorno da funcao multiplicacao
d ww 1        # +1 or -1

main add x, m
     jz x, caso1 # base igual a 0
     sub x, d
     jz x, caso2 # base igual a 1

     add y, n
     jz y, caso3 # expoente igual a 0
     sub y, d
     jz y, caso4 # expoente igual a 1

     mov y, n    # n <- n -1
     zerar y    # y <- 0

     add x, d    
     mov x, a    # a <- x
     mov x, b    # b <- x
     zerar x
    
     goto mult

    
caso1 halt
caso2 add x, m
      mov x, r
      halt
caso3 add y, d
      mov y, r
      halt
caso4 add y, m
      mov y, r
      halt

potencia add y, n
         sub y, d
         jz y, finalpotencia
         mov y, n
         zerar y
         
         add x, m
         mov x, b # b <- m
         zerar x 
         
         add x, z 
         mov x, a  # a <- z
         

         zerar x # z <- 0
         mov x, z
         
         goto mult
finalpotencia add y, z
              mov y, r
              halt

mult add y, b     # multiplicacao z <- a * b       
     jz y, finalmult
     zerar y
     
     add y, a             
     add y, z
     mov y, z
     zerar y
     
     add y, b            
     sub y, d     
     mov y, b
     zerar y
     
     goto mult
finalmult goto potencia