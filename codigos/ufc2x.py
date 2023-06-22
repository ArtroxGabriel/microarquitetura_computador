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

# funcoes pros registradores
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

# ULA
def ula(bits_de_controle):
    global N, Z, BAR_A, BAR_B, BAR_C
    
    A = BAR_A
    B = BAR_C
    saida = 0
    
    deslocador = (bits_de_controle & 0b11000000) >> 6
    
    funcoes = bits_de_controle & 0b00111111

    if funcoes == 0b011000:
        saida = A
    elif funcoes == 0b010100:
        saida = B
    elif funcoes == 0b011010:
        saida = ~A
    elif funcoes == 0b101100:
        saida = ~B 
    elif funcoes == 0b111100:
        saida = A + B
    elif funcoes == 0b111101:
        saida = A + B + 1
    elif funcoes == 0b111001:
        saida = A + 1
    elif funcoes == 0b110101:
        saida = B + 1
    elif funcoes == 0b111111:
        saida = B - A
    elif funcoes == 0b110110:
        saida = B - 1
    elif funcoes == 0b111011:
        saida = -A
    elif funcoes == 0b001100:
        saida = A & B
    elif funcoes == 0B011100:
        saida = A | B
    elif funcoes == 0b010000:
        saida = 0
    elif funcoes == 0b110001:
        saida = 1
    elif funcoes == 0b110010:
        saida = -1 
    
    if saida == 0:
        N = 0
        Z = 1
    else:
        N = 1
        Z = 0
    
    if deslocador == 0b01:
        saida = saida << 1
    elif deslocador == 0b10:
        saida = saida >> 1
    elif deslocador == 0b11:
        saida = saida << 8

    BAR_C = saida

# MPC
def next_instruction(next, jam):
    global MPC, MBR, N, Z

    if jam == 0b000:
        MPC = prox
        return
    if jam & 0b001:
        prox = prox | (Z << 8)
    if jam & 0b010:
        prox = prox | (N << 8)
    if jam & 0b100:
        prox = prox | MBR
    MPC = prox

# input e output da memoria
def memoryIO(bits):
    global PC, MBR, MDR, MAR

    if bits & 0b001:
        #fetch
        MBR = memory.read_byte(PC)
    if bits & 0b010:
        #read
        MDR = memory.read_word(MAR)
    if bits & 0b100:
        #write
        memory.write_word(MAR, MDR)

def step():
    global MIR, MPC

    MIR = firmware[MPC]

    if MIR == 0:
        return False
    