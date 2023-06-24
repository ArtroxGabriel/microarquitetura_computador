goto main
wb 0

a ww 21
b ww 3
c ww 10
d ww 0

main add x, a
     jz x, nova
     add x, b
nova add x, c
     mov x, d
     halt