#include <iostream>

using namespace std;

int main(void){
	int map[10][10];
	// �ʱ���ġ 
	int x = 1, y = 1;
	
	// ���پ� �ʱ�ȭ 
	for(int i = 0; i < 10; i++){
		scanf("%d %d %d %d %d %d %d %d %d %d", \
		&map[i][0], &map[i][1], &map[i][2], &map[i][3], &map[i][4],\
		&map[i][5],	&map[i][6], &map[i][7], &map[i][8], &map[i][9]);
	}
	
	// Ž�� 
	while(map[x][y] != 2){
		// trace
		map[x][y] = 9;
		
		// ������ Ȯ�� y��ǥ +1 ���� 
		if(map[x][y+1] == 1){
			// �Ʒ� Ȯ�� 
			if(map[x+1][y] == 1){
				// Dead End
				break;
			}
			// �̵��� �ϰ� trace�� ���� �������� 
			x++;
			continue;
		}
		y++;
	}
	// ���̸� ã�� ��� 
	map[x][y] = 9;
	
	// ��� 
	for(int i = 0; i < 10; i++){
		for(int j = 0; j < 10; j++){
			cout << map[i][j] << " ";
		}
		cout << endl;
	}
	
	return 0;
}
