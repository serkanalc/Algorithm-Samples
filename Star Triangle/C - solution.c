#include <stdio.h>

int main() {
    int bosluk = 5;
    int yildiz = 1;
    
    for(int i = bosluk; i >= 0; i--) {
        for(int j = i; j > 0; j--) {
            printf(" ");
        }
        
        for(int j = 0; j < yildiz; j++) {
            printf("*");
        }
        yildiz += 2;
        printf("\n");
    }
    return 0;
}
