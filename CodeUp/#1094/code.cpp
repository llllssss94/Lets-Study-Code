#include <iostream>

using namespace std;

int main(void){
	int num, call;
	// �ִ� ��ǲ 10000����  
	int input[10001] = {0,};
	
	scanf("%d", &num);
	
	// �����丮 ���� 
	for(int j = 0; j < num; j++){
		scanf("%d", &call);
		input[j] = call;
	}
	
	// ���� ��ȸ 
	for(int j = num-1; j >= 0; j--){
		cout << input[j] << " ";
	}
	cout << endl;
	
	return 0;
} 
