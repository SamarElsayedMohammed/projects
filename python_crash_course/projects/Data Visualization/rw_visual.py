import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
# Make a random walk.
    rw = RandomWalk(50_000)
    # rw = RandomWalk()
    rw.fill_walk()
    # rw_visual.py318 Chapter 15
    # Plot the points in the walk.
    plt.style.use('classic')

    fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
    # fig, ax = plt.subplots(figsize=(15, 9))

    # fig, ax = plt.subplots()

    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,edgecolor='none', s=1)

    # ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,edgecolors='none', s=15)

        # Emphasize the first and last points.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',s=100)


    # Remove the axes.


    # ax.scattery(rw.x_values, rw.y_values, s=15)
    plt.show()
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break