     goto main
     wb 0

r ww 0
a ww 3
b ww 20
u ww 1

main  add x, a
      jz x, final
      sub x, u
      mov x, a
      sub x, a

      add x, b
      jz x, final2
      sub x, u
      mov x, b
      sub x, b

      goto main
final halt

final2 add x, u
       mov x, r
       halt