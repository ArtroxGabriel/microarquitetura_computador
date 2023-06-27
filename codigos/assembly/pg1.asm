    goto main
    wb 0

a ww 0 # guardar na word 1 sempre
b ww 4
c ww 6
d ww 1

main    add y, b # y <- y + B
        add y, c # y <- y + C
        inc y
        mov y, a # A <- y
        halt     # finaliza