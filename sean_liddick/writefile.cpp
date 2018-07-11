// copy of old main which writes various things to files

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

int get_bin_index(double energy, double bin_width){
	return floor(energy/bin_width);
}

double get_cell_centerx(int i){
	return 3.0*floor(i/16.0)-22.5;
}

double get_cell_centery(int i){
	return 3.0*(i%16)-22.5;
}

int main(int argc, char *argv[]){


	/*************************
	****** READ IN DATA ******
	*************************/

	// limit number of events to read in
	int max = 1000000;

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



	
	cout << "writing to... 'cell_stats.dat'" << endl;
	ofstream outfile;
	outfile.open("cell_stats.dat");
	outfile << "# cell index, cell center x, cell center y, avg x, avg y, avg r (from center of cell), std dev x, std dev y, std dev r" << endl;

	for(int targetcell = 0; targetcell < 256; ++targetcell){

		int count = 0;
		double center_x = get_cell_centerx(targetcell);
		double center_y = get_cell_centery(targetcell);
		double avg_x = 0.0, avg_y = 0.0, avg_r = 0.0;
		double sig_x = 0.0, sig_y = 0.0, sig_r = 0.0;
		vector<double> x, y;

		// calculate averages
		for(int i = 0; i < max; ++i){
			if(energy[i][targetcell] > 0){
				count += 1;
				x.push_back(position[i][0]);
				y.push_back(position[i][1]);
				avg_x += position[i][0];
				avg_y += position[i][1];
			}
		}

		if(count != 0){
			avg_x = avg_x/count;
			avg_y = avg_y/count;
			avg_r = sqrt(pow(avg_x-center_x,2) + pow(avg_y-center_y,2));			
		}

		// calculate standard deviations
		if(count > 1){
			for(int i = 0; i < count; ++i){
				sig_x += pow(x[i]-avg_x,2)/(count-1);
				sig_y += pow(y[i]-avg_y,2)/(count-1);
			}		
		}
		sig_x = sqrt(sig_x);
		sig_y = sqrt(sig_y);
		if(avg_r > 0) sig_r = (avg_x-center_x)*sig_x/avg_r + (avg_y-center_y)*sig_y/avg_r;

		outfile << targetcell << "\t" << center_x << "\t" << center_y << "\t";
		outfile << avg_x << "\t" << avg_y << "\t" << avg_r << "\t";
		outfile << sig_x << "\t" << sig_y << "\t" << sig_r << endl;	
	}

	outfile.close();
	
	double bin_width = 10;
	double max_energy = 3070;
	int nbins = ceil(max_energy/bin_width);

	vector<vector<double>> energy_bins;
	energy_bins.resize(nbins);
	for(int i = 0; i < nbins; ++i){
		energy_bins[i].resize(2);
		energy_bins[i][0] = (i+0.5)*bin_width;
		energy_bins[i][1] = 0;
	}

	// open files to organize data
	ofstream outfile1, outfile2, outfile3, outfile4;
	outfile1.open("indices.dat");
	outfile2.open("total_energies.dat");
	outfile3.open("energy_bins.dat");
	outfile4.open("positions.dat");

	// headings
	outfile1 << "# line i, activated cell indices j's" << endl; 
	outfile2 << "# line i, total energy for event i" << endl;
	outfile3 << "# energy bin width = " << bin_width << endl;
	outfile3 << "# center of energy bin (keV), count in bin, percentile" << endl;
	outfile4 << "# x_i, y_i, activated cell indices j's" << endl;

	// write to file
	for(int i = 0; i < max; ++i){

		outfile1 << i << "\t";
		outfile2 << i << "\t";
		outfile4 << position[i][0] << "\t" << position[i][1] << "\t";

		double Etot = 0;

		for(int j = 0; j < 256; ++j){

			if(energy[i][j] > 0){
				Etot += energy[i][j];
				outfile1 << j << "\t";
				outfile4 << j << "\t";
			}
		}
		outfile1 << endl;
		outfile2 << Etot << endl;
		outfile4 << endl;

		energy_bins[get_bin_index(Etot, bin_width)][1] += 1;
	}

	// close file
	outfile1.close();	
	outfile2.close();
	outfile4.close();

	double percentile = 0.0;
	for(int i = 0; i < nbins; ++i){
		percentile += energy_bins[i][1]/max;
		outfile3 << energy_bins[i][0] << "\t" << energy_bins[i][1];
		outfile3 << "\t" << percentile << endl;
	}

	outfile3.close();

	for(int targetcell = 0; targetcell < 256; ++targetcell){

		cout << targetcell << endl;

		ofstream outfile;
		outfile.open("cell"+to_string(targetcell)+".dat");

		for(int i = 0; i < max; ++i){

			for(int j = 0; j < 256; ++j){
				if(energy[i][j] > 0){
					if(j == targetcell) outfile << position[i][0] << "\t" << position[i][1] << endl; 
				}
			}
		}

		outfile.close();
	}



	return 0;
}