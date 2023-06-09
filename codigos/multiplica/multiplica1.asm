goto main
 wb 0
 
r ww 0 
b ww 7
c ww 35
u ww 1

main add x, c      # if c=0 goto final
     jz x, final   
     sub x, c
     
     add x, b      # r = r + b
     add x, r
     mov x, r
     sub x, r
     
     add x, c      # c = c - 1
     sub x, u     
     mov x, c
     sub x, c
     
     goto main
final halt
     
