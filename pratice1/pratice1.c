#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int argc, char* argv[])
{
    char buf[20];
    printf("Enter password :");
    gets(buf);
    srand(time(0) ^ getpid());
    int magic = rand();
    if(atoi(buf) == magic)
        system("/bin/sh");
    else
        puts("Wrong !!");
}
