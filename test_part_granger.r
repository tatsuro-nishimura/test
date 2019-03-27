library(devtools)
library(gtools)
library(DiagrammeR)
source_url('https://raw.githubusercontent.com/cran/FIAR/master/R/partGranger.R')
ts <- EuStockMarkets
n <- ncol(ts)
partGranger(ts[,1:n],nx=1,ny=1,order=3)
partGranger(ts[,1:n],nx=1,ny=3,order=3)
alpha <- 0.05
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
