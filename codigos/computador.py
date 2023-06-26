"""Computador com CPU e memória."""
import sys
import cpu
import memory as mem
import clock as clk
import disk

disk.read(str(sys.argv[1]))


print("====================================")
clk.start([cpu])

print("------------------------------------")

print(f"Resultado: {mem.read_word(1)}")

print("====================================")
