#include <iostream>
#include <vector>

using namespace std;

int recursive(int a){
	int sum = a;
	
	// �ڸ��� �ݺ��ϸ� ���ϱ� 
	while(a > 0){
		sum += (a % 10);
		a = a / 10;
	}
	 
	return sum;
}

int main(void){
	int count[10001] = {0,};
	int temp;
	
	// 1���� 10000���� 
	for(int i = 1; i < 10001; i++){
		temp = recursive(i);
		// �ϳ��� ������ ���� �� �ִ� 10000 ������ �� ī��Ʈ 
		while(temp <= 10000){
			count[temp]++;
			temp = recursive(temp);
		}
	}
	
	for(int i = 1; i < 10001; i++){
		if(count[i] == 0) cout << i << "\n";
	}
	
	return 0;	
}
