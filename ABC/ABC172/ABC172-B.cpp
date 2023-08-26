#include<iostream>
#include<string>
using namespace std;

int main() {
    string S;
	string T;
	cin >> S;
	cin >> T;
	int count = 0;

	for(int i=0 ; i<S.size() ; i++)
	{
	  if(S.at(i) != T.at(i))
		{
		  count ++;
		}
	}
	cout << count << endl;
}
