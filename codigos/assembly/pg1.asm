    goto main
    wb 0

a ww 0 # guardar na word 1 sempre
b ww 4
c ww 6

main    add y, b # X <- X + B
        add y, c # X <- X + C
        mov y, a # A <- X
        zerar y
        halt     # finaliza