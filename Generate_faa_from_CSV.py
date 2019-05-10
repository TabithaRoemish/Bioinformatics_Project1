#Generates fasta files from CSV with column names:
#DP Name, Reference, Database, Source, Sequence, Structure, GC Count, Length, Pairs, Mean
import pandas as pd

def getfilename(val):
    val = val[5:]
    val = val[:-3]
    return val + ".faa"
    
#open cvs file
file = 'C:/Users/v-taroem/test.csv'
data = pd.read_csv(file, delimiter='\t')

#save columns as arrays
dp = data['DP Name'].values
seq = data['Sequence'].values
ref = data['Reference'].values
size = len(seq)

#for each row in column, create .faa file
for i in range(size):
    filename = getfilename(ref[i])
    out = open(filename, 'w')
    out.write('>' + dp[i] + '_' + ref[i] + '\n')
    out.write(seq[i] + '\n')
    out.close()

print("done")