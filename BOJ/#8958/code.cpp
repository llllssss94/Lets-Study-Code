#include <iostream>

using namespace std;

int main(void){
	cin.tie(NULL);
	ios::sync_with_stdio(false);
	
	int n, score, tmp, j;
	char ox[81];
	
	cin >> n;
	
	for(int i = 0; i < n; i++){
		cin >> ox;
		
		score = 0;
		tmp = 0;
		j = 0;
		// 처음부터 끝까지!!! 
		while(ox[j]){
			if(ox[j] == 'O'){
				tmp++;
				score += tmp;
			}
			else{
				tmp = 0;
			}
			j++;
		}
		
		cout << score << "\n";
	}
	
	
	return 0;
}
