#!/bin/bash
paste DOS121 DOS123 | \
awk '{for (i=1;i<=NF;i+=4) printf("%f ", $i); for (j=2;j<=NF;j+=4) printf("%f ", $j+$j+4); print ""}' > interstitial_dos.dat

