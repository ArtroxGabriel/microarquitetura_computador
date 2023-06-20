import memory
from array import array

firmware = array('L', [0]) * 512

#! main: PC <- PC + 1; MBR <- read_byte(PC); goto MBR
firmware[0] =   0b000000000_100_00110101_001000_001_001

#! HALT - Instrução de parada
firmware[255] = 0b000000000_000_00000000_000000_000_000

#! X = X + memory[address]

##? 2: PC <- PC + 1; fetch; goto 3
firmware[2] = 0b000000011_000_00110101_001000_001_001

##? 3: MAR <- MBR; read_word(MAR); goto 4
firmware[3] = 0b000000100_000_00010100_100000_010_010

##? 4: H <- MDR; goto 5
firmware[4] = 0b000000101_000_00010100_000001_000_000

##? 5: X <- H + X; goto 0
firmware[5] = 0b000000000_000_00111100_000100_000_011


#! X = X - memory[address]

##? 6: PC <- PC + 1; fetch; goto 7
firmware[6] = 0b000000111_000_00110101_001000_001_001

##? 7: MAR <- MBR; read; goto 8
firmware[7] = 0b000001000_000_00010100_100000_010_010

##? 8: H <- MDR; goto 9
firmware[8] = 0b000001001_000_00010100_000001_000_000

##? 9: X <- X - H; goto 0
firmware[9] = 0b000000000_000_00111111_000100_000_011

#! memory[address] = X

##? 10: PC <- PC + 1; fetch; goto 11
firmware[10] = 0b00001011_000_00110101_001000_001_001

##? 11: MAR <- MBR; goto 12
firmware[11] = 0b00001100_000_00010100_100000_000_010

##? 12: MDR <- X; write; goto 0
firmware[12] = 0b00000000_000_00010100_010000_100_011

#! goto address 

##? 13: PC <- PC + 1; fetch; goto 14
firmware[13] = 0b00001110_000_00110101_001000_001_001

##? 14: PC <- MBR; fetch; goto MBR
firmware[14] = 0b00000000_100_00010100_001000_001_010

#! if X == 0 goto address

##? 15: X <- X; if alu = 0 goto 272 else goto 16
firmware[15] = 0b00010000_001_00010100_000100_000_011

##? 16: PC <- PC + 1; goto 0
firmware[16] = 0b00000000_000_00110101_001000_000_001

##? 272: goto 13
firmware[272]= 0b00001101_000_00000000_000000_000_000

# Registradores
MPC = 0
MIR = 0

MAR = 0
MDR = 0
PC  = 0
MBR = 0
X = 0
Y = 0
H = 0

N = 0
Z = 1

# Barramentos   
BAR_A = 0
BAR_B = 0
BAR_C = 0

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

    global MAR, BAR_C, MDR, PC, X, Y, H

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
        
            
def alu(bits_de_controle):

    global BAR_A, BAR_B, BAR_C, N, Z
    
    a = BAR_A 
    b = BAR_B
    o = 0
    
    shift_bits = bits_de_controle & 0b11000000
    shift_bits = shift_bits >> 6
    
    bits_de_controle = bits_de_controle & 0b00111111
    
    #* Seguindo a tabela do livro, bits_de_controle determina a operacao da ULA.
    if bits_de_controle == 0b011000: 
        o = a
    elif bits_de_controle == 0b010100:
        o = b
    elif bits_de_controle == 0b011010:
        o = ~a
    elif bits_de_controle == 0b101100:
        o = ~b
    elif bits_de_controle == 0b111100:
        o = a + b    
    elif bits_de_controle == 0b111101:
        o = a + b + 1
    elif bits_de_controle == 0b111001:
        o = a + 1
    elif bits_de_controle == 0b110101:
        o = b + 1
    elif bits_de_controle == 0b111111:
        o = b - a
    elif bits_de_controle == 0b110110:
        o = b - 1
    elif bits_de_controle == 0b111011:
        o = -a
    elif bits_de_controle == 0b001100:
        o = a & b
    elif bits_de_controle == 0b011100:
        o = a | b
    elif bits_de_controle == 0b010000:
        o = 0
    elif bits_de_controle == 0b110001:
        o = 1
    elif bits_de_controle == 0b110010:
        o = -1 
        
    if o == 0:
        N = 0
        Z = 1
    else:
        N = 1
        Z = 0
        
    if shift_bits == 0b01:
        o = o << 1
    elif shift_bits == 0b10:
        o = o >> 1
    elif shift_bits == 0b11:
        o = o << 8
        
    BAR_C = o
 

def next_instruction(next, jam):

    global MPC, MBR, N, Z
    
    if jam == 0b000:
        MPC = next
        return
        
    if jam & 0b001:                 # JAMZ
        next = next | (Z << 8)
        
    if jam & 0b010:                 # JAMN
        next = next | (N << 8)

    if jam & 0b100:                 # JMPC
        next = next | MBR
        
    MPC = next


def memory_io(mem_bits):

    global PC, MBR, MDR, MAR
    
    if mem_bits & 0b001:                # FETCH
       MBR = memory.read_byte(PC)
       
    if mem_bits & 0b010:                # READ
       MDR = memory.read_word(MAR)
       
    if mem_bits & 0b100:                # WRITE
       memory.write_word(MAR, MDR)
       
def step():
   
    global MIR, MPC
    
    MIR = firmware[MPC]
    
    if MIR == 0:
        return False    
    
    read_regs        ( MIR & 0b00000000000000000000000000000111)
    alu              ((MIR & 0b00000000000011111111000000000000) >> 12)
    write_regs       ((MIR & 0b00000000000000000000111111000000) >> 6)
    memory_io        ((MIR & 0b00000000000000000000000000111000) >> 3)
    next_instruction ((MIR & 0b11111111100000000000000000000000) >> 23,
                      (MIR & 0b00000000011100000000000000000000) >> 20)
                      
    return True