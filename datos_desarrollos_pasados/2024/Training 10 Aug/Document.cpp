#include <iostream>
#include <string>
#include <algorithm>
#include <sstream>
#include <vector>
#include <math.h>
using namespace std;

int main()
{
   int cantidad;
   int alto, suma;
   cin >> cantidad;
   string palabras[cantidad];
   int largo = 0;
   int c_letras = 0;
   
   for(int i=0; i<cantidad; i++){
       cin >> palabras[i];
       c_letras += palabras[i].size()+1;
       if(largo == 0){
           largo = palabras[i].size()+1;
       }else if(largo < palabras[i].size()){
           largo = palabras[i].size()+1;
       }
   }
   
   c_letras += cantidad;
   alto =c_letras / largo;
   suma = alto + largo;
   
    cout << suma;
   
  
}

