#include <bits/stdc++.h>
using namespace std;

int main()
{
    int N;
	int K;
	cin >> N;
	cin >> K;
	vector<int> p_vec(N);
	for(int i=0 ; i<N ; i++)
	{
	  cin >> p_vec[i];
	}
	sort(p_vec.begin(), p_vec.end());

	int sum_ = 0;
	for(int i=0 ; i<K ; i++)
    {
	    sum_ += p_vec[i];
	}
	cout << sum_ << endl;
}
