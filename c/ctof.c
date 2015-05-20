#include <stdio.h>
/*c to f*/
int main(void){
    float c,f;
    int step = 20,min = 0,max = 300;
    f = 300;
    
    printf("\nThe below is f to c\n");
    while(f >= min){
        c=(5.0 /9.0)*(f - 32.0);
        f = f - step;
        printf ("%6.1f\t%3f\n",f,c);    
    }
    return 0;
}
