// Con t minutos desde las 12: hora = t/2 grados y minuto = 6t mod 360. Asi t = 2h y basta 12h mod 360 == m.
#include <bits/stdc++.h>
int main() {
    int h, m;
    std::cin >> h >> m;
    puts(12 * h % 360 == m ? "yes" : "no");
}
