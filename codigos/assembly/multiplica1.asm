    goto main
    wb 0
result ww 0 
a ww 0
b ww 5
u ww 1

main add x, b             # if b=0 goto final
     jz x, final
     sub x, b
     
     add x, a             # r = r + a
     add x, result
     mov x, result
     sub x, result
     
     add x, b             # b = b - 1
     sub x, u     
     mov x, b
     sub x, b
     
     goto main
final halt
     