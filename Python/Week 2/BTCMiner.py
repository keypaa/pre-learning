import numpy as np
import matplotlib.pyplot as plt
# Let be the mining speed be 1 TH/s (free plan)
mining_speed = 1 # in TH/s this will give us .47$ per day
# let money be the amount of money we have and start with 0 @ day 1
money_in_the_wallet = 0
keep_up_mining_speed = []
keep_up_time = []

keep_up_mining_speed.append(mining_speed)
day = 0
keep_up_time.append(day)
money_per_day = 0.47


while mining_speed < 100:
  while money_in_the_wallet < 30:
    day +=1
    money_in_the_wallet += money_per_day
    #print(money_in_the_wallet)
    keep_up_time.append(day)
    keep_up_mining_speed.append(mining_speed)

  money_in_the_wallet = money_in_the_wallet - 30
  mining_speed += 2.820
  money_per_day += 0.86
  keep_up_mining_speed.append(mining_speed)
  keep_up_time.append(day)
print(day)
print("mining speed", keep_up_mining_speed)
print("time", keep_up_time)
#####################################################################
# 188 days to reach the goal of 100TH/s
plt.plot(keep_up_time, keep_up_mining_speed, label='Mining Speed (TH/s)', marker='o')
plt.title('Mining Speed Over Time')
plt.xlabel('Time (days)')
plt.ylabel('Mining Speed (TH/s)')
plt.legend()
plt.grid()
plt.show()
