# calculate partial correlation coefficients by ppcor
library(ppcor)
result <- pcor(iris[,-5])$estimate
result[1,2]

# calculate partial correlation coefficients by recursive formula
calc0 <- function(x_12,x_13,x_23){
  return((x_12 - x_13*x_23)/sqrt((1-x_13^2)*(1-x_23^2)))
}
pcor0 <- function(x,y,z){
  return(calc0(cor(x,y),cor(x,z),cor(y,z)))
}

p_12_3 <- pcor0(iris[,1],iris[,2],iris[,3])
p_14_3 <- pcor0(iris[,1],iris[,4],iris[,3])
p_24_3 <- pcor0(iris[,2],iris[,4],iris[,3])
calc0(p_12_3,p_14_3,p_24_3)

p_12_4 <- pcor0(iris[,1],iris[,2],iris[,4])
p_13_4 <- pcor0(iris[,1],iris[,3],iris[,4])
p_23_4 <- pcor0(iris[,2],iris[,3],iris[,4])
calc0(p_12_4,p_13_4,p_23_4)
