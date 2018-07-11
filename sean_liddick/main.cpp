#include <iostream>
#include <cmath>
#include <string> 
#include <fstream>
#include <iomanip>
#include <vector>
#include <random>
#include "pixel.h"

using namespace std;


int main(int argc, char *argv[]){

	// limit number of events to read in
	int max = 10000;

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


	// make detector
	vector<CPixel*> detector;
	for(int j = 0; j < 256; ++j){

		CPixel* pixel_ptr = new pixel(j,3.0);
		detector.push_back(pixel);

		for(int i = 0; i < max; ++i){
			if(energy[i][j] > 0){
				detector[j]->events_.push_back(i);
				detector[j]->E_.push_back(energy[i][j]);
				detector[j]->X_.push_back(position[i][0]);
				detector[j]->Y_.push_back(position[i][1]);
			}
		}

	}

	// deallocate memory
	for(int j = 0; j < 256; ++j) delete detector[j];
	detector.clear();

	return 0;
}