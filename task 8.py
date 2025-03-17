import matplotlib.pyplot as plt

x = ["sat", "sun", "mon", "tue", "wed", "thu", "fri"]
y = [30, 25, 23, 27, 29, 22,20]


plt.plot(x, y, marker='+', linestyle='--', color='black',label="Temperature")
plt.title(" The temperature variation over a week")
plt.xlabel("Days of week")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.show()