# single linear regression
result <- lm(iris[,4]~iris[,3])
result$coefficient
summary(result)

# multiple linear regression
lm(iris[,4]~iris[,1]+iris[,2]+iris[,3])

# logistic regression@# y ~ (1+exp(-(a1*x1+a2*x2+....)))^{-1}
glm(c(iris[,5])%%2~iris[,1]+iris[,2]+iris[,3],family=binomial)

library(glmnet)
# Lasso regression
result <- cv.glmnet(as.matrix(iris[,1:3]),as.matrix(iris[,4],ncol=1),alpha = 1)
coefficients(result,s="lambda.min")

# Ridge regression
result <- cv.glmnet(as.matrix(iris[,1:3]),as.matrix(iris[,4],ncol=1),alpha = 0)
coefficients(result,s="lambda.min")
