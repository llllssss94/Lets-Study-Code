#include <iostream>

using namespace std;

int main(void){
	int num, i = 0, sum = 0;
	
	scanf("%d", &num);
	
	while(sum < num){
		i++;
		sum += i;
	}
	
	cout << sum << endl;
	
	return 0;
}
