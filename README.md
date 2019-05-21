# Task__v2.0
Contains files with sorting algorithm
hytyr
/*bubble sorting*/
#include<stdio.h>
int main()
{
  int a[10],i,j,x,n;
  printf("enter total number of elements:");
  scanf("%d",&n);
  printf("\n enter the elements of array");
  for(i=0; i<n; i++)
    scanf("%d",&a[i]);
  for (i=0; i<n-i; i++)
  {
    for(j=0; j<n-i-1; j++)
    {
       if(a[j]>a[j+1])
       {
          x=a[j];
          a[j]=a[j+1];
          a[j+1]=x;
       }
     }
  }
  printf("\n List sorted in ascending order:");
  for(i=0; i<n; i++)
    printf("%d\t",a[i]);
  printf("\n");
  return 0;
}