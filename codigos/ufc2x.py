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
BAR_A = 0
BAR_B = 0
BAR_C = 0

# Armazenamento de controle
firmware = array("L", [0]) * 512

firmware[0] = 0b000000001_000_00000000_000000_010_000
### H = MDR  GOTO 2
firmware[1] = 0b000000010_000_00010100_000001_000_000
### MAR = 1 GOTO 3
firmware[2] = 0b000000011_000_00110001_100000_000_000
### MDR = memory[MAR] GOTO 4
firmware[3] = 0b000000100_000_00000000_000000_010_000
### MDR = H + MDR GOTO 5
firmware[4] = 0b000000101_000_00111100_010000_000_000
### X = 1 GOTO 6
firmware[5] = 0b000000110_000_00110001_000100_000_000
### X = X + 1 GOTO 7
firmware[6] = 0b000000111_000_00110101_000100_000_011
### X = X + 1 GOTO 8
firmware[7] = 0b000001000_000_00110101_000100_000_011
### MAR = X  GOTO 9
firmware[8] = 0b000001001_000_00010100_100000_000_011
### memory[MAR] = MDR GOTO10
firmware[9] = 0b000001010_000_00000000_000000_100_000


# leitura do registrador
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


# escrita do registrador
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
    global BAR_A, BAR_B, BAR_C, N, Z

    A = BAR_A
    B = BAR_B
    saida = 0

    deslocador = bits_de_controle & 0b11000000
    deslocador = deslocador >> 6

    bits_de_controle = bits_de_controle & 0b00111111

    if bits_de_controle == 0b011000:
        saida = A
    elif bits_de_controle == 0b010100:
        saida = B
    elif bits_de_controle == 0b011010:
        saida = ~A
    elif bits_de_controle == 0b101100:
        saida = ~B
    elif bits_de_controle == 0b111100:
        saida = A + B
    elif bits_de_controle == 0b111101:
        saida = A + B + 1
    elif bits_de_controle == 0b111001:
        saida = A + 1
    elif bits_de_controle == 0b110101:
        saida = B + 1
    elif bits_de_controle == 0b111111:
        saida = B - A
    elif bits_de_controle == 0b110110:
        saida = B - 1
    elif bits_de_controle == 0b111011:
        saida = -A
    elif bits_de_controle == 0b001100:
        saida = A & B
    elif bits_de_controle == 0b011100:
        saida = A | B
    elif bits_de_controle == 0b010000:
        saida = 0
    elif bits_de_controle == 0b110001:
        saida = 1
    elif bits_de_controle == 0b110010:
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


# Prox e Jam
def next_instruction(prox, jam):
    global MPC, MBR, N, Z

    if jam == 0b000:
        MPC = prox
        return

    if jam & 0b001:  # JAMZ
        prox = prox | (Z << 8)

    if jam & 0b010:  # JAMN
        prox = prox | (N << 8)

    if jam & 0b100:  # JMPC
        prox = prox | MBR

    MPC = prox


# input e output da memoria
def memory_io(mem_bits):
    global PC, MBR, MDR, MAR

    if mem_bits & 0b001:  # FETCH
        MBR = memory.read_byte(PC)

    if mem_bits & 0b010:  # READ
        MDR = memory.read_word(MAR)

    if mem_bits & 0b100:  # WRITE
        memory.write_word(MAR, MDR)


def step():
    global MIR, MPC

    MIR = firmware[MPC]

    if MIR == 0:
        return False

    read_regs(MIR & 0b00000000000000000000000000000111)
    ula((MIR & 0b00000000000011111111000000000000) >> 12)
    write_regs((MIR & 0b00000000000000000000111111000000) >> 6)
    memory_io((MIR & 0b00000000000000000000000000111000) >> 3)
    next_instruction(
        (MIR & 0b11111111100000000000000000000000) >> 23,
        (MIR & 0b00000000011100000000000000000000) >> 20,
    )

    return True
