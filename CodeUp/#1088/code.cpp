#include <iostream>

using namespace std;

int main(void){
	int num;
	
	scanf("%d", &num);
	
	for(int i = 0; i <= num; i++){
		if(i % 3 != 0){
			printf("%d ", i);
		}
	}
	
	return 0;
}
