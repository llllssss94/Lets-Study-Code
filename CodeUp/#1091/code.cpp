#include <iostream>
using namespace std;

int main(void){
	int a, m, d, n;
	long long int r;
	
	scanf("%d %d %d %d", &a, &m, &d, &n);
	
	r = a;
	
	for(int i = 1; i < n; i++){
		r = r * m + d;
	}
	
	cout << r << endl;
	
	return 0;	
}
