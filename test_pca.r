pca_data <- prcomp(iris[,-5], scale = T)$x[,1:2]
plot(pca_data, col = iris[,5], pch = 16)
