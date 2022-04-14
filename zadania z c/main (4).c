#include <stdio.h>
#include <stdlib.h>
//Zad 5.2.3
int porownaj(char *nap,char *nap2)
{
    int i =0 ;
        while(nap[i] != '\0' )
        {
            if(nap[i] != nap2[i])
                return 0;
            i++;
        }
    return 1;
}
int porownaj2(wchar_t *nap,wchar_t *nap2)
{
    int i =0 ;
        while(nap[i] != '\0' )
        {
            if(nap[i] != nap2[i])
                return 0;
            i++;
        }
    return 1;
}
//Zad 5.2.5
int main()
{
    //Zad 5.2.3
    char a[10] = {'a','b','\0'};
    char b[10] = {'a','b','\0'};
    printf("%d\n",porownaj(a,b));

    wchar_t aa[10] = {'a','b','\0'};
    wchar_t bb[10] = {'c','b','\0'};
    printf("%d\n",porownaj2(aa,bb));
    //Zad 5.2.5
    return 0;
}
