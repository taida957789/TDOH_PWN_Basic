CC = gcc
CFLAGS = -m32 -fno-stack-protector -static
BIN=./bin

all: pratice4
%: %.c
	$(CC) $(CFLAGS) $^ -o $@

clean:
	find -type f -perm -0111 | xargs rm
