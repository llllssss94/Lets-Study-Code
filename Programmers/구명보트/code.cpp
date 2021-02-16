#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int solution(vector<int> people, int limit) {
    int answer = 0;
    int a, b;
    
    sort(people.begin(), people.end());
    
    a = 0;
    b = people.size() - 1;
    // �� ������ 
    while(a <= b){
    	answer++;
    	// ���� Ż�� �ִٸ� 
    	if(people[a] + people[b] <= limit){
    		a++;
		}
		b--;
	}
    
    return answer;
}

int main(void){
	vector<int> people = {70, 50, 80, 50};
	int limit = 100;
	
	cout << solution(people, limit) << "\n";
	
	people = {70, 80, 50};
	
	cout << solution(people, limit) << "\n";
	
}
