#include <stdio.h>
#define MAX 52

int a[MAX];
int b[MAX];
int c[MAX];
int d[MAX];
int ia, ib, ic, id;
int x,y,z,u;

int main(void){
for(ia = 1; ia <= 52; ++ia)
{
       a[ia] = (ia % 13);
       if(a[ia] == 0)
             a[ia] = 1;
}

for(ib = 1; ib <= 52; ++ib)
       b[ib] = (ib % 13);
       if(b[ib] == 0)
             b[ib] = 1;

for(ic = 1; ic <= 52; ++ic)
       c[ic] = (ic % 13);
       if(c[ic] == 0)
             c[ic] = 1;
       
for(id = 1; id <= 52; ++id)
       d[id] = (id % 13);
       if(d[id] == 0)
             d[id] = 1;


for(ia = 1; ia <= 52; ++ia)
{
       x = a[ia];
       for(ib = 1; ib <= 52; ++ib)
       {
              y = b[ib];
              for(ic = 1; ic <= 52; ++ic)
              {
                     z = c[ic];
                     for(id = 1; id < 52; ++id)
                            u = d[id];
                            if((x + y + z + u) == 24)
                             printf("%d\t%d\t%d\t%d\n",x, y, x, u);
               }       
       }
       
       
     
}
    
}
