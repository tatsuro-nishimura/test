library(CausalImpact)
x <- arima.sim(n=200, list(arima=.99))
y <- 1.6*x + rnorm(200)
y[141:200] <- y[141:200] + 10
impact <- CausalImpact(cbind(y, x), c(1, 140), c(141, 200))
summary(impact)
plot(impact)
