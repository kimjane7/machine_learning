#include "pixel.h"

// assume detector has NxN pixels and is centered at origin
// number pixels upwards from lower left corner 
CPixel::CPixel(int N, int pixel_number, double pixel_width){

	N_ = N; 	
	number_ = pixel_number;
	width_ = pixel_width;

	guess_params();
}


void CPixel::guess_params(){

	x1_ = width_*(floor(number_/N_)-0.5*N);
	x2_ = x1_+width_;
	alpha1_ = 5.0;
	alpha2_ = 5.0;
	normx_ = 1.0/(x2_-x1_+1/alpha1_+1/alpha2_);

	y1_ = width_*((number_%N_)-0.5*N);
	y2_ = y1_+width_;
	beta1_ = 5.0;
	beta2_ = 5.0;
	normy_ = 1.0/(y2_-y1_+1/beta1_+1/beta2_);
}


double CPixel::probx(double x){
	if((x >= x1_) && (x <= x2_)) return normx_;
	if(x < x1_) return normx_*exp(alpha1_*(x-x1_));
	if(x > x2_) return normx_*exp(-alpha2_*(x-x_2));
}

double CPixel::proby(double y){
	if((y >= y1_) && (y <= y2_)) return normy_;
	if(y < y1_) return normy_*exp(beta1_*(y-y1_));
	if(y > y2_) return normy_*exp(-beta2_*(y-y_2));
}