#include <iostream>
using namespace std;
int main() {
int n,t;
string c;
char temp;
cin>>n>>t>>c;
for(int i =0;i<t;i++){
    
    for(int j=0;j<=n-1;j++){
        if((c[j]=='B')&& (c[j+1]=='G')){
                temp=c[j];
                c[j]=c[j+1];
                c[j+1]=temp; 
                j++;  
            }
        
        
    }
}

cout<<c;
}