#include <iostream>

using namespace std;

int main(void){
	int num, input;
	// 번호 범위 1~23
	int min = 24;
	
	scanf("%d", &num);
	
	for(int i = 0; i < num; i++){
		scanf("%d", &input);
		
		// 이전 최소와 비교해서 새로운 값이 더작으면 업데이트 
		if(input < min) min = input;
	}
	
	cout << min << endl;
	
	return 0;
}
