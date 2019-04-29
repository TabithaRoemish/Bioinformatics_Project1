import numpy as np


#generate sequence
def generate_weighted_rna(length, gc_percent):
    weights = generate_weights(gc_percent);
    rna_str = ""
    for x in range(0, length):
        rna_str += weighted_random_codon(weights);
    return rna_str;

def generate_weights(gc_percent):
	if ((gc_percent < 0) or (gc_percent > 100)):
		raise ValueError('Please select a percentage GC content between 0 and 100.');
	g_percent = gc_percent / 200.0;
	at_percent = 100 - gc_percent;
	a_percent = at_percent / 200.0;
	print("> %G used: ", str(g_percent), "/%A used: ", str(a_percent));
	return [g_percent, g_percent, a_percent, a_percent];

def weighted_random_codon(weights):
	codons = ['G', 'C', 'T', 'A'];
	return np.random.choice(codons, p=weights);

#create file
def create_file():
    try:
        filename = str.format("RNA_fastafile");
        file = open(filename, "w+");
        return file;
    except Exception as e:
        raise

#write to file
def write_file(data, file, gc_content, seq_num):
    try:
        file.write(">GCPercent.%d.seq%d\n" % (gc_content, seq_num));
        file.write(data);
        file.write("\n");
        print(data);
    except Exception as e:
        raise
        

if __name__=="__main__":
    try:
        seq_size = 1000;
        gc_content = 0; 
        num_of_seq = 10;
        file = create_file(); # create file
        #loop at 10+ intervals (0 - 100 percent)
        for i in range(0,11):
            gc_content = i*10;
            #loop for x sequences at each percentage
            for n in range(0,num_of_seq):
                data = generate_weighted_rna(seq_size, gc_content);
                write_file(data, file, gc_content, n+1);
        file.close();
    except ValueError as e:
        print(e);
