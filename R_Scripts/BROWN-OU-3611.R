y <- c(0)                   #Initiate the Brownian Motion (BM) Process
ou <- c(0)                  #Initiate the Orstein-Uhlenbeck (OU) Process
length_of_process <- 1000   #Length of all processes (the number of 'evolutionary time steps')
dt <- 1/length_of_process   #Magnitude of each time step
sig <- 1                    #This can alter the magnitude the underlying white noise process
num_processes <- 100        #How many processes will be constructed 

# Alternatively, you might consider a theta which varies over time. i.e. should/could theta reflect a fluctuating environment? 

packet <- c(1,1,1,1,10)                        #Does this look any different from an average theta of sum(packet)/length(packet) ?
theta = rep(packet, length_of_process/packet)  #This repeats the packet for a 1000 time steps
theta = rnorm(length_of_process, 0, 1)         #What is theta is pulled from a normal distribution? 
theta = rep(c(-1,1), length_of_process/2)      #What if the environment fluctuates in equal opposite forces? What happens if these are larger than 1?
theta = rep(10, length_of_process)             #Use this to test any baseline hypothesis you have: What if 0, -1, -100, average of packet? Etc.
theta = 1:length_of_process/150                #What if theta gets larger with time?
theta = length_of_process:1/150                #What if theta gets smaller with time?
theta = c((length_of_process/2):1/100, -1:-(length_of_process/2)/100) #What if theta gets goes from large to negatively large?

########################################################################################################################

for_hist_OU <- c() #Stores the last value of each OU process
for_hist_BM <- c() #Similarly, for each BM process

par(mfrow=c(1,2))  #Partitions the plots in to 1 row, 2 columns (left is processes, right is sumperimposed histograms)
plot(x = 1:1000, xlim=c(1,1000), ylim=c(-0.3, 0.3), xlab="Evolutionary Time Step", ylab="Phenotype") #Initiates the first plot
for(j in 1:num_processes){    
for(i in 1:1000){
  
  temp_noise <- rnorm(1, mean=0, sd=1)*dt
  y[i+1] = y[i] + temp_noise
  ou[i+1] = ou[i] + -theta[i]*ou[i]*dt + sig*temp_noise
}
  
  for_hist_OU[j] <- ou[1000]
  for_hist_BM[j] <- y[1000]
      
  points(y, type="l", col="blue") #These two add the processes in sequence
  points(ou, type="l", col="red")
}

#All of the below is for plotting

legend("topright", legend=c("Brownian", "OU"), lty = 1, col=c("blue", "red"), inset = 0.05, cex=0.8)

max_lim <- max(for_hist_OU, for_hist_BM)
min_lim <- min(for_hist_OU, for_hist_BM)

x_limits = c(min_lim, max_lim)  

BM <- hist(for_hist_BM, breaks=20, plot=FALSE)
OU <- hist(for_hist_OU, breaks=20, plot=FALSE)

y_limits <- c(min(BM$counts, OU$counts), max(BM$counts, OU$counts))

c1 <- rgb(0,0,255, max = 255, alpha = 150, names = "blue")
c2 <- rgb(255,0,0, max = 255, alpha = 150, names = "red")
plot(BM, col = c1, ylim = y_limits, xlim = x_limits, xlab = "Phenotype", main = "")
plot(OU, col = c2, add = TRUE)
legend("topright", legend=c("Brownian", "OU"), lty = 1, col=c(c1, c2), inset = 0.05, cex = 0.8)

  
