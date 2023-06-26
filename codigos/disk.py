"""Disco"""
import memory as mem


def read(img):
    """Lê um arquivo de imagem de disco e carrega na memória."""
    disk = open(img, "rb")
    byte = disk.read(1)
    byte_address = 0
    while byte:
        mem.write_byte(byte_address, int.from_bytes(byte, "little"))
        byte = disk.read(1)
        byte_address += 1
    disk.close()
