#simple simulation of optimal foraging 

#say there is some known ideal size around 40-60

#all strategies start as random or norm away from optimal value

#warning: this script will save generations number of photos to your wroking directory

library(ggplot2)
theme_set(theme_bw())

pop_size = 1000

#try unique strats (take away hashtag to try a different strat)

#strats <- runif(pop_size, 0, 100)
strats <- rnorm(pop_size, 20, 2)


carrying_capacity = 5000
mov_mean <- c()
generations = 250
vsd = 2 #this is the offspring variation

for (i in 1:generations){
  
  temp_strats <- c()
  df = data.frame(Strategy=strats)
  p <- ggplot(df, aes(x=Strategy)) + geom_histogram() + ggtitle(paste0("Generation ", i)) + xlim(0,100) + ylim(0, 1500)
  ggsave(file=paste0(i,".jpg"), plot = p, width = 8, height = 4.5, units = "in", dpi=300)
  
  for (j in 1:pop_size){
    
    if (strats[j]<=55 & strats[j]>=45) {
      temp_strats <- c(temp_strats, strats[j] + rnorm(1, 0, vsd), strats[j] + rnorm(1,0,vsd), strats[j] + rnorm(1,0,vsd))
    } else if (strats[j]<=65 & strats[j]>=35) {
      temp_strats <- c(temp_strats, strats[j] + rnorm(1, 0, vsd), strats[j] + rnorm(1,0,vsd))
    } else if (strats[j] <=95 & strats[j] >= 5) {
      temp_strats <- c(temp_strats, strats[j] + rnorm(1,0,vsd))
    } else {
      temp_strats <- temp_strats
    }
    
      
  }
  
  if(length(temp_strats)>=carrying_capacity){
    to_del <- length(temp_strats)-carrying_capacity
    to_del <- sample(length(temp_strats), to_del)
    temp_strats <- temp_strats[-to_del]
    }
  
  #print(length(temp_strats))
  mov_mean <- c(mov_mean, mean(strats))
  
  strats <- temp_strats
  
}

p <- ggplot(df, aes(x=Strategy)) + geom_histogram() + ggtitle(paste0("Generation ", i)) + xlim(0,100) + ylim(0, 1500)
ggsave(file=paste0(i,".jpg"), plot = p, width = 8, height = 4.5, units = "in", dpi=300)

plot(1:generations, mov_mean, type="l", xlab="Generation", ylab="Mean Phenotype")

