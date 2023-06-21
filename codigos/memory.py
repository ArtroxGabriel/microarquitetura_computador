from array import array

# memória de 32 bits
memory = array("L", [0]) * ( (2 ** 18) - 1 )   # 1MB / 262.144 words / 1 word = 32 bits or 4 bytes

# acesso a memoria(leitura ou escrita), ignorar overflow

def read_word(endereco):
    # mascarando o endereco para 18 bits
    endereco = endereco & 0b111111111111111111
    return memory[endereco]

def write_word(endereco, valor):
    # mascarando o endereco para 18 bits
    endereco = endereco & 0b111111111111111111 
    # mascarando o valor para 32 bits
    valor = valor & 0xFFFFFFFF
    memory[endereco] = valor

def read_byte(endereco):
    #ler um determinado byte de uma palavra, em suma, divisao + o resto, vc descobre qual o by
    # determinar qual a palavra, por divisao.
    endereco = endereco & 0b11111111111111111111 # mascarando... em 20 bits
    end_word = endereco >> 2   # divisão por 4
    val_word = memory[end_word]

    # determinar o byte dentro da palavra, pelo resto.
    end_byte = endereco & 0b11   # resto da divisão por 4
    val_byte = val_word >> (end_byte << 3)
    val_byte = val_byte & 0xFF
    return val_byte

def write_byte(add,val):
    val = val & 0xFF                   # e.g. val = DD
    add = add & 0b11111111111111111111  # mascarando... em 20 bits
    end_word = add >> 2   # divisão por 4
    val_word = memory[end_word]        

    end_byte = add & 0b11   # resto da divisão por 4
    
    mask = ~(0xFF << (end_byte << 3))  
    val_word = val_word & mask         # 34004F33
    val = val << (end_byte << 3)       
 
    val_word = val_word | val          

    memory[end_word] = val_word
