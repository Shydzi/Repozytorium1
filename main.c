#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
int nieparzyste=0;
int parzyste=0;
int najwieksza=0;
int ilosc=0;
const int N = 100;
srand(time(NULL));
int n = (rand()%N)+1;
int tab[n];
printf("wylosowana liczba n: %d\n",n);
for(int i=0;i<n;i++){

    int cos = (rand()%100)+1;
    tab[i]=cos;
    //=====podpunkt a======

    printf("wylosowana liczba cos: %d\n",cos);
    if(cos%2==1){
        tab[i]=3*cos+1;
        }
    else{
        tab[i]=cos;
    }
    //=====podpunkt b======

        printf("wylosowana liczba cos: %d\n",cos);
    if(cos%2==1){
        tab[i]=2*cos;
        }
    else{
        tab[i]=(cos)*-1;
    }
    if(tab[i]<0){
        tab[i]=-1;
    }
    else
    {
        tab[i]=1;
    }
}


//=====podpunkt c======

for(int i=0;i<n;i++){
    printf("%d\n",tab[i]);
}
unsigned int lewy = 2;
unsigned int prawy = 4;
for(int i=lewy;i<prawy+1;i++)
{
    for(int j=prawy;j>lewy;j--){
        int tymczasowa = tab[i];
        tab[i]=tab[j];
        tab[j]=tymczasowa;
}}
//=====podpunkt d======
for(int i=0;i<n;i++){

if(tab[i]%2==0){
    parzyste++;
}
else
{
    nieparzyste++;
}}

printf("nieparzyste:%d parzyste:%d",nieparzyste,parzyste);
//=====podpunkt d======


 for (int i = 0; i < n; ++i) {
    if (najwieksza < tab[i]) {
      najwieksza = tab[i];
    }
  }
   for (int i = 0; i < n; ++i){
        if(tab[i]==najwieksza)
        {
            ilosc++;
        }
   }
for(int i=0;i<n;i++){
    printf("%d\n",tab[i]);
}

    return 0;
}
