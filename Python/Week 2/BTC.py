
import numpy as np
import matplotlib.pyplot as plt

# let n be the number of days
n = 1
# Let the mining speed be 1 TH/s (free plan)
mining_speed = 1  # in TH/s this will give us .47$ per day
# let money be the amount of money we have and start with 0 @ day 1
money_in_the_wallet = 0
keep_up = []
time = []  # Store time for x-axis
mining_speeds = []  # Store mining speed for y-axis

# Initialize time and mining speed lists
time.append(n)
mining_speeds.append(mining_speed)

#/*-----------------------------------------------------------*/

while money_in_the_wallet < 30:
    n += 1
    money_in_the_wallet += 0.47
    keep_up.append(money_in_the_wallet)
    # Save current state
    time.append(n)
    mining_speeds.append(mining_speed)

def invest(money, mining_speed):
    money -= 30  # Subtract 30$ for investment
    mining_speed += 2.820  # Increase mining speed by 2.820 TH/s
    return money, mining_speed  # Return updated values

while mining_speed < 100:
    while money_in_the_wallet < 30:
        n += 1
        money_in_the_wallet += 0.47
        keep_up.append(money_in_the_wallet)
        # Save current state
        time.append(n)
        mining_speeds.append(mining_speed)
    
    money_in_the_wallet, mining_speed = invest(money_in_the_wallet, mining_speed)  # Update values from invest
    # Save new mining speed
    time.append(n)
    mining_speeds.append(mining_speed)

# Plot the results
plt.plot(time, mining_speeds, label='Mining Speed (TH/s)', marker='o')
plt.title('Mining Speed Over Time')
plt.xlabel('Time (days)')
plt.ylabel('Mining Speed (TH/s)')
plt.legend()
plt.grid()
plt.show()
