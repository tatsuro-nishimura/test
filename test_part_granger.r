library(devtools)
source_url('https://raw.githubusercontent.com/cran/FIAR/master/R/partGranger.R')
partGranger(EuStockMarkets[,1:4],nx=1,ny=1,order=3)
partGranger(EuStockMarkets[,1:4],nx=1,ny=3,order=3)
for(i in 1:24){
  perm <- permutations(4,4,1:4)[i,]
  print(perm)
  print(partGranger(EuStockMarkets[,perm],nx=1,ny=1,order=3))
}
