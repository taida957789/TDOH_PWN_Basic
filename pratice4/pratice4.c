#include <stdio.h>
#include <stdlib.h>

int main(int argc, char*argv[]) {

    puts("HaHa I have DEP");
    fflush(stdout);

    char name[40];

    printf("What's your name ? ");
    fflush(stdout);
    scanf("%s", &name);

    return EXIT_SUCCESS;
}
