#include <stdio.h>
#include <stdlib.h>


int main(int argc, char* argv[])
{
    char buf[20];
    puts("What's your name? ");
    fflush(stdout);
    scanf("%s", &buf);
    printf("Hi ~ %s", buf);
    fflush(stdout);
}
