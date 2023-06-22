from array import array

# memória de 32 bits
memory = array("L", [0]) * (1024*1024//4)  # 1MB / 262.144 words (218) / 1 word = 32 bits or 4 bytes

# acesso a memoria(leitura ou escrita), ignorar overflow

def read_word(endereco):
    # mascarando o endereco para 18 bits
    endereco = endereco & 0b111111111111111111
    return memory[endereco]

def write_word(endereco, valor):
    # mascarando o endereco para 18 bits
    endereco = endereco & (2**18-1)
    # mascarando o valor para 32 bits
    valor = valor & 0xFFFFFFFF
    memory[endereco] = valor

def read_byte(endereco):
    #ler um determinado byte de uma palavra, em suma, divisao + o resto, vc descobre qual o by
    # determinar qual a palavra, por divisao.
    endereco = endereco & 0b1111111111111111111 # mascarando... em 20 bits
    end_word = endereco >> 2   # divisão por 4
    val_word = memory[end_word]

    # determinar o byte dentro da palavra, pelo resto da divisao
    end_byte = endereco & 0b11   # resto da divisão por 4
    val_byte = val_word >> (end_byte << 3)
    val_byte = val_byte & 0xFF
    return val_byte

def write_byte(endereco,valor):
    valor = valor & 0xFF                   
    endereco = endereco & 0b1111111111111111111  # mascarando em 20 bits
    end_word = endereco >> 2   # divisão por 4
    val_word = memory[end_word]        

    end_byte = endereco & 0b11   # resto da divisão por 4
    
    mask = ~(0xFF << (end_byte << 3))  
    val_word = val_word & mask         

    valor = valor << (end_byte << 3)
 
    val_word = val_word | valor

    memory[end_word] = val_word

