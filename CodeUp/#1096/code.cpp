#include <iostream>

using namespace std;

int main(void){
	int map[19][19] = {{0,},};
	int cnt, x, y;
	
	scanf("%d", &cnt);
	
	for(int i = 0; i < cnt; i++){
		scanf("%d %d", &x, &y);
		// index�� 0����~ 
		map[x-1][y-1] = 1;
	}
	
	// �������� Ž�� 
	for(int i = 0; i < 19; i++){
		for(int j = 0; j < 19; j++){
			cout << map[i][j] << " ";
		}
		cout << endl;
	}
	
	return 0;
	
} 
