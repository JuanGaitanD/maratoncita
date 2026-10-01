#include <iostream>
void bubblesort(int [], size_t);
void imprimirArreglo(int [], size_t);

int main()
{
    int lista[10] = {6, 5, 1, 3, 6, 6, 3, 2, 53, 12};
    size_t len = sizeof(lista) / sizeof(lista[0]);
    
    bubblesort(lista, len);
    imprimirArreglo(lista, len);

    return 0;
}

void imprimirArreglo(int a[], size_t len) {
    for (int i = 0; i < len; i++) {
        std::cout << a[i] << ", ";
    }
    
    std::cout << "\n";
}

void bubblesort(int a[], size_t len) {
    int i, j, temp;
    
    for (i=0; i < len-1; i++) {
        for (j=0; j < len-i-1; j++){
            temp = 0;
            
            if (a[j] > a[j+1]) {
                temp = a[j];
                a[j] = a[j+1];
                a[j+1] = temp;
            }
        }
    }
}