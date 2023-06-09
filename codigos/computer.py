import ufc2x as cpu
import memory as mem
import clock as clk

mem.write_word(50, 21) 
mem.write_word(100, 32)
mem.write_word(130, 10)

# X <- X + memory[50]
mem.write_byte(1, 2)      # X <- X + memory...
mem.write_byte(2, 50)     # ...[50]

# if X=0 goto 7
mem.write_byte(3, 15)
mem.write_byte(4, 7)

# X <- X + memory[100]
mem.write_byte(5, 2)      # X <- X + memory...
mem.write_byte(6, 100)    # ...[100]

# X <- X - memory[130]
mem.write_byte(7, 6)
mem.write_byte(8, 130)
    
# memory[150] = X
mem.write_byte(9, 10)
mem.write_byte(10, 150)    
    
# stop
mem.write_byte(11, 255)


clk.start([cpu])

print(mem.read_word(150))