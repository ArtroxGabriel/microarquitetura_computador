import ufc2x as cpu
import memory as mem
import clock as clk
 

clk.start([cpu])

print(mem.read_word(150))
