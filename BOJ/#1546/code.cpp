#include <iostream>

using namespace std;

int main(void){
	cin.tie(NULL);
	ios::sync_with_stdio(false);
	
	int n, max = 0;
	int num[1001];
	double avg = 0;
	
	cin >> n;
	
	for(int i = 0; i < n; i++){
		cin >> num[i];
		if(max < num[i]) max = num[i];
	}
	
	for(int i = 0; i < n; i++){
		avg += (double(num[i])/max) * 100;
	}
	
	cout.precision(8);
	cout << avg/n << "\n";
	
	return 0;
}
