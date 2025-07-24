import math
import time
import matplotlib.pyplot as plt
from scipy.stats import f_oneway

# Calculates average and statistical uncertainty
def calculate_average_and_uncertainty(total, count):
    if count == 0:
        return 0, 0
    avg = total / count
    uncertainty = math.sqrt(total) / count if count > 0 else 0
    return avg, uncertainty

# Determines particle type based on PDG code (1 for positive pion, -1 for negative pion, 0 otherwise)
def check_type(pdg_code):
    if pdg_code == 211:
        return 1
    elif pdg_code == -211:
        return -1
    else:
        return 0
    
start_time=time.time()

batch_size = 1000
max_particles = 100000  # Limit to first 50000 particles per file
file_paths = [
    "data_science/output-Set1.txt",
    "data_science/output-Set2.txt",
    "data_science/output-Set3.txt",
    "data_science/output-Set4.txt",
    "data_science/output-Set5.txt",
    "data_science/output-Set6.txt", 
    "data_science/output-Set7.txt",
    "data_science/output-Set8.txt",
    "data_science/output-Set9.txt",
    "data_science/output-Set10.txt",


    # Add more files as needed
]

threshold = 0.05
avg_F_static_list = []
avg_P_list = []
avg_pT_list = []
avg_p_list = []
file_labels = []
start_time = time.time()

for filename in file_paths:
    total_poz = 0
    total_neg = 0
    total_events = 0
    batch_poz = 0
    batch_neg = 0
    batch_events = 0
    sum_pT = 0
    sum_p = 0
    try:
        with open(filename, 'r') as infile:
            first_line = infile.readline().strip()
            event_id, num_particles = first_line.split()[:2]
            event_id = int(event_id)
            num_particles = int(num_particles)
            particle_count = 0
            for line in infile:
                if particle_count >= max_particles:
                    break
                parts = line.strip().split()
                if not parts or len(parts) < 4:
                    continue
                try:
                    pdg_code = int(parts[-1])
                    px = float(parts[0])
                    py = float(parts[1])
                    pz = float(parts[2])
                except ValueError:
                    continue
                t = check_type(pdg_code)
                if t == 1:
                    batch_poz += 1
                elif t == -1:
                    batch_neg += 1
                # Calculate pT and p for each particle
                pT = math.sqrt(px**2 + py**2)
                p = math.sqrt(px**2 + py**2 + pz**2)
                sum_pT += pT
                sum_p += p
                batch_events += 1
                particle_count += 1
                if batch_events % batch_size == 0:
                    total_poz += batch_poz
                    total_neg += batch_neg
                    total_events += batch_events
                    batch_poz = 0
                    batch_neg = 0
                    batch_events = 0
            # Add any remaining batch
            if batch_events > 0:
                total_poz += batch_poz
                total_neg += batch_neg
                total_events += batch_events
    except FileNotFoundError:
        print(f"File {filename} not found.")
        continue
    except IOError as e:
        print(f"Error reading file {filename}: {e}")
        continue

    avg_poz, unc_poz = calculate_average_and_uncertainty(total_poz, total_events)
    avg_neg, unc_neg = calculate_average_and_uncertainty(total_neg, total_events)
    mean_diff = avg_poz - avg_neg
    comb_uncert = math.sqrt(unc_poz**2 + unc_neg**2)
    significance = mean_diff / comb_uncert if comb_uncert != 0 else 0

    # F static = mean_diff (difference in averages)
    avg_F_static_list.append(mean_diff)
    # P value = significance
    avg_P_list.append(significance)
    # Average pT and p
    avg_pT = sum_pT / total_events if total_events else 0
    avg_p = sum_p / total_events if total_events else 0
    avg_pT_list.append(avg_pT)
    avg_p_list.append(avg_p)
    file_labels.append(filename.split('/')[-1])

# ANOVA for average pT and p across files
pt_groups = []
p_groups = []
for filename in file_paths:
    pt_vals = []
    p_vals = []
    try:
        with open(filename, 'r') as infile:
            first_line = infile.readline().strip()
            event_id, num_particles = first_line.split()[:2]
            event_id = int(event_id)
            num_particles = int(num_particles)
            particle_count = 0
            for line in infile:
                if particle_count >= max_particles:
                    break
                parts = line.strip().split()
                if not parts or len(parts) < 4:
                    continue
                try:
                    px = float(parts[0])
                    py = float(parts[1])
                    pz = float(parts[2])
                except ValueError:
                    continue
                pt_vals.append(math.sqrt(px**2 + py**2))
                p_vals.append(math.sqrt(px**2 + py**2 + pz**2))
                particle_count += 1
    except Exception:
        continue
    pt_groups.append(pt_vals)
    p_groups.append(p_vals)

# One-way ANOVA for pT
f_stat_pt, p_value_pt = f_oneway(*pt_groups)
print(f"ANOVA for pT: F-statistic = {f_stat_pt:.4f}, p-value = {p_value_pt:.4g}")


# Print per-file results using collected statistics
print("\nPer-file results:")
for i, label in enumerate(file_labels):
    print(f"\nResults for {label}:")
    print(f"  Mean difference (F static): {avg_F_static_list[i]:.6f}")
    print(f"  Significance (P value): {avg_P_list[i]:.2f} sigma")
    print(f"  Average pT: {avg_pT_list[i]:.6f}")
    print(f"  Average p: {avg_p_list[i]:.6f}")
    if abs(avg_P_list[i]) > threshold:
        print("  The difference is statistically significant.")
    else:
        print("  The difference is not statistically significant.")


# Plot 1: Average F static and P value per file
plt.figure(figsize=(8,5))
plt.plot(file_labels, avg_F_static_list, marker='o', label='Average F static')
plt.plot(file_labels, avg_P_list, marker='s', label='Average P value')
plt.xlabel('File')
plt.ylabel('Value')
plt.title('Average F static and P value per file')
plt.legend()
plt.tight_layout()
plt.show()

# Plot 2: Average pT and p per file
plt.figure(figsize=(8,5))
plt.plot(file_labels, avg_pT_list, marker='o', label='Average pT')
plt.plot(file_labels, avg_p_list, marker='s', label='Average p')
plt.xlabel('File')
plt.ylabel('Value')
plt.title('Average pT and p per file')
plt.legend()
plt.tight_layout()
plt.show()


end_time=time.time()
print(f"Total processing time: {end_time - start_time:.2f} seconds")
