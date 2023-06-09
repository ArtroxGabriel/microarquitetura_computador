 goto main
 wb 0
 
r ww 0 
b ww 3
c ww 2
u ww 1

main add x, c
     jz x, final
     sub x, c
     add x, b
     add x, r
     mov x, r
     sub x, r
     add x, c
     sub x, u     
     mov x, c
     sub x, c
     goto main
final halt
     
     
     
