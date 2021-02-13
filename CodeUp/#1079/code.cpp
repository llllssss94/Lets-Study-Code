#include <iostream>
#include <string>

using namespace std;

int main(void){
	string str;
	int i = 0, l;
	
	getline(cin, str);
	l = str.size();
	
	while(i < l)
	{
		if(str.at(i) == 'q'){
			cout << str.at(i) << endl;
			
			break;
		}
		if(str.at(i) != ' '){
			cout << str.at(i) << endl;
		}
		i++;
	}
	
	return 0;
}
