#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int solution(vector<int> citations) {
    int answer = 0, length, cnt;
    int max_val = 0;
    
    length = citations.size();
    // �ִ밪 ã�� 
    for(int i = 0; i < length; i++){
    	max_val = max(citations[i], max_val);
	}
	
	// �ִ� �ο밪���� Ȯ���ϱ� 
	for(int i = 0; i < max_val; i++){
		cnt = 0;
		for(int j = 0; j < length; j++){
			// i�� �̻� �ο�� ��� 
			if(citations[j] >= i){
				cnt++;
			}
		}
		// i�� �̻� �ο��� i�� �̻��̸� 
		if(cnt >= i){
			// H-index ���� 
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
