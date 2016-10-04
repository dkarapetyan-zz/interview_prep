#include <stdio.h>
#include <stdlib.h>

// Quicksort recursive algorithm

void swap(int *s, int k, int m)
{
	int temp;
	temp = s[k];
	s[k] = s[m];
	s[m] = temp;
}

void quicksort(int *v, int left, int right)
{
	// we partition using the middle element of the array
	// base step
	int last;
	int mid = (left + right)/2;
	if (left >= right)
	return;

//inductive (i.e. recursive) step
	swap(v, left, mid);// make partition element first element of array
	last = left;
	for (int i=left +1; i <= right; ++i)
	{
		if (v[i] < v[left])
		{
			swap(v, i, ++last);
		}
// have all elements less than v[left] immediately following it--once this list terminates, have all ellements greater than v[left]. Now we restore partition element
		swap(v, left, last);//done partitioning--last is our partition element
		quicksort(v, left, last-1);
		quicksort(v, last+1, right);
	}

}

int main()
{
	int array[] =
	{ 1, 4, 2, 5, 20 };
	quicksort(array, 0, 5);
	return 0;
}

