#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    char *s;
    s = malloc(1024 * sizeof(char));
    scanf("%[^\n]", s);
    s = realloc(s, strlen(s) + 1);
    // Define delimiter
    char delim[]= " ";
    // Use strtok
    char *ptr = strtok(s, delim);

    // While there are tokens left
    while (ptr != NULL)
    {        
        // Print token
        printf("%s\n", ptr);
        // Split again at the next delimiter
        ptr = strtok(NULL, delim);
    }
    // Deallocate s
    free(s);
    return 0;
}
