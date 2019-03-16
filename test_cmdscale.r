mdscale_data<-cmdscale(dist(iris[,-5]))
plot(mdscale_data, col = iris[,5], pch = 16)
