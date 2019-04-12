#/usr/bin/env python3

import gen_rna

def create_file_and_write(data, weight, run_id=1):
	try:
		filename = str.format("gc_%d_run_%d" % (weight, run_id));
		f = open(filename, "w+"); #overwrite file if exists
		f.write(data);
		print("filename: " + data);
		f.close();
	except Exception as e:
		raise


if __name__=="__main__":
	try:
		gc_content = 50;
		data = gen_rna.generate_weighted_rna(10, gc_content);
		create_file_and_write(data, gc_content);
	except ValueError as e:
		print(e);
