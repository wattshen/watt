#include <stdio.h>
/* f to c */
int main(void){
float c,f;
int min,max,step;

min = 0;
max = 300;
step = 20;
f = min;
printf("\nThis is c to f change, look!\n");
while(f <= max){
c = (5.0 / 9.0) * (f - 32.0);
printf("%3.0f\t%7.3f\n",f,c);
f = f + step;
}

return 0;
}

