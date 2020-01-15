from kinematics import Twist
from files import getEvents, getTeamsForEvent, getFilesForTeamForEvent
import sys
import matplotlib.pyplot as plt

# handle args
printout = False
if len(sys.argv) == 2:
    if sys.argv[1] == "p":
        printout = True


# Read file from STDIN
file = open("/dev/stdin").read()

# Split file to lines
lines = file.split("\n")[2:-1]

# Tracker for last datapoint
last = [0, 0, 0]  # L, R, t

# Plot trackers
data = []

# Print CSV header
print("left, right, dt")

# Parse each datapoint
for line in lines:

    # Convert line from CSV to datapoints
    x, y, t = line.split(",")

    # Convert datatype
    x, y, t = float(x), float(y), float(t)

    # Build a twist from current point, referencing the last
    d: Twist = Twist.fromTranslation(last[0], last[1], x, y)

    # Get wheelspeeds
    speeds = d.toWheelSpeeds()

    # Get dt
    dt = t - last[2]

    # Print the new datapoint
    if printout:
        print(
            f"{round(speeds[0] / 100, 2)}, {round(speeds[1] / 100, 2)}, {round(dt, 4)}")

    else:
        # Add to plot
        # data.append((speeds[0], speeds[1], dt))
        plt.plot(t, speeds[0], t, speeds[1])

    # Set last to current
    last[0] = speeds[0]
    last[1] = speeds[1]
    last[2] = t

plt.show()
# if not printout:
    