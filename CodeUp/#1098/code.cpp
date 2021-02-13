#include <iostream>
#include <cmath>

using namespace std;

int main(void){
	int h, w, n;
	int l, d, x, y;
	int map[100][100] = {{0,},};
	
	scanf("%d %d\n%d", &h, &w, &n);
	
	for(int i = 0; i < n; i++){
		scanf("%d %d %d %d", &l, &d, &x, &y);
		
		// index�� 0����~ 
		x--;
		y--;
		
		// ���ι��� x�� 
		if(d == 0){
			// ĭ�� ������ ������
			l = min(l, w - y);
			for(int j = 0; j < l; j++){
				map[x][y + j] = 1;
			}
		}
		else{
			// ���ι��� y��
			// ĭ�� ������ ������
			l = min(l, h - x);
			for(int j = 0; j < l; j++){
				map[x + j][y] = 1;
			}
		}
	}
	
	// ��� 
	for(int i = 0; i < h; i++){
		for(int j = 0; j < w; j++){
			cout << map[i][j] << " ";
		}
		cout << endl;
	}
	
	return 0;
} 
