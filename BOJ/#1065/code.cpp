#include <iostream>
#include <vector>

using namespace std;

bool check(int a){
	// 1�� �ڸ� �� 
	int t = a % 10; 
	int d;
		
	// �ڸ��� ���� 
	a = a / 10;
	// ó�� �� �ڸ��� ���� ���
	d = t - (a % 10);
	
	// ���ڸ����� �Ǹ� �������� 
	while(a >= 10){
		
		// t�� ���� �� �ְ� 
		t = a % 10;
		// �ڸ��� ���� 
		a = a / 10;
		// ���� �ڸ��� ���̸� ���ؼ� ������ ������ Ȯ�� 
		if(d != t - (a % 10)){
			// �ٸ��� �Ѽ��� �ƴ� 
			return false; 
		};
	}
	
	// ������ ����� ��� �Ѽ��� ���� 
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
