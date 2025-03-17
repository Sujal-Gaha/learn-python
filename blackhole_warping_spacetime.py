import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

def blackhole_spacetime():
    # Define grid
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x, y)
    
    # Define gravitational well (simulated by a 1/sqrt function)
    r = np.sqrt(X**2 + Y**2)
    Z = -1 / (r + 0.1)  # Avoid division by zero
    
    # Create 3D plot
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='inferno', edgecolor='none')
    
    # Labels and aesthetics
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Spacetime Curvature")
    ax.set_title("Black Hole Warping Spacetime")
    ax.view_init(elev=60, azim=45)  # Adjust view angle
    
    # Celestial body orbiting the black hole
    orbit_radius = 3
    theta = np.linspace(0, 2 * np.pi, 100)
    orbit_x = orbit_radius * np.cos(theta)
    orbit_y = orbit_radius * np.sin(theta)
    orbit_z = -1 / (orbit_radius + 0.1)  # Match curvature
    
    planet, = ax.plot([], [], [], 'bo', markersize=6, label='Orbiting Body')
    
    def update(frame):
        planet.set_data([orbit_x[frame]], [orbit_y[frame]])
        planet.set_3d_properties([orbit_z])
        return planet,
    
    ani = animation.FuncAnimation(fig, update, frames=len(theta), interval=50, blit=True)
    
    plt.legend()
    plt.show()

# Run visualization
blackhole_spacetime()
