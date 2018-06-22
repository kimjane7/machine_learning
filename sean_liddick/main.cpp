#include <iostream>
#include <cmath>
#include <string> 
#include <fstream>
#include <iomanip>
#include <vector>
#include <random>

using namespace std;

void show_event(vector<vector<double>>& energy, int i){
	for(int k = 15; k >= 0; --k){
		cout << "[";
		for(int j = k; j < 256; j += 16){
			cout << setw(7) << setprecision(4) << energy[i][j];
		}
		cout << "]" << endl;
	}
}

int get_bin_index(double energy, double binwidth){
	return floor(energy/binwidth);
}

int main(int argc, char *argv[]){


	/*************************
	****** READ IN DATA ******
	*************************/

	
	// limit number of events to read in
	int max = 5000;

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
	for(int i = 0; i < max; ++i){

		for(int j = 0; j < 256; ++j) infile >> energy[i][j];
		infile >> dummy;
		infile >> position[i][0] >> position[i][1];
		for(int j = 0; j < 3; ++j) infile >> dummy;
	}
	
	// close file
	infile.close();


	/*****************************************
	****** GET WEIGHTS FROM ENERGY DIST ******
	*****************************************/

	/*
	// define bins
	int nbins = 200;
	double max_energy = 6120.0;
	double binwidth = max_energy/nbins;
	vector<vector<double>> total_energy_weights;
	total_energy_weights.resize(nbins);
	for(int i = 0; i < nbins; ++i) total_energy_weights[i].resize(2);

	*/

	ofstream outfile;
	outfile.open("cell_stats.dat");

	for(int targetcell = 0; targetcell < 256; ++targetcell){

		outfile << targetcell << "\t";

		vector<double> x,y;

		for(int i = 0; i < max; ++i){

			int count = 0;

			for(int j = 0; j < 256; ++j){
				if(energy[i][j] > 0){
					count += 1;
					if(count == 1 & j == targetcell) {
						x.push_back(position[i][0]);
						y.push_back(position[i][1]);
					}
				}
			}
		}

		outfile.close();
	}




	/* SOME CODE THAT WRITES TO FILES

	// open files to organize data
	ofstream outfile1, outfile2, outfile3;
	outfile1.open("indices.dat");
	outfile2.open("total_energies.dat");
	outfile3.open("positions.dat");

	// headings
	outfile1 << "# line i, activated cell indices j's" << endl; 
	outfile2 << "# line i, total energy for event i" << endl;
	outfile3 << "# x_i, y_i, activated cell indices j's" << endl;

	// write to file
	for(int i = 0; i < max; ++i){

		outfile1 << i << "\t";
		outfile2 << i << "\t";
		outfile3 << position[i][0] << "\t" << position[i][1] << "\t";

		double Etot = 0;

		for(int j = 0; j < 256; ++j){

			if(energy[i][j] > 0){
				Etot += energy[i][j];
				outfile1 << j << "\t";
				outfile3 << j << "\t";
			}
		}
		outfile1 << endl;
		outfile2 << Etot << endl;
		outfile3 << endl;
	}

	// close file
	outfile1.close();	
	outfile2.close();
	outfile3.close();

	for(int targetcell = 0; targetcell < 256; ++targetcell){

		cout << targetcell << endl;

		ofstream outfile4;
		outfile4.open("cell"+to_string(targetcell)+".dat");

		for(int i = 0; i < max; ++i){

			int count = 0;

			for(int j = 0; j < 256; ++j){
				if(energy[i][j] > 0){
					count += 1;
					if(count == 1 & j == targetcell) outfile4 << position[i][0] << "\t" << position[i][1] << endl; 
				}
			}
		}

		outfile4.close();
	}

	*/

	return 0;
}