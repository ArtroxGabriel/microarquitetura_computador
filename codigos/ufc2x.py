import memory 
from array import array

# REGISTRADORES
MPC = 0
MIR = 0

MAR = 0
MDR = 0
PC = 0
MBR = 0
X = 0
Y = 0
H = 0

N = 0
Z = 1

# BARRAMENTOS
BAR_C = 0
BAR_B = 0
BAR_A = 0

# Armazenamento de controle:
firmware = array('L', [0] ) * 512

def read_regs(reg_num):
    global MDR, PC, MBR, X, Y, H, BAR_A, BAR_B

    BAR_A = H

    if reg_num == 0:
        BAR_B = MDR
    elif reg_num == 1:
        BAR_B = PC
    elif reg_num == 2:
        BAR_B = MBR
    elif reg_num == 3:
        BAR_B = X
    elif reg_num == 4:
        BAR_B = Y
    else:
        BAR_B = 0

def write_regs(reg_bits):
    global MAR, MDR, PC, X, Y, H, BAR_C

    if reg_bits & 0b100000:
        MAR = BAR_C
    if reg_bits & 0b010000:
        MDR = BAR_C
    if reg_bits & 0b001000:
        PC = BAR_C
    if reg_bits & 0b000100:
        X = BAR_C
    if reg_bits & 0b000010:
        Y = BAR_C
    if reg_bits & 0b000001:
        H = BAR_C

def ula(bits_de_controle):
    global N, Z, BAR_A, BAR_B, BAR_C
    
    a = BAR_A
    B = BAR_C
    saida = 0
    
    
