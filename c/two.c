#include <stdio.h>
/* c *2  */
int main(void){
int c,f;
int min,max,step;

min = 0;
step = 2;
max = 50;
c = min;
while(c<=max){
                f = c * 234;
                printf("c=%d\tc*2=%d\n",c,f);
                c = c + step;
}
return 0;
}
/*
学习笔记:

if 只执行一回,while却一直执行,只到不满足条件.
 
函数引用今天直接用的一个变量名没有搞定,后面再学. 



*/







