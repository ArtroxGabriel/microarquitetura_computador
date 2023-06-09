    goto main # questao 4 - funcao fatorial
    wb 0       

r ww 1        # retorno da funcao fatorial
n ww 11       # n: argumentos da funcao fatorial
a ww 1        # a: argumento da funcao multiplicacao
b ww 1        # b: argumento da funcao multiplicacao
z ww 0        # retorno da multiplicacao
d ww 1        # +1 ou -1

main add x, n  
     
     jz x, finalmain # Se N igual a 0, finaliza o programa e retorna r = 1       
     sub x, d
     jz x, finalmain # verificao se é 1
     add x, d
     
     mov x, a # a <- n
     sub x, d 
     mov x, b # b <- n - 1
     mov x, n # n - 1
     zerar x # 0
     goto mult
finalmain add y, z
          jz y, caso1
          mov y, r 
              
caso1 halt

fact add x, n # n
     sub x, d # n - 1
     jz x, finalmain
     
     mov x, b # b <- n - 1
     mov x, n # n <- n - 1

     zerar x # x <- 0
     add x, z
     mov x, a # a <- z
     
     zerar x
     mov x, z # z <- 0 
     goto mult    

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
finalmult goto fact