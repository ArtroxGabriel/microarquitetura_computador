    goto main
    wb 0

a ww 0 # guardar na word 1 sempre
b ww 4
c ww 6

main    add x, b # X <- X + B
        add x, c # X <- X + C
        mov x, a # A <- X
        halt     # finaliza