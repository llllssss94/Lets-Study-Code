#include <iostream>

using namespace std;

int main(void){
	int year;
	
	scanf("%d", &year);
	
	if(year % 4 == 0){
		if(year % 100 != 0){
			cout << 1 << endl;
			return 0;
		}
		else if(year % 400 == 0){
			cout << 1 << endl;
			return 0;
		}
	}
	cout << 0 << endl;
	
	return 0;
}
