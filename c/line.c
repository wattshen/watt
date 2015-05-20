#include <stdio.h>
/* 统计输入内容的单词数 字符数 行数 */

int c,nl,nw,nc,state;
#define IN 1/* 在单词内 */
#define OUT 0/* 在单词外 */ 

int main(void){
    state = OUT;
    nl = 1;
    nw = nc =0;
    while((c = getchar()) != EOF){
            ++nc;
        if(c == '\n')
                ++nl;
        if(c ==' '||c == '\t'||c == '\n')
                state = OUT;
        else if(state == OUT){
                state = IN;
                ++nw;        
        }
    }
    printf("%d\t%d\t%d\n",nl,nw,nc);
/*printf("\nnl is %d\nnw is %d\nnc is %d\n",nl,nw,nc);*/
return 0;
}
 
