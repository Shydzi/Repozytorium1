#include <stdio.h>
#include <stdlib.h>
#include <string.h>
//Zad 5.2.25
void kopiuj(char *nap,char **napw)
{
    char tab[10]={};
    strcpy(tab,nap);
    napw = &tab;
}
int main()
{
    //Zad 5.2.25
    return 0;
}
