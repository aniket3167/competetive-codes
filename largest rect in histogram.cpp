#include <bits/stdc++.h>
using namespace std;

int main()
{
	int n;	cin>>n;
	int a[n];
	for(int i=0; i<n; i++)
		cin>>a[i];
		
	stack<int> h;
	stack<int> pos;
	
	int ans = 0;
	
	for(int i=0; i<n; i++)
	{
		if(h.empty() || a[i] > h.top())
		{
			h.push(a[i]);
			pos.push(i);
		}
		else if(a[i] < h.top())
		{
			int tmpos, tmph;
			while(!h.empty() && a[i] < h.top())
			{
				tmpos = pos.top();
				tmph = h.top();
				h.pop();
				pos.pop();
				int tmp = tmph*(i - tmpos);
				if(tmp > ans)
					ans = tmp;
			}
			h.push(a[i]);
			pos.push(tmpos);
		}
	}
    int i = n;
	while(!h.empty())
	{
        int tmpos, tmph;
		tmpos = pos.top();
		tmph = h.top();
		h.pop();
		pos.pop();
		int tmp = tmph*(i - tmpos);
		if(tmp > ans)
			ans = tmp; 
       
	}
	cout<<ans<<endl;
	return 0;
}
