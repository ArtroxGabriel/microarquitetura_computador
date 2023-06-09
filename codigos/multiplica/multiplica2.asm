 goto main
 wb 0
 
r ww 0 
b ww 2
c ww 3
u ww 1

main add x, c      # if c=0 goto final
     jz x, final   
     
     sub x, u      # c = c - 1
     mov x, c
     sub x, c
     
     add x, r      # r = r + b
     add x, b
     mov x, r
     sub x, r
     
     goto main
     
final halt
     
     
     
