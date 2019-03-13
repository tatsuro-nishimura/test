library(prophet)
df <- data.frame(matrix(0,100,2))
colnames(df) <- c('ds', 'y')
df$ds <- paste0(1901:2000,'-01-01')
df$y <- 1:100 + 10*sin(1:100*pi/2) + rnorm(100)
# sin(1:100*pi/2) is equivalent to Im(1i^{1:100}) or rep(c(1,0,-1,0),25) mathematically
head(df)
m <- prophet(df)
future_df <- make_future_dataframe(m, 30, freq='year')
pred <- predict(m, future_df)
plot(m, pred)
pred$yhat
