    goto main
    wb 0

r ww 0
b ww 2
d ww 3
u ww 1

main    add y, d
        jz y, final
        sub y, d
        add y, b
        add y, r
        mov y, r
        sub y, r
        add y, d
        sub y, u
        mov y, d
        sub y, d
        goto main

final halt     
