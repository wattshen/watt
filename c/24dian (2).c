/* 
*
* title:任意四张扑克通过加减乘除等于24 
* date: 20140613
* auther:Watt Shen
*
* by:穷举for 
* desicribetion:未实现. 
*               碰到数组值相加的问题 
*               碰到多值相加的问题 
*               数组输出使用%d还是其它? 
*               数组能否",分隔",一行声明多个?
*               为什么条件是==24,出来的结果却是什么都有? 
*/

#include <stdio.h>
#define MAX 52
int a[MAX];
int b[MAX];
int c[MAX];
int d[MAX];
int ia, ib, ic, id;
int x,y,z,u,v;

int main(void){

for(ia = 1; ia <= 52; ++ia)
{
        a[ia] = (ia % 13);
        if(a[ia] == 0)
                a[ia] = 13;
        x = a[ia];
       
       for(ib = 1; ib <= 52; ++ib)
       {
              b[ib] = (ib % 13);
              if(b[ib] == 0)
                       b[ib] = 13;
              y = b[ib];
              for(ic = 1; ic <= 52; ++ic)
              {
                     c[ic] = (ic % 13);
                     if(c[ic] == 0)
                              c[ic] = 13;
                     z = c[ic];
                     for(id = 1; id < 52; ++id)
                     {
                            d[id] = (id % 13);
                            if(d[id] == 0)
                                     d[id] = 13;
                            u = d[id];
                            v = 0;
                            v = x + y - z + u;
                            if(v == 24)
                            printf("%d\t%d\t%d\t%d\n",x, y, z, u);
                     }
               }       
       }    
}
    
}
