result <- prcomp(iris[,-5], scale = T)
#'scale=T': using correlation matrix
#default: using covariance matrix
summary(result)
data_PC1_2 <- result$x[,1:2]
plot(data_PC1_2, col = iris[,5], pch = 16)
