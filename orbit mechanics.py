import numpy as np

# 1. THE PHYSICS CONSTANTS (First Principles)
G = 6.6743e-11          # Gravitational constant (m^3 kg^-1 s^-2)
M_EARTH = 5.972e24      # Mass of the Earth (kg)
R_EARTH = 6.371e6       # Radius of the Earth (meters)

# 2. INITIAL CONDITIONS (Setting up our Satellite)
# Place the satellite in Low Earth Orbit (LEO) - 400 km above surface
altitude = 400000 
r_initial = R_EARTH + altitude

# Calculate the exact velocity needed for a stable circular orbit (v = sqrt(GM/r))
v_orbital = np.sqrt((G * M_EARTH) / r_initial)

# State vectors: [x, y] position and [vx, vy] velocity
position = np.array([r_initial, 0.0])
velocity = np.array([0.0, v_orbital])

# Time configuration
dt = 10.0               # Step size: calculate position every 10 seconds
total_time = 5500       # Roughly 92 minutes (one full orbit)

print(f"🚀 Launching simulation... Target Orbital Velocity: {v_orbital:.2f} m/s\n")

# 3. THE SIMULATION LOOP (The Engineering & Coding)
for step in range(0, total_time, int(dt)):
    # Calculate distance from Earth's center
    r_vector = np.linalg.norm(position)
    
    # Check if the satellite crashed into Earth
    if r_vector < R_EARTH:
        print("💥 Collision! The satellite burned up in the atmosphere.")
        break
        
    # Newton's Law of Universal Gravitation: F = G*(M1*M2)/r^2
    # Acceleration vector: a = - (G * M_Earth / r^3) * position_vector
    acceleration = - (G * M_EARTH / (r_vector**3)) * position
    
    # Update Physics State using Coding Logic (Euler-Cromer Method)
    velocity += acceleration * dt
    position += velocity * dt
    
    # Print status every 15 minutes of simulated time
    if step % 900 == 0:
        current_altitude_km = (r_vector - R_EARTH) / 1000
        speed_km_s = np.linalg.norm(velocity) / 1000
        print(f"Time: {step:4d}s | Altitude: {current_altitude_km:.1f} km | Speed: {speed_km_s:.2f} km/s")

print("\n🌍 Orbit completed successfully!")
