CC = gcc
CFLAGS = -m32 -fno-stack-protector -z execstack
BIN=./bin

all: pratice2
%: %.c
	$(CC) $(CFLAGS) $^ -o $@

clean:
	find -type f -perm -0111 | xargs rm
