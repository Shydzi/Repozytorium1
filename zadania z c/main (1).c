#include <stdio.h>
#include <stdlib.h>
//Zad 5.2.6
void kopiujn(char *nap1,char *nap2, int n)
{

    for (int i=0;i<n;i++)
    {
        if (nap1[i]!='\0')
            nap2[i] = nap1[i];
        else
        {
            nap2[i]='\0';
            break;
        }

    }
}

void kopiujn2(wchar_t *nap1,wchar_t *nap2, int n)
{

    for (int i=0;i<n;i++)
    {
        if (nap1[i]!='\0')
            nap2[i] = nap1[i];
        else
        {
            nap2[i]='\0';
            break;
        }

    }
}

int main()
{
    //Zad 5.2.6
    char a[10] = {'c','g','c','d','c','\0'};
    char b[10] = {};
    int n = 2;
    printf("%s\n%s\n",a,b);
    kopiujn(a,b,n);
    printf("%s\n%s\n",a,b);
    printf("\n\n");

    wchar_t aa[10] = {'a','b','c','d','e','\0'};
    wchar_t bb[10] = {};
    printf("%ls\n%ls\n",aa,bb);
    kopiujn2(aa,bb,n);
    printf("%ls\n%ls\n",aa,bb);
    printf("\n\n");

}
