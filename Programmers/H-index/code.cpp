#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int solution(vector<int> citations) {
    int answer = 0, length, cnt;
    int max_val = 0;
    
    length = citations.size();
    // 최대값 찾기 
    for(int i = 0; i < length; i++){
    	max_val = max(citations[i], max_val);
	}
	
	// 최대 인용값까지 확인하기 
	for(int i = 0; i < max_val; i++){
		cnt = 0;
		for(int j = 0; j < length; j++){
			// i번 이상 인용된 경우 
			if(citations[j] >= i){
				cnt++;
			}
		}
		// i번 이상 인용이 i번 이상이면 
		if(cnt >= i){
			// H-index 공식 
			answer = max(answer, min(cnt, i));
		}
	}
   
    return answer;
}

int main(void){
	vector<int> citations = {3, 0, 6, 1, 5};
	int result;
	result = solution(citations);
	cout << result << "\n";
}
