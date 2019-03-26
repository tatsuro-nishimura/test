library(devtools)
source_url('https://raw.githubusercontent.com/cran/FIAR/master/R/partGranger.R')
n <- 4
partGranger(EuStockMarkets[,1:n],nx=1,ny=1,order=3)
partGranger(EuStockMarkets[,1:n],nx=1,ny=3,order=3)
for(i in 1:(n*(n-1))){
  perm <- permutations(n,2,1:n)[i,]
  perm <- c(perm,setdiff(1:n,perm))
  prob <- partGranger(EuStockMarkets[,perm],nx=1,ny=1,order=3)$prob
  if(prob <= 0.05){
    print(perm)
    print(prob)
  }
}
