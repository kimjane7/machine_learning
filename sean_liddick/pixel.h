#ifndef PIXEL_H
#define PIXEL_H

#include <iostream>
#include <cmath>
#include <string> 
#include <fstream>
#include <iomanip>
#include <vector>
#include <random>
#include "time.h"

using namespace std;

class CPixel{

public:

	int N_, number_;
	double width_;

	// stores event numbers that involve pixel
	vector<int> event_;

	// stores energy deposited into pixel
	vector<double> E_;

	// stores initial positions of electrons that hit pixel
	vector<double> X_, Y_;





	// probability distribution parameters
	double x1_, x2_, alpha1_, alpha2_, normx_;
	double y1_, y2_, beta1_, beta2_, normy_;
	
	CPixel(int pixel_number, double pixel_width);
	~CPixel(){}

	void guess_params();
	double probx(double x);
	double proby(double y);




};

#endif