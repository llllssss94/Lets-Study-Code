#include <iostream>

using namespace std;

int main(void){
	int a, d, n, r;
	
	scanf("%d %d %d", &a, &d, &n);
	
	r = a + (n-1) * d;
	
	cout << r << endl;
	
	return 0;
}
