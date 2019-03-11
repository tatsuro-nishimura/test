library(prophet)
df <- data.frame(matrix(0,100,2))
colnames(df) <- c('ds', 'y')
df$ds <- paste0(1901:2000,'-01-01')
df$y <- 1:100 + rnorm(100)
head(df)
m <- prophet(df)
future_df <- make_future_dataframe(m, 30, freq='year')
pred <- predict(m, future_df)
plot(m, pred)
pred$yhat
