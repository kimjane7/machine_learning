#include "layer.h"

using namespace std;

int main(int argc, char *argv[]){




	return 0;
}


/*

	int nevents = 1000000;

	// matrices to store energy deposition and initial positions
	vector<vector<double>> energy;
	vector<vector<double>> position;
	energy.resize(max);
	position.resize(max);
	for(int i = 0; i < max; ++i){
		energy[i].resize(256);
		position[i].resize(2);
	}

	// to store useless data
	double dummy;

	// open file
	ifstream infile;
	infile.open("data.dat");

	// read in data
	cout << "reading data..." << endl;
	for(int i = 0; i < max; ++i){

		for(int j = 0; j < 256; ++j) infile >> energy[i][j];
		infile >> dummy;
		infile >> position[i][0] >> position[i][1];
		for(int j = 0; j < 3; ++j) infile >> dummy;
	}
	
	// close file
	infile.close();


	// output
	vector<double> output;
	output.resize(3);

	// for now, we only have 1 electron cases
	vector<double> answer{0.0, 1.0, 0.0};

	// one hidden layer with nhidden nodes
	int nhidden = 10;
	vector<double> hidden_layer;
	hidden_layer.resize(nhidden);

	// random weights
	mt19937 generator;
	uniform_real_distribution<double> rand(-10.0,10.0);

	vector<vector<vector<double>>> weights;
	W.resize(nhidden);
	for(int i = 0; i < nhidden; ++i){
		W[i].resize(256);
		for(int j = 0; j < 256; ++j){
			W[i][j].resize(256);
			for(int k = 0; k < 256; ++k) W[i][j][k] = rand(generator);
	}



	// biases
	vector<double> B;

*/