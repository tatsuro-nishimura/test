library(devtools)
library(gtools)
library(DiagrammeR)
library(tseries)
source_url('https://raw.githubusercontent.com/cran/FIAR/master/R/partGranger.R')
pgranger <- function(ts, alpha=.05){
  n <- ncol(ts)
  partGranger(ts[,1:n],nx=1,ny=1,order=3)
  partGranger(ts[,1:n],nx=1,ny=3,order=3)
  cn <- colnames(ts)
  dotstr <- 'digraph causality {'
  for(i in 1:(n*(n-1))){
    perm0 <- permutations(n,2,1:n)[i,]
    perm <- c(perm0,setdiff(1:n,perm0))
    prob <- partGranger(ts[,perm],nx=1,ny=1,order=3)$prob
    if(prob <= alpha){
      arrow <- paste(cn[perm0[1]],'->',cn[perm0[2]])
      print(arrow)
      print(prob)
      dotstr <- paste0(dotstr,arrow,'[label="',round(prob,5),'     "];')
    }
  }
  dotstr <- paste0(dotstr, '}')
  grViz(dotstr)
}
pgranger(EuStockMarkets)
ts <- EuStockMarkets
cn <- colnames(ts)
n <- ncol(ts)
for (i in 1:n){
  print(cn[i])
  print(adf.test(EuStockMarkets[,i]))
}
for(i in 1:(n*(n-1))){
  perm0 <- permutations(n,2,1:n)[i,]
  print(paste(cn[perm0[1]], cn[perm0[2]]))
  print(po.test(EuStockMarkets[,perm0]))
}
pgranger(diff(EuStockMarkets),0.4)
