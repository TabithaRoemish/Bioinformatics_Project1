#to run infernal

wget eddylab.org/infernal/infernal-1.1.2.tar.gz
tar xf infernal-1.1.2.tar.gz
cd infernal-1.1.2 
./configure
make
make check

#to search Rfam database
wget ftp://ftp.ebi.ac.uk/pub/databases/Rfam/12.1/Rfam.cm.gz 
gunzip Rfam.cm.gz 
./cmpress Rfam.cm