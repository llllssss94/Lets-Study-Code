#include <iostream>

using namespace std;

int main(void){
	int num, input;
	// ��ȣ ���� 1~23
	int min = 24;
	
	scanf("%d", &num);
	
	for(int i = 0; i < num; i++){
		scanf("%d", &input);
		
		// ���� �ּҿ� ���ؼ� ���ο� ���� �������� ������Ʈ 
		if(input < min) min = input;
	}
	
	cout << min << endl;
	
	return 0;
}
