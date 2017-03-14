#include <iostream>
#include <vector>

void sort_data(std::vector<int> &data){
	// Find the length of the vector.
	int length = data.size();

	// A vector with 1 element is already sorted. Therefore, our loop starts from 1 to length.
	for(int i(1); i < length; ++i){

		// temporarily hold the value of the data.
		int key = data.at(i);

		// We now insert the value on the sorted array behind the current position.
		int j = i-1;

		// A loop to find the correct position for the value at hand along with swapping the values which is greater than the 
		// value in our hand.
		while(j >= 0 && data.at(j)>key){
			data.at(j+1) = data.at(j); // just swap the values
			j--;
		}

		// insert the data into its correct place.
		data.at(j+1) = key;
	}
}

void print_data(std::vector<int> data){
	for(auto it: data){
		std::cout << it << std::endl;
	}
}

int main(){
	std::vector<int> data = {1,8,6,7,4,3,9,2};
	sort_data(data);
	print_data(data);

	std::cout << "#############" << std::endl;

	data = {9,8,7,6,5,4,3,2,1};
	sort_data(data);
	print_data(data);
	return 0;
}