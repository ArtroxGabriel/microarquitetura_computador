import ufc2x as cpu
import memory as mem
import clock as clk

mem.write_word(0, 6836)
mem.write_word(1, 2432)

print("antes: ", mem.read_word(3))

clk.start([cpu])

print("depois: ", mem.read_word(3))
