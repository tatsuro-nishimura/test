# try Augmented Dickey-Fuller Test
library(tseries)
adf.test(rnorm(10000))
adf.test(cumsum(rnorm(10000)))
