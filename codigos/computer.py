import ufc2x as cpu
import memory as mem
import clock as clk

mem.write_word(50, 21)
mem.write_word(100, 32)
mem.write_word(130, 10)

# X <- X + memory[50]
mem.write_byte(1, 30)
# stop
mem.write_byte(2, 255)


clk.start([cpu])

print(cpu.Y)
