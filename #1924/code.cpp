#include <stdio.h>
#include <iostream>

using namespace std;

int main(void){
	int m, d, i, date_sum = 0;
	
	// ���ǹ� ��� ����Ʈ ���
	string days[7] = {"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};
	
	// �� ���� ���� 
	int dates[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
	
	
	// �Է� 
	scanf("%d %d", &m, &d);
	
	// ���� ��¥ �ջ� 
	for(int i = 0; i < m - 1; i++){
		date_sum += dates[i];
	}
	
	// ���� ���� �ջ� 
	date_sum += d;
	
	// ������ ��� �� �ε����� ����Ͽ� ���
	cout << days[int(date_sum % 7)] << endl;
	
		
}
