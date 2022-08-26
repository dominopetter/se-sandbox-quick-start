# Import dependencies
import random
import matplotlib.pyplot as plt
import json
import os

# Print to console/stdout
print("Hello, {0}!".format(os.environ['DOMINO_PROJECT_OWNER']))


# Define a helper function to generate a random number
def random_number(start, stop):
    return random.uniform(start, stop)


# Plot the values of random points
x = random.sample(range(1000), 100)
xbins = [0, len(x)]
plt.bar(range(0, 100), x)
plt.show()
plt.savefig('results/myHistogramFromPython.png', format='png')

# Adding json output while using a git based project zx12345678
# Generate and save some key statistics to dominostats.json
# Learn more at https://docs.dominodatalab.com/en/latest/reference/runs/Diagnostic_statistics_with_dominostats.json.html
r2 = round(random_number(0, 1), 4)
p = round(random_number(0, 1), 4)
# Modified the json file to output to Artifacts
with open('/mnt/artifacts/dominostats.json', 'w') as f:
    f.write(json.dumps({"R^2": r2, "p-value": p}))