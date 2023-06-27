import cpu
import memory as mem
import clock as clk

mem.write_word(50, 21)
mem.write_word(100, 32)
mem.write_word(130, 10)

# X <- X + memory[50]
mem.write_byte(1, 17)
mem.write_byte(2, 50)

mem.write_byte(3, 34)
# stop
mem.write_byte(4, 255)


clk.start([cpu])

print(cpu.Y)
