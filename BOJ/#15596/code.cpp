#include <iostream>
#include <vector>

using namespace std;

long long sum(vector<int> &a){
	long long int sum;
	
	for(int i; i < a.size(); i++){
		sum += a[i];
	}
	
	return sum;
}

int main(void){
	vector<int> a = {1, 2, 3, 4, 5};
	long long int r;
	
	r = sum(a);
	
	cout << r << "\n";
	
	return 0;
}
