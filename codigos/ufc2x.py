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
        BUS_B = MDR
    elif reg_num == 1:
        BUS_B = PC
    elif reg_num == 2:
        BUS_B = MBR
    elif reg_num == 3:
        BUS_B = X
    elif reg_num == 4:
        BUS_B = Y
    else:
        BUS_B = 0