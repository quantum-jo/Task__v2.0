#include<iostream.h>
#include<conio.h>


void bubblesort (int  array[] , int n )
{
	int temp;
	for(int i=0;i<n;i++)
	{
		for(int j=0 ; j<(n-i) ; j++)
			if ( array[j] > array[j+1])
			{
				temp=array[j];
				array[j]=array[j+1];
				array[j+1]=temp;
			}
	}
	cout<<" The array after sorting using bubble sort";
	for(i=0;i<n;i++)
		cout<<array[i]<<" ";
}

void main()
{
	clrscr();
	int array[50],n;
	cout<<"Enter the number of elements in the array";
	cin>>n;
	cout<<"Enter the elements of the unsorted array";
	for(int i=0 ; i<n ; i++)
		{
		cin>>array[i];
		}
	bubblesort(array,n);
	getch();
}
