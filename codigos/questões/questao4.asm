    goto main # questao 4 - funcao fatorial
    wb 0       

r ww 1        # retorno da funcao fatorial
n ww 12       # argumentos da funcao fatorial
a ww 1        # argumento da funcao multiplicacao
b ww 1        # argumento da funcao multiplicacao
z ww 0        # retorno da multiplicacao

main add x, n  
     
     jz x, finalmain # Se N igual a 0, finaliza o programa e retorna r = 1       
     dec x
     jz x, finalmain # verificao se é 1
     inc x
     
     mov x, a # a <- n
     dec x 
     mov x, b # b <- n - 1
     mov x, n # n - 1
     zerar x # 0
     goto mult
finalmain add y, z
          jz y, caso1
          mov y, r 
              
caso1 halt

fact add x, n # n
     dec x # n - 1
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
     dec y     
     mov y, b
     zerar y
     
     goto mult
finalmult goto fact