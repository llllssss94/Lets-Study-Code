#include <iostream>

using namespace std;

int main(void){
	int map[10][10];
	// 초기위치 
	int x = 1, y = 1;
	
	// 한줄씩 초기화 
	for(int i = 0; i < 10; i++){
		scanf("%d %d %d %d %d %d %d %d %d %d", \
		&map[i][0], &map[i][1], &map[i][2], &map[i][3], &map[i][4],\
		&map[i][5],	&map[i][6], &map[i][7], &map[i][8], &map[i][9]);
	}
	
	// 탐색 
	while(map[x][y] != 2){
		// trace
		map[x][y] = 9;
		
		// 오른쪽 확인 y좌표 +1 지점 
		if(map[x][y+1] == 1){
			// 아래 확인 
			if(map[x+1][y] == 1){
				// Dead End
				break;
			}
			// 이동만 하고 trace는 다음 루프에서 
			x++;
			continue;
		}
		y++;
	}
	// 먹이를 찾은 경우 
	map[x][y] = 9;
	
	// 출력 
	for(int i = 0; i < 10; i++){
		for(int j = 0; j < 10; j++){
			cout << map[i][j] << " ";
		}
		cout << endl;
	}
	
	return 0;
}
