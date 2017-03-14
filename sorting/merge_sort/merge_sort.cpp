#include <iostream>
#include <vector>
#include <cmath>
#include <limits>

void merge(std::vector<int> v, int p, int q, int r);
void mergesort(std::vector<int> v, int p, int r);
void print_data(std::vector<int> v);


void mergesort(std::vector<int> data, int p, int r){
	if(p < r){
		int q = p + (r-p)/2;
		mergesort(data, p, q);
		mergesort(data, q+1, r);
		merge(data, p, q, r);
	}
}

void merge(std::vector<int> data, int p, int q, int r){
	int n1 = q - p + 1; // Length of Left Vector
	int n2 = r - q; // Length of Right Vector

	// A precondition of the merge is that the two Vector A[p...q] and A[q+1 ..r] are already sorted.

	std::vector<int> left;
	std::vector<int> right;

	for( int i(0); i < n1; i++)
		left.push_back(data.at(p + i));



	for( int i(0); i < n2; i++){
		right.push_back(data.at(q + i + 1));
	}

	int i(0),j(0), k(p);

	while(i < n1 && j < n2){
		if(left.at(i) <= right.at(j)){
			data.at(k) = left.at(i);
			i++;
		}
		else{
			data.at(k) = right.at(j);
			j++;
		}
	}

	/* Copy the remaining elements of L[], if there
       are any */
    while (i < n1)
    {
        data.at(k) = left.at(i);
        i++;
        k++;
    }
 
    /* Copy the remaining elements of R[], if there
       are any */
    while (j < n2)
    {
        data.at(k) = right.at(j);
        j++;
        k++;
    }

}



void print_data(std::vector<int> data){
	for(auto it: data){
		std::cout << it << std::endl;
	}
}

int main(){
	std::vector<int> data = {1,8,6,7,4,3,9,2};
	int size = data.size();
	mergesort(data, 0, data.size() - 1);
	print_data(data);
	return 0;
}