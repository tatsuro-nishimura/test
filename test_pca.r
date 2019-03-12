result <- prcomp(iris[,-5], scale = T)
pca_data <- result$x[,1:2]
plot(pca_data, col = iris[,5], pch = 16)
