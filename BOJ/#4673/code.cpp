#include <iostream>
#include <vector>

using namespace std;

int recursive(int a){
	int sum = a;
	
	// 자릿수 반복하며 더하기 
	while(a > 0){
		sum += (a % 10);
		a = a / 10;
	}
	 
	return sum;
}

int main(void){
	int count[10001] = {0,};
	int temp;
	
	// 1부터 10000까지 
	for(int i = 1; i < 10001; i++){
		temp = recursive(i);
		// 하나의 수에서 만들 수 있는 10000 이하의 수 카운트 
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
