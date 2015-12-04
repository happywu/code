#include<cstdio>
#include<iostream>
using namespace std;
int main(){
	freopen("a.in","r",stdin);
	double M;
	scanf("%lf",&M);
	double a[10];
	a[1] = 0;
	a[2] = 1500*0.03;
	a[3] = a[2]+3000*0.1;
	a[4] = a[3]+(9000-4500)*0.2;
	a[5] = a[4]+(35000-9000)*0.25;
	a[6] = a[5]+(55000-35000)*0.3;
	a[7] = a[6]+(80000-55000)*0.35;
	int idx = 8;
	for(int i=1;i<=7;i++)
		if(a[i]>=M){
			idx = i;
			break;
		}

	double b[]={0,0,1500,4500,9000,35000,55000,80000};
	double c[]={0,0,0.03,0.1,0.2,0.25,0.3,0.35,0.45};
	M-=a[idx-1];
	double ans = M/c[idx];
	ans += b[idx-1];
	ans += 3500;
	printf("%d\n",(int)ans);

	return 0;
}
