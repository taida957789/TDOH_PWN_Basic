CC = gcc
CFLAGS = -m32 -fno-stack-protector
BIN=./bin

all: bypassASLR
%: %.c
	$(CC) $(CFLAGS) $^ -o $@

clean:
	find -type f -perm -0111 | xargs rm
