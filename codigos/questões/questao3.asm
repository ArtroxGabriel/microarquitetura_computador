    goto main # questa 3 - Operacao CSW
    wb 0

r ww 1    # retorno da funcao csw
a ww 2    # argumento da funcao csw
b ww 2    # operando da funcao csw
c ww 10   # argumento da funcao csw


main add x, a # a != c; a <- c; return 1
     sub x, c
     jz x, else
     add y, c
     mov y, a
     halt


else mov x, r # a == c; c <- b; return 0
     add x, b
     mov x, c
     halt