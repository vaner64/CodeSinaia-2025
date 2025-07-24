import math
import matplotlib.pyplot as plt
import numpy as np

threshold = 0.05

# Returns 1 for positive pion (211), -1 for negative pion (-211), 0 otherwise
def check_type(pdg_code):
    if pdg_code == 211:
        return 1
    elif pdg_code == -211:
        return -1
    else:
        return 0

# Returns the Poisson uncertainty for a given average
def poisson_distribution(average):

    # Poisson uncertainty is sqrt(N), where N is the average count
    return np.sqrt(average)

# Returns the absolute difference between two numbers
def difference(no_1, no_2):
    return abs(no_1 - no_2)  # TODO: Implement this function  # TODO: Implement this function

def combined_uncertainty(no_1, no_2):
    # Combined uncertainty for independent Poisson: sqrt(sigma1^2 + sigma2^2)
    return np.sqrt(no_1 + no_2)

# Returns the significance of the difference
def significance(no_1, no_2, comb_uncertainty):
    # Significance = difference / combined uncertainty
    diff = difference(no_1, no_2)
    if comb_uncertainty == 0:
        return 0
    return diff / comb_uncertainty

import os
import time

max_particles = 300000
start_time = time.time()
batch_size = 1000

total_poz = 0
total_neg = 0
poz_per_batch = []
neg_per_batch = []

try:
    with open("data_science/output-Set1.txt", 'r') as infile:
        first_line = infile.readline().strip()
        event_id, num_particles = first_line.split()[:2]
        event_id = int(event_id)
        num_particles = int(num_particles)
        count = 0
        batch_poz = 0
        batch_neg = 0
        for line in infile:
            if count >= max_particles:
                break
            parts = line.strip().split()
            if not parts:
                continue
            # Assume PDG code is always the last value in the line
            try:
                pdg_code = int(parts[-1])
            except ValueError:
                continue
            t = check_type(pdg_code)
            if t == 1:
                total_poz += 1
                batch_poz += 1
            elif t == -1:
                total_neg += 1
                batch_neg += 1
            count += 1
            if count % batch_size == 0:
                poz_per_batch.append(batch_poz)
                neg_per_batch.append(batch_neg)
                batch_poz = 0
                batch_neg = 0
        # Add last batch if not full
        if batch_poz > 0 or batch_neg > 0:
            poz_per_batch.append(batch_poz)
            neg_per_batch.append(batch_neg)
except FileNotFoundError:
    print(f"File data_science/output-Set1.txt not found in {os.getcwd()}")
    exit(1)
except IOError as e:
    print(f"Error reading file: {e}")
    exit(1)

num_batches = len(poz_per_batch)
avg_poz = total_poz / num_batches if num_batches else 0
avg_neg = total_neg / num_batches if num_batches else 0
poisson_poz = poisson_distribution(total_poz)
poisson_neg = poisson_distribution(total_neg)
diff = difference(total_poz, total_neg)
comb_uncert = combined_uncertainty(total_poz, total_neg)
sig = significance(total_poz, total_neg, comb_uncert)

print(f"In {count} total particles, we had {total_poz} positive pions and {total_neg} negative pions.")
print(f"There is an average of {avg_poz:.6f} positive pions per batch.")
print(f"There is an average of {avg_neg:.6f} negative pions per batch.")
print(f"The Poisson uncertainty for the positive pions is {poisson_poz:.2f}")
print(f"The Poisson uncertainty for the negative pions is {poisson_neg:.2f}")
print(f"There are {diff} more positive pions than negative pions.")
print(f"The combined uncertainty of the total amount of positive and negative pions is {comb_uncert:.2f}")
print(f"The significance is {sig:.2f}")
if sig > threshold:
    print("The significance is very large compared to the threshold.")
else:
    print("The significance is not large compared to the threshold.")

# Plotting
plt.figure(figsize=(10,6))
plt.plot([i*batch_size for i in range(num_batches)], poz_per_batch, label="Positive pions", color="Blue")
plt.plot([i*batch_size for i in range(num_batches)], neg_per_batch, label="Negative pions", color="Red")
plt.xlabel("Particle number")
plt.ylabel(f"Number of pions in each batch of {batch_size}")
plt.title("Positive and Negative Pions per Batch")
plt.legend()
plt.tight_layout()
plt.show()
end_time = time.time()
print(f"Total execution time: {end_time - start_time:.2f} seconds")




