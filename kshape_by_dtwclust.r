# using kshape method by dtwclust
library(tidyverse)
library(dtwclust)

series_list = data.frame(a1 = c(0,0,0,1,1,1),
                       a2 = c(1,1,1,0,0,0),
                       a3 = c(0,0,1,1,1,0),
                       a4 = c(1,1,1,0,0,0),
                       a5 = c(1,1,1,0,0,0),
                       a6 = c(1,2,1,1,1,1),
                       a7 = c(1,1,1,1,1,0)) %>% t() %>% as.data.frame()

res <- tsclust(series = series_list,
               type = "partitional",
               preproc = zscore,
               distance = "sbd",
               centroid = "shape",
               k = 2)
df_res <- data.frame(cluster = res@cluster,
                     centroid_dist = res@cldist)

#drawing centroids
centroids <- res@centroids
for(i in 1:length(centroids)){
  ts_centroid <- centroids[i] %>% unlist()
  plot(1:length(ts_centroid), ts_centroid, type='l', xlab='time', ylab='centroid(z-score)')
}
