flock.index <- function() {
  df.index <- read.csv("index.csv", header = TRUE)
  return(df.index)
}
