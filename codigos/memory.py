"""Memoria"""
from array import array

# memória de 32 bits
memory = array("L", [0]) * (2**18)


def read_word(endereco):
    """! leitura de uma palavra da memoria"""

    endereco = endereco & 0b111111111111111111
    return memory[endereco]


def write_word(endereco, valor):
    """! escrita de uma palavra na memoria"""

    endereco = endereco & (2**18 - 1)

    valor = valor & 0xFFFFFFFF
    memory[endereco] = valor


def read_byte(endereco):
    """! leitura de um byte da memoria"""

    endereco = endereco & 0b1111111111111111111
    end_word = endereco >> 2
    val_word = memory[end_word]

    end_byte = endereco & 0b11
    val_byte = val_word >> (end_byte << 3)
    val_byte = val_byte & 0xFF
    return val_byte


def write_byte(endereco, valor):
    """! escrita de um byte na memoria"""

    valor = valor & 0xFF
    endereco = endereco & 0b1111111111111111111
    end_word = endereco >> 2
    val_word = memory[end_word]

    end_byte = endereco & 0b11

    mask = ~(0xFF << (end_byte << 3))
    val_word = val_word & mask

    valor = valor << (end_byte << 3)

    val_word = val_word | valor

    memory[end_word] = val_word
