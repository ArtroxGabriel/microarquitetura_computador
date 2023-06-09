 goto main
 wb 0
 
r ww 0 
b ww 2
c ww 3
u ww 1

main add x, c
     jz x, final
     
     sub x, u
     mov x, c
     sub x, c
     
     add x, r
     add x, b
     mov x, r
     sub x, r
     
     goto main
     
final halt
     
     
     
