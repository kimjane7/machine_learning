#ifndef LAYER_H
#define LAYER_H

#include <iostream>
#include <cmath>
#include <string> 
#include <fstream>
#include <iomanip>
#include <vector>
#include <random>
#include "time.h"

using namespace std;

class CLayer{

public:

	int n_, m_;
	vector<double> output_;
	vector<vector<double>> bias_;
	vector<vector<vector<double>>> weight_;
	
	CLayer(int size_of_input, int number_of_nodes);
	~CLayer(){}

	double sigmoid(double z);
	void compute_output(vector<double> const &input);


};

#endif