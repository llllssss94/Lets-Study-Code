#include <iostream>

using namespace std;

int main(void){
	// 0���� �ʱ�ȭ 
	int cnt[23] = {0,};
	int num, i;
	
	// �� �� �θ��� 
	scanf("%d", &num);
	
	for(int j = 0; j < num; j++){
		scanf("%d", &i);
		// index�� 0���� 
		cnt[i-1]++;
	}
	
	// ���  
	for(int j = 0; j < 23; j++){
		printf("%d ", cnt[j]);
	}
	
	return 0;
}
