# import matplotlib.pyplot as plt
# input_values = [1, 2, 3, 4, 5]
# squares = [1, 4, 9, 16, 25]
# plt.style.use('seaborn')
# fig, ax = plt.subplots()


# # ax.scatter(2, 4)


# ax.scatter(2, 4, s=200)
# # Set chart title and label axes.
# ax.set_title("Square Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=14)
# # Set size of tick labels.
# ax.tick_params(axis='both', which='major', labelsize=14)

# # ax.plot(squares, linewidth=3)
# ax.plot(input_values, squares, linewidth=3)
# ax.scatter(input_values, squares, s=100)
# Set chart title and label axes.
# ax.set_title("Square Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=14)
# # Set size of tick labels.
# ax.tick_params(axis='both', labelsize=14)

# ax.plot(squares)
# plt.show()

# print(plt.style.available)

############################################################
# plt.style.use('seaborn')
# fig, ax = plt.subplots()
# ax.scatter(2, 4)
# plt.show()

##*******************************************************************
import matplotlib.pyplot as plt
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]
plt.style.use('seaborn')
fig, ax = plt.subplots()
# ax.scatter(x_values, y_values,s=10)
# ax.scatter(x_values, y_values, c='red',s=10)
# ax.scatter(x_values, y_values, c=(0, 0.8, 0),s=10)
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Set chart title and label axes.
# ax.set_title("Square Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=14)
# # Set size of tick labels.
# ax.tick_params(axis='both', labelsize=14)

# Set the range for each axis.
#the minimum and maximum values for the x-axis and the y-axis.
ax.axis([0, 1100, 0, 1100000])
plt.savefig('squares_plot.png', bbox_inches='tight')

plt.show()