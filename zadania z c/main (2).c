#include <stdio.h>
#include <stdlib.h>
#include <string.h>
//Zad 5.2.24
void kopiuj(char *nap1,char *nap2)
{
    strcpy(nap2,nap1);
}

void kopiuj2(wchar_t *nap1,wchar_t *nap2)
{
    wcscpy(nap2,nap1);
}
int main()
{
    //Zad 5.2.24
    char a[10] = "Cos";
    char b[10] = {};
    printf("%s\n%s\n",a,b);
    kopiuj(a,b);
    printf("%s\n%s\n",a,b);
    printf("\n\n");

    wchar_t aa[10] = {'c','g','c','d','c','\0'};
    wchar_t bb[10] = {};
    printf("%ls\n%ls\n",aa,bb);
    kopiuj2(aa,bb);
    printf("%ls\n%ls\n",aa,bb);
    return 0;
}
