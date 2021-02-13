#include <iostream>

using namespace std;

int main(void){
	// 0으로 초기화 
	int cnt[23] = {0,};
	int num, i;
	
	// 몇 번 부를겨 
	scanf("%d", &num);
	
	for(int j = 0; j < num; j++){
		scanf("%d", &i);
		// index는 0부터 
		cnt[i-1]++;
	}
	
	// 출력  
	for(int j = 0; j < 23; j++){
		printf("%d ", cnt[j]);
	}
	
	return 0;
}
