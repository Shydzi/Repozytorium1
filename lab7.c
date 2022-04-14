#include <stdio.h>
#include <stdlib.h>
#include <string.h>
// 5.2.3,
/*int porownaj( char *nap1, char * nap2){
int i;
int licznik=0;
for(i=0;i<=strlen(nap1);i++)
    if(nap1[i]==nap2[i])
        {licznik++;

        }
    else
        {licznik=0;}

    if(licznik>0)
    {
        return 1;
    }else
    {
        return 0;
    }

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
}*/
// 5.2.5
/*
void przepisz(char *nap,char *nap2)
{
    int i =0 ;
        while(nap[i] != '\0' )
        {
            nap2[i+strlen(nap)] = nap[i];
            i++;
        }
}
void przepisz2(wchar_t *nap, wchar_t *nap2)
{
    int i =0 ;
        while(nap[i] != '\0' )
        {
            nap2[i+strlen(nap)+1] = nap[i];
            i++;
        }
}*/
//5.2.6
/*
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
*/
// 5.2.24
/*
void kopiuj(char *nap1,char *nap2)
{
    strcpy(nap2,nap1);
}

void kopiuj2(wchar_t *nap1,wchar_t *nap2)
{
    wcscpy(nap2,nap1);
}
*/
//5.2.25

void kopiuj(char *nap,char **napw)
{
    char tab[10]={};
    strcpy(tab,nap);
    napw = &tab;
    return napw;
}
void kopiuj2(wchar_t *nap,wchar_t **napw)
{
    char tab[10]={};
    strcpy(tab,nap);
    napw = &tab;
    return napw;
}
int main()
{
  //5.2.3
   /* printf("%d",porownaj("napis","napisa"));
    wchar_t aa[10] = {'a','b','\0'};
    wchar_t bb[10] = {'c','b','\0'};
    printf("%d\n",porownaj2(aa,bb));*/
    //5.2.5
    /*
    char a[10] = {'a','b','\0'};
    char b[10] = {'c','d','\0'};
    przepisz(a,b);
    printf("%s\n%s\n",a,b);
    printf("\n\n");

    wchar_t aa[10] = {'a','b','\0'};
    wchar_t bb[10] = {'c','d','\0'};
    przepisz2(aa,bb);
    printf("%ls\n%ls\n",aa,bb);*/
      //Zad 5.2.6
   /* char a[10] = {'l','o','l','o','l','\0'};
    char b[10] = {};
    int n = 2;
    kopiujn(a,b,n);
    printf("%s\n%s\n",a,b);
    printf("\n\n");

    wchar_t aa[10] = {'l','o','l','o','l','\0'};
    wchar_t bb[10] = {};
    kopiujn2(aa,bb,n);
    printf("%ls\n%ls\n",aa,bb);
    printf("\n\n");*/
        //Zad 5.2.24
    /*
    char a[10] = "Cos";
    char b[10] = {};
    kopiuj(a,b);
    printf("%s\n%s\n",a,b);
    printf("\n\n");

    wchar_t aa[10] = {'l','o','l','o','l','\0'};
    wchar_t bb[10] = {};
    kopiuj2(aa,bb);
    printf("%ls\n%ls\n",aa,bb);*/
    //5.2.25
    char a[10] = "Cos";
    char b[10] = {};
    printf("%s\n%s\n",a,b);
    kopiuj(a,b);
    printf("%s\n%s\n",a,b);
    printf("\n\n");

    wchar_t aa[10] = {'l','o','l','o','l','\0'};
    wchar_t bb[10] = {};
    printf("%ls\n%ls\n",aa,bb);
    kopiuj2(aa,bb);
    printf("%ls\n%ls\n",aa,bb);

    return 0;
}
