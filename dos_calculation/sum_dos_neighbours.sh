#!/bin/bash
paste DOS201 DOS93 DOS42 DOS150 | \
awk '{for (i=1;i<=NF;i+=4) printf("%f ", $i); for (j=2;j<=NF;j+=4) printf("%f ", $j+$j+4+$j+8+$j+12); print ""}' > neighbors_dos.dat

