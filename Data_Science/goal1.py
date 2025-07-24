import math

def calculate_p(px, py, pz):    #This function calculates the momentum of a particle given its components.
    # expects px, py, pz as arguments
    return math.sqrt(math.pow(px, 2) + math.pow(py, 2) + math.pow(pz, 2))

def calculate_pT (px, py):    #This function calculates the transverse momentum of a particle given its x and y components.    
    # expects px, py as arguments
    return math.sqrt(px**2 + py**2)

def calculate_pseudorapidity(pz, p):               #pseudorapidity is the n with a long end
    # expects pz, p as arguments
    theta = math.acos(pz / p)
    return -math.log(math.tan(theta / 2))

def calculate_azimuthal_angle():
    pass      #solve if you finish early
    # expects px, py as arguments

def check_type(pdg_code):      #this function checks the type of particle based on the pdg code
    if pdg_code == 211:
        print("This is a positive pion")
    elif pdg_code == -211:
        print("This is a negative pion")
    elif pdg_code == 111:
        print("This is neutral pion")
    else:
        print("This is not a pion of a ny kind")



# Open the input file
# Deschide fișierul de intrare
with open("data_science/output-Set0.txt", 'r') as infile:
    first_line = infile.readline().strip()
    event_id, num_particles = map(int, first_line.split())
    lines_list = [line.strip().split() for line in infile]

print(f"Event ID: {event_id} | Particule: {num_particles}")

# Parcurge fiecare particulă
for i in range(num_particles):
    particle_data = lines_list[i]
    if (len(particle_data) < 4):
        continue
    pdg_code = int(particle_data[3])
    px = float(particle_data[0])
    py = float(particle_data[1])
    pz = float(particle_data[2])
    print("Particulă:", check_type(pdg_code))
    p=calculate_p(px, py, pz)
    print("Pseudorapidity:", calculate_pseudorapidity(pz, p))
    print("pT:", calculate_pT (px, py))
