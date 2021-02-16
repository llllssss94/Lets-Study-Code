#include <iostream>

using namespace std;

int main(void){
	int num, sum = 0;
	
	scanf("%d", &num);
	
	for(int i = 1; i <= num; i++){
		sum += i;
	}
	
	cout << sum << endl;
	
	return 0;
}
