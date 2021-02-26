#include <iostream>
#include <vector>

using namespace std;

bool check(int a){
	// 1의 자리 수 
	int t = a % 10; 
	int d;
		
	// 자릿수 삭제 
	a = a / 10;
	// 처음 두 자리로 공차 계산
	d = t - (a % 10);
	
	// 한자릿수가 되면 끝난거임 
	while(a >= 10){
		
		// t에 다음 수 넣고 
		t = a % 10;
		// 자릿수 삭제 
		a = a / 10;
		// 다음 자리와 차이를 구해서 공차와 같은지 확인 
		if(d != t - (a % 10)){
			// 다르면 한수가 아님 
			return false; 
		};
	}
	
	// 끝까지 통과한 경우 한수인 것임 
	return true;
}

int main(void){
	int num, cnt = 0;
	
	cin >> num;
	
	for(int i = 1; i <= num; i++){
		if(check(i)){
			cnt++;
		}
	}
	
	cout << cnt << "\n";
	
	return 0;
}
