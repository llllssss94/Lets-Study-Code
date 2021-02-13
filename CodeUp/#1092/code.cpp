#include <iostream>

using namespace std;

int main(void){
	int a, b, c, cnt = 2;
	
	scanf("%d %d %d", &a, &b, &c);
	
	while((cnt % a) + (cnt % b) + (cnt % c) != 0){
		cnt++;
	}
	
	cout << cnt << endl;
	
	return 0;
}
