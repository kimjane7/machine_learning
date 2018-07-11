#include "layer.h"

CLayer::CLayer(int size_of_input, int number_of_nodes){

	n_ = number_of_nodes;
	m_ = size_of_input;

	output_.resize(n_);

	// assign random weights and biases
	mt19937 generator;
	uniform_real_distribution<double> rand(-1.0,1.0);

	bias_.resize(n_);
	for(int i = 0; i < n_; ++i){
		bias_[i].resize(m_);
		for(int j = 0; j < m_; ++j){
			bias_[i][j] = rand(generator);
		}
	}

	weight_.resize(n_);
	for(int i = 0; i < n_; ++i){
		weight_[i].resize(m_);
		for(int j = 0; j < m_; ++j){
			weight_[i][j].resize(m_);
			for(int k = 0; k < m_; ++k){
				weight_[i][j][k] = rand(generator);
			}
		}
	}

}

double CLayer::sigmoid(double z){
	return 1.0/(1.0+exp(-z));
}

void CLayer::compute_output(vector<double> const &input){

	// for each node
	for(int i = 0; i < n_; ++i){

		// compute weighted sum with bias
		double sum = 0.0;

		for(int j = 0; j < m_; ++j){
			
		}

	}
}