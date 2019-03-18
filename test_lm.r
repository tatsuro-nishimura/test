# single linear regression
result <- lm(iris[,4]~iris[,3])
result$coefficient
summary(result)

# multiple linear regression
lm(iris[,4]~iris[,1]+iris[,2]+iris[,3])

# logistic regression
glm(c(iris[,5])%%2~iris[,1]+iris[,2]+iris[,3],family=binomial)

library(glmnet)
# Lasso regression
result <- cv.glmnet(as.matrix(iris[,1:3]),as.matrix(iris[,4],ncol=1),alpha = 1)
coefficients(result,s="lambda.min")

# Ridge regression
result <- cv.glmnet(as.matrix(iris[,1:3]),as.matrix(iris[,4],ncol=1),alpha = 0)
coefficients(result,s="lambda.min")

# multinomial logistic regression
result <- cv.glmnet(as.matrix(iris[,-5]),as.matrix(iris[,5],ncol=1), family="multinomial", type.multinomial="grouped")
pred <- predict(result, newx=as.matrix(iris[,-5]), type="class")
table(pred, iris[,5])
