#include <bits/stdc++.h>
using namespace std;

int arr[10000];
int sz[10000];

int dad(int i)
{
	while(arr[i] != i){
		arr[i] = arr[arr[i]];
		i = arr[i];
	}
	
	return i;
}

void merge(int a, int b)
{
	int dad_a = dad(a);
	int dad_b = dad(b);
	
	if(sz[dad_a] < sz[dad_b]){
		arr[dad_a] = arr[dad_b];
		
		sz[dad_b] += sz[dad_a];
	}
	else{
		arr[dad_b] = arr[dad_a];
		
		sz[dad_a] += sz[dad_b];
	}
}

void initialize(int n)
{
	for(int i=0; i<n; i++){
		arr[i] = i;
		sz[i] = 1;
	}
}

bool find(int a, int b)
{
	if(dad(a) != dad(b))
		return false;
	else
		return true;
}

int main()
{
	int n,m;	cin>>n>>m;
	// n no of node and m no of edges
	
	initialize(n);
	
	while(m--){
		int x,y;	cin>>x>>y;
		merge(x, y);
	}
	
	return 0;
}
