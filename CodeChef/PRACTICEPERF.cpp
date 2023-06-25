#include <iostream>
using namespace std;

int main() {
	int n = 4, p, count = 0;
	
	while(n != 0){
	    cin >> p;
	    if (p >= 10){
	        count ++;
	    }
	    
	    n--;
	}
	
	cout << count;
	
	return 0;
}
