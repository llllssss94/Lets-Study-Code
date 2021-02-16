#include <iostream>

using namespace std;

int main(void){
	cin.tie(NULL);
	ios::sync_with_stdio(false);
	
	int num, new_num = 0, cycle = 0;
	
	cin >> num;
	
	new_num = num;
	while(true){
		if(new_num < 10){
			new_num = new_num * 10 + new_num;
		}
		else{
			new_num = (new_num % 10) * 10 + ((new_num % 10) + (new_num / 10)) % 10;
		}
		cycle++;
		if(new_num == num) break;
	}
	cout << cycle << "\n";
	
	return 0;
}
