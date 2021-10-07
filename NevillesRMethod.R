poly.neville <- function(x, y, x0) {
  
  n <- length(x)
  q <- matrix(data = 0, n, n)
  q[,1] <- y
  
  for (i in 2:n) {
    for (j in i:n) {
      q[j,i] <- ((x0 - x[j-i+1]) * q[j,i-1] - (x0 - x[j]) * q[j-1,i-1]) / (x[j] - x[j-i+1])
    }
  }
  
  res <- list('Approximated value'=q[n,n], 'Neville iterations table'=q)
  return(res)
}

x <- c(-0.75,-0.5,-0.25,0)
y <- c(-0.07181250,-0.02475000,0.33493750,1.1010000)

print(poly.neville(x, y, -1/3))
