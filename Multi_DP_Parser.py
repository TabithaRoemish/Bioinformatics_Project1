#multi dp reader
#file requires:
  #  dp files from RNA strand
  #  list of sequence lengths from website data saved as txt files

import math
import pandas as pd

def getlength(file):
    length = file.readline()
    length = length.strip()
    lg = int(length)
    return lg

def getdata(file, length):
    rows = 0
    data = ""
    if(length<50):
        rows = 1
    else:
        rows = length/50 # fifty char per line
        rows = math.ceil(rows)
    for i in range(rows):
        temp = file.readline()
        temp = temp[:-1]
        data = data + temp
    data = data.strip()
    if(length%50 == 0):
        file.readline() # eat white line if length is perfectly divisible by 50
    return data

def countGC(seq):
    G = seq.count("G")
    C = seq.count("C")
    minimum = G # need to find min matching pairs for GC pair content
    if(G>C):
        min = C
    minimum = minimum * 2
    length = len(seq)
    ratio = minimum/length
    return ratio

def countPairs(struc):
    dots = struc.count(".")
    length = len(struc)
    pairs = (length - dots)
    return pairs

def cleanHeader(val):
    val = val[2:] # remove #
    val = val[:-1] # remove return character
    val = val.replace(",", "-") # remove any commas
    return val


if __name__=="__main__":
    try:
        
        fileList = ["5S rRNA_","23S rRNA_", "16S rRNA_", "GI Intron_", "Other RNA_"]
        fileSizes = [161, 205, 723, 152, 202]
        fileCount = len(fileList)
        date = pd.to_datetime('today').strftime('%Y_%m_%d_%H_%M') 
        results = date + '_Results.csv'
        o = open(results, "w")
        o.write("DP Name,Reference,Database,Source,Sequence,Structure,GC Count,Length,Pairs,Mean\n")
        
        for n in range(fileCount):
            #new file - for write to
            filename = fileList[n] + str(fileSizes[n]) + ".dp" # update for each file
            filelengths = fileList[n] + "lengths.txt" # update for each file
            seq_in_file = fileSizes[n] # update for each file

            f = open(filename, "r")
            l = open(filelengths, "r") #open corresponding lengths file

            for i in range(seq_in_file):
                o.write(filename + ",")
                length = getlength(l)
                SequenceReference = f.readline()
                #check for random white space after structure
                if(SequenceReference[0] != "#"):
                    SequenceReference = f.readline() # eat extra white space
                SequenceReference = cleanHeader(SequenceReference)
                o.write(SequenceReference + ",")
                database = f.readline()
                database = cleanHeader(database)
                o.write(database + ",")
                source = f.readline()
                source = cleanHeader(source)
                o.write(source + ",")
                nextline = f.readline()
                if(nextline[0] == "#"):
                    f.readline() #eat line after fourth # otherwise already eaten
                sequence = getdata(f,length)
                o.write(sequence + ",")
                structure = getdata(f,length)
                o.write(structure + ",")
                GC = countGC(sequence)
                o.write(str(GC) + ",")
                o.write(str(length) + ",")
                pairs = countPairs(structure)
                o.write(str(pairs) + ",")
                mean = pairs/length
                o.write(str(mean) + "\n")
                f.readline() #eat white line

            f.close()
            l.close()
        o.close()
        print("done")
    except ValueError as e:
        print(e);