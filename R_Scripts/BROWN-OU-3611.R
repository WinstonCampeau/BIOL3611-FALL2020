y <- c(0)
ou <- c(0)
dt = 1/1000
theta = 10
sig = 1

for_hist_OU <- c()
for_hist_BM <- c()

plot(x = 1:500, xlim=c(1,1000), ylim=c(-0.1, 0.1), xlab="Evolutionary Time Step", ylab="Phenotype")
for(j in 1:1000){
for(i in 1:1000){
  
  temp_noise <- rnorm(1, mean=0, sd=1)*dt
  y[i+1] = y[i] + temp_noise
  ou[i+1] = ou[i] + -theta*ou[i]*dt + sig*temp_noise
}
  
  for_hist_OU[j] <- ou[500]
  for_hist_BM[j] <- y[500]
    
  points(y, type="l", col="blue")
  points(ou, type="l", col="red")
}

hist(for_hist_BM, xlab = "Phenotype at Last Evolutionary Time Step", main="Brownian Motion Model of Evolution", breaks=20)
hist(for_hist_OU, xlab = "Phenotype at Last Evolutionary Time Step", main="Ornstein-Uhlenbeck Model of Evolution", breaks=20)
  