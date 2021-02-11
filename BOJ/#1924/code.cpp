#include <stdio.h>
#include <iostream>

using namespace std;

int main(void){
	int m, d, i, date_sum = 0;
	
	// 조건문 대신 리스트 사용
	string days[7] = {"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};
	
	// 각 월별 일자 
	int dates[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
	
	
	// 입력 
	scanf("%d %d", &m, &d);
	
	// 월별 날짜 합산 
	for(int i = 0; i < m - 1; i++){
		date_sum += dates[i];
	}
	
	// 남은 일자 합산 
	date_sum += d;
	
	// 나머지 계산 후 인덱스로 사용하여 출력
	cout << days[int(date_sum % 7)] << endl;
	
		
}
