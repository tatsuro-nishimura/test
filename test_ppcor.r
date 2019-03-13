# calculate partial correlation coefficients by ppcor
library(ppcor)
result <- pcor(iris[,-5])$estimate
result
pc_12_34_1 <- result[1,2]
pc_12_34_1

# calculate partial correlation coefficients by recursive formula
calc0 <- function(x_12,x_13,x_23){
  return((x_12 - x_13*x_23)/sqrt((1-x_13^2)*(1-x_23^2)))
}
pcor0 <- function(x,y,z){
  return(calc0(cor(x,y),cor(x,z),cor(y,z)))
}

pc_12_3 <- pcor0(iris[,1],iris[,2],iris[,3])
pc_14_3 <- pcor0(iris[,1],iris[,4],iris[,3])
pc_24_3 <- pcor0(iris[,2],iris[,4],iris[,3])
pc_12_34_2 <- calc0(pc_12_3,pc_14_3,pc_24_3)
pc_12_34_2

pc_12_4 <- pcor0(iris[,1],iris[,2],iris[,4])
pc_13_4 <- pcor0(iris[,1],iris[,3],iris[,4])
pc_23_4 <- pcor0(iris[,2],iris[,3],iris[,4])
pc_12_34_3 <- calc0(pc_12_4,pc_13_4,pc_23_4)
pc_12_34_3

pc_12_34_1 - pc_12_34_2 == 0
pc_12_34_2 - pc_12_34_3 == 0
abs(pc_12_34_2 - pc_12_34_3) < 10^{-10}
