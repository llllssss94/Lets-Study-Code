#include <iostream>

using namespace std;

int main(void){
	cin.tie(NULL);
	ios::sync_with_stdio(false);
	
	int n, m, cnt;
	int score[1001] = {0,};
	double avg;
	
	cin >> n;
	
	for(int i = 0; i < n; i++){
		cin >> m;
		
		// 초기화 
		fill_n(score, 1001, 0);
		avg = 0;
		cnt = 0;
		for(int j = 0; j < m; j++){
			cin >> score[j];
			avg += score[j];
		}
		avg = double(avg / m);
		
		for(int j = 0; j < m; j++){
			if(score[j] > avg) cnt++;
		}
		
		//  셋째 자리 고정~ 
		cout << fixed;
		cout.precision(3);
		cout << (double(cnt) / m) * 100 << "%\n";
	}
} 
