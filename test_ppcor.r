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

# calculate partial correlation coefficients by gramSchmidt
library(pracma)
cosine <- function(x,y){
  return(c(x%*%y)/sqrt(c(x%*%x)*c(y%*%y)))
}
pcor1 <- function(x,y,z,data){
  vecs <- scale(data)
  L_z_orth_basis <- gramSchmidt(vecs[,z])$Q #L means linear space
  vec_x_proj <- vecs[,x] - apply(L_z_orth_basis%*%diag(c((t(vecs[,x])%*%L_z_orth_basis))),1,sum)
  vec_y_proj <- vecs[,y] - apply(L_z_orth_basis%*%diag(c((t(vecs[,y])%*%L_z_orth_basis))),1,sum)
  return(cosine(vec_x_proj, vec_y_proj))
}
pcor1(1,2,c(3,4),iris[,-5])
