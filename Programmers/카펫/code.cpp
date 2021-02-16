#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(int brown, int yellow) {
    vector<int> answer;
    int h= 1, v = 9;
    
    while(h <= v){
    	v = (brown / 2) - h + 2;
    	if(((h * v) - brown) == yellow){
    		answer.push_back(v);
    		answer.push_back(h);
    		break;
		}
		h++;
	}
	
	cout << "[" << answer[0] << ", " << answer[1] <<  "]\n";
    return answer;
}

int main(void){
	solution(10, 2);
	solution(8, 1);
	solution(24, 24);	
}
