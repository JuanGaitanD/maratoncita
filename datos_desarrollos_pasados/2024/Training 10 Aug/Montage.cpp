#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

string can_arrange(int n, int w, vector<int>& alturas) {
    
    sort(alturas.begin(), alturas.end());

    for (int i = 0; i < n - w; i += w) {
     
        int last_person_current_row = alturas[i + w - 1];
    
        int first_person_next_row = alturas[i + w];
        
        if (last_person_current_row >= first_person_next_row) {
            return "no";
        }
    }
    
    return "yes";
}

int main() {
    int n, w;
    cin >> n >> w;
    
    vector<int> alturas(n);
    for (int i = 0; i < n; ++i) {
        cin >> alturas[i];
    }
    
    string result = can_arrange(n, w, alturas);
    cout << result;
    
    return 0;
}