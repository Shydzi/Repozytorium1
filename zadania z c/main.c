#include <stdio.h>
#include <stdlib.h>
//Zad 5.2.5
void przepisz(char *nap,char *nap2)
{
    int i =0 ;
        while(nap[i] != '\0' )
        {
            nap2[i] = nap[i];
            i++;
        }
}
void przepisz2(wchar_t *nap, wchar_t *nap2)
{
    int i =0 ;
        while(nap[i] != '\0' )
        {
            nap2[i] = nap[i];
            i++;
        }
}
int main()
{
    //Zad 5.2.5
    char a[10] = {'c','g','\0'};
    char b[10] = {'a','b','\0'};
    printf("%s\n%s\n",a,b);
    przepisz(a,b);
    printf("%s\n%s\n",a,b);
    printf("\n\n");

    wchar_t aa[10] = {'c','g','\0'};
    wchar_t bb[10] = {'a','b','\0'};
    printf("%ls\n%ls\n",aa,bb);
    przepisz2(aa,bb);
    printf("%ls\n%ls\n",aa,bb);
    return 0;
}
