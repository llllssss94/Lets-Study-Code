#include <iostream>

using namespace std;

int main(void){
	int map[19][19];
	int num, x, y;
	
	// ���پ� �ʱ�ȭ 
	for(int i = 0; i < 19; i++){
		scanf("%d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d", \
		&map[i][0], &map[i][1], &map[i][2], &map[i][3], &map[i][4], &map[i][5], &map[i][6], \
		&map[i][7], &map[i][8], &map[i][9], &map[i][10], &map[i][11], &map[i][12],\
		&map[i][13],	&map[i][14], &map[i][15], &map[i][16], &map[i][17], &map[i][18], &map[i][19]);
	}
	
	scanf("%d", &num);
	
	for(int i = 0; i < num; i++){
		scanf("%d %d", &x, &y);
		
		// index�� 0���� ~ 
		x--;
		y--; 
		
		// ������(x��) ������
		for(int j = 0; j < 19; j++){
			map[x][j] = map[x][j] ^ 1;
		}
		
		// ������(y��) ������
		for(int j = 0; j < 19; j++){
			map[j][y] = map[j][y] ^ 1;
		}
	}
	
	// ��� 
	for(int i = 0; i < 19; i++){
		for(int j = 0; j < 19; j++){
			cout << map[i][j] << " ";
		}
		cout << endl;
	}
	
	return 0;
}
