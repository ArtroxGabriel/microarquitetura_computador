import ufc2x as cpu
import memory as mem
import clock as clk

mem.write_word(2, 100)
mem.write_word(3, 50)

# y = y + mem[2]
mem.write_byte(1, 17)
mem.write_byte(2, 2)

# y = y + mem[3]
mem.write_byte(3, 17)
mem.write_byte(4, 3)

# mem[1] = y
mem.write_byte(5, 25)
mem.write_byte(6, 1)

clk.start([cpu])

print(mem.read_word(1))
