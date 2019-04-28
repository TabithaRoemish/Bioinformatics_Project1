#/usr/bin/env python

#https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.choice.html

import numpy as np

if __name__ == "__main__":
	try:
		percent = 0;
		#loop 10 times, add 10 to percent each time
		for i in range(0,10):
			#loop for 100 at each percentage
			for n in range(0,100):
				result = generate_weighted_rna(1000, percent); #sequence length needs to be large for RFam database search, changed 10 to 1000
				print (result);
			percent = i*10;
	except ValueError as e:
		print(e)

def generate_weighted_rna(length, gc_percent):
	weights = generate_weights(gc_percent);
	rna_str = "";
	for x in range(0, length):
		rna_str += weighted_random_codon(weights);
	return rna_str;

def generate_weights(gc_percent):
	if ((gc_percent < 0) or (gc_percent > 100)):
		raise ValueError('Please select a percentage GC content between 0 and 100.');
	g_percent = gc_percent / 200.0;
	at_percent = 100 - gc_percent;
	a_percent = at_percent / 200.0;
	print("\% G used: " + str(g_percent));
	print("\% A used: " + str(a_percent));
	return [g_percent, g_percent, a_percent, a_percent];

def weighted_random_codon(weights):
	codons = ['G', 'C', 'T', 'A'];
	return np.random.choice(codons, p=weights);
