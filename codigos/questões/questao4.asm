    goto main # questao 4 - funcao fatorial
    wb 0      # argumentos: N

r ww 1        # retorno da funcao fatorial
n ww 10        #   
a ww 1        # 
b ww 1        # 
z ww 0        # 
d ww 1        # 

main add x, n   
     jz x, finalmain # Se N igual a 0, finaliza o programa e retorna r = 1       
     
     mov x, a # a <- n
     sub x, d 
     mov x, b # b <- n - 1
     mov x, n # n - 1
     sub x, n # 0
     goto mult
finalmain add y, z
          jz y, caso1
          mov y, r 
          halt    
caso1 add y, d
      mov y, r
      halt

fact add x, n # n
     sub x, d # n - 1
     jz x, finalmain
     
     mov x, b # b <- n - 1
     mov x, n # n <- n - 1

     sub x, n # x <- 0
     add x, z
     mov x, a # a <- z
     
     sub x, a 
     mov x, z # z <- 0 
     goto mult    

mult add y, b     # multiplicacao z <- a * b       
     jz y, finalmult
     sub y, b
     
     add y, a             
     add y, z
     mov y, z
     sub y, z
     
     add y, b            
     sub y, d     
     mov y, b
     sub y, b
     
     goto mult
finalmult goto fact