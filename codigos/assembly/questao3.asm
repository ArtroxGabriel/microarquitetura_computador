    goto main
    wb 0

r ww 1
a ww 2
b ww 2
c ww 10


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