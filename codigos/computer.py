import cpu
import memory as mem
import clock as clk

mem.write_word(50, 21)
mem.write_word(100, 32)
mem.write_word(130, 10)

# X <- memory[130] + memory[50]
mem.write_byte(1, 47)
mem.write_byte(2, 50)
mem.write_byte(3, 100)

mem.write_byte(4, 35)
mem.write_byte(5, 50)
mem.write_byte(6, 100)
# mem.write_byte(1, 2)
# mem.write_byte(2, 50)
# mem.write_byte(3, 2)
# mem.write_byte(4, 100)
# stop
mem.write_byte(7, 255)


clk.start([cpu])

print(f"{cpu.X} {cpu.Y}")
