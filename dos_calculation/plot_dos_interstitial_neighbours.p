set terminal pngcairo enhanced font 'Arial, 12' size 800,600
set output 'interstitial_neighbors_dos.png'
set grid
set title "DOS of Interstitial Forming Atoms and Surrounding Atoms"
set xlabel "Energy [eV]"
set ylabel "DOS"
plot "interstitial_dos.dat" using 1:2 title "Interstitial Spin up" with lines ls 5, \
     "interstitial_dos.dat" using 1:3 title "Interstitial Spin down" with lines ls 10, \
     "neighbors_dos.dat" using 1:2 title "Neighbors Spin up" with lines ls 11, \
     "neighbors_dos.dat" using 1:3 title "Neighbors Spin down" with lines ls 12

