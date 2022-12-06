#include<bits/stdc++.h>
using namespace std;
int main()
{
 int t1,t2;
 int n;
 cin>>t1;
 cin>>t2;
 cin>>n;
 vector<int>v;
 for(int i=0;i<n;i++){
  int temp;
  cin>>temp;
   v.push_back(temp);
 }
 sort(v.begin(),v.end());
 vector<int>a;
 vector<int>b;
  int c1=0;
  int c2=0;
 int j=t1*v[n-1];
 int k=0;
 a.push_back(v[n-1]);
  c1++;
 for(int i=n-2;i>=0;i--){
          int x=j+(t1*v[i]);
          int y=k+(t2*v[i]);
         
          if(x<y){
           a.push_back(v[i]);
            c1++;
           y=y-(t2*v[i]);
           if(x<y){
             j=0;
             k=y-x;
            }
            else{
             k=0;
             j=x-y;
            }

          }
          else{
           x=x-(t1*v[i]);
            b.push_back(v[i]);
            c2++;
            if(x<y){
             j=0;
             k=y-x;
            }
            else{
             k=0;
             j=x-y;
            }}}
 for(int i=0;i<c1;i++)
  cout<<a[i]<<" ";
 cout<<endl;
 for(int i=0;i<c2;i++)
  cout<<b[i]<<" ";
}
