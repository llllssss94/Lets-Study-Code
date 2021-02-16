#include <iostream>

using namespace std;

int main(void){
	int h, m, sum;
	
	scanf("%d %d", &h, &m);
	
	sum = h * 60 + m;
	
	if(sum < 45){
		cout << 23 << " " << (15 + sum) << endl;
		return 0;
	}
	
	sum -= 45;
	cout << (sum / 60) << " " << (sum % 60) << endl;
	
	return 0;
}
