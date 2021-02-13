#include <iostream>

using namespace std;

int main(void){
	int num, call;
	// 최대 인풋 10000까지  
	int input[10001] = {0,};
	
	scanf("%d", &num);
	
	// 히스토리 저장 
	for(int j = 0; j < num; j++){
		scanf("%d", &call);
		input[j] = call;
	}
	
	// 역순 조회 
	for(int j = num-1; j >= 0; j--){
		cout << input[j] << " ";
	}
	cout << endl;
	
	return 0;
} 
