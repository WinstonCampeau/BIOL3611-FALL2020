#protoyping levy dust; a mathematical example of vegetation dispersal

# Kenkel, N., & Irwin, A. (1994). Fractal analysis of dispersal. Abstracta Botanica, 18(2), 79-84. http://www.jstor.org/stable/43519530

r_o <- 0.001 # minimum flight ditance -- pretty arbitrary because you can scale it with minmax
D <- 2 # fractal dimension (values between 1 and 2 are the most interesting)
r <- c() # empty vector to be populated with the proceeding 'for' loop

for(i in 1:5000){
  x <- runif(1, 0, 1)
  r[i] <- r_o*((1-x)^(-1/D))
}

# min max, vect is for r, a is the new minimum, b is the new maximum

minmax <- function(vect, a, b){
  output <- c()
  mini = min(vect)
  maxi = max(vect)
  
  for(i in 1:length(vect)){
    
    output[i] <- a + ((vect[i] - mini)*(b-a))/(maxi - mini)
    
  }
  return(output)
}

# converting to cartersian from polar

x <- c(0)
y <- c(0)

for(i in 1:length(r)){
  
  test = runif(1,0,2*pi)
  x[i+1] <- x[i] + r[i]*cos(test)   
  y[i+1] <- y[i] + r[i]*sin(test)
  
}

# scaling to new dimensions and converting to integers 

x <- minmax(x, 0, 250)
y <- minmax(y, 0, 250)
x <- round(x)
y <- round(y)

plot(x, y, cex = 0.01, pch=19)

   




