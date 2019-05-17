#include<iostream.h>
#include<conio.h>
void main()
{clrscr();
int ar[10],n;
cout<<"please enter the size of the array to be sorted";
cin>>n;
cout<<"please enter an array to be sorted ";
for(int i=0;i<n;i++)
cin>>ar[i];
for(int j=0;j<n;j++)
{for(int k=0;k<n-j-1;k++)
 if(ar[k]>ar[k+1])
 {int temp=ar[k+1];
  ar[k+1]=ar[k];
  ar[k]=temp;
 }
}
for(i=0;i<n;i++)
cout<<ar[i]<<" ";
getch();
}
