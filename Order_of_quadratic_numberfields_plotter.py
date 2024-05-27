import matplotlib.pyplot as plt
import numpy as np

def plot_quadratic_field_lattice(d, connect_dots='solid'):
    """
    Plot the lattice of a quadratic number field.
    
    Parameters:
    - d: Square-free integer for the quadratic field Q(sqrt(d)).
    - connect_dots: 'solid' for solid lines, 'dashed' for dashed lines, 'none' to hide connections.
    """
    # Check if d is square-free
    if any(d % p**2 == 0 for p in range(2, int(np.sqrt(abs(d))) + 1)):
        raise ValueError("d must be a square-free integer.")
    
    # Determine omega based on d
    if d % 4 == 1:
        omega_real = 0.5
        omega_imag = np.sqrt(abs(d)) / 2
        omega_tex = r"$\frac{1+\sqrt{"+str(d)+"}}{2}$"
    else:
        omega_real = 0
        omega_imag = np.sqrt(abs(d))
        omega_tex = r"$\sqrt{"+str(d)+"}$"

    # Prepare the figure
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.axhline(0, color='gray', lw=0.5)
    ax.axvline(0, color='gray', lw=0.5)
    
    # Set initial plot limits
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    
    # Draw plot to get the actual limits
    plt.draw()
    
    # Get actual limits
    x_limits = ax.get_xlim()
    y_limits = ax.get_ylim()
    
    # Calculate appropriate range for lattice points
    x_range = int(np.ceil(max(abs(x_limits[0]*1.5), abs(x_limits[1]*1.5))))
    y_range = int(np.ceil(max(abs(y_limits[0]*1.5), abs(y_limits[1]*1.5)) / omega_imag))

    # Loop to plot the lattice points and connect them
    for x in range(-x_range, x_range + 1):
        for y in range(-y_range, y_range + 1):
            # Calculate coordinates
            coordx = x + omega_real * y
            coordy = omega_imag * y
            plt.plot(coordx, coordy, 'bo')
            
            # Connect points horizontally
            if connect_dots != 'none' and y < y_range:
                nextx = x + omega_real * (y + 1)
                nexty = omega_imag * (y + 1)
                linestyle = '--' if connect_dots == 'dashed' else '-'
                plt.plot([coordx, nextx], [coordy, nexty], 'b', linestyle=linestyle, lw=0.5)
            
            # Connect points vertically
            if connect_dots != 'none' and x < x_range:
                nextx = (x + 1) + omega_real * y
                nexty = omega_imag * y
                linestyle = '--' if connect_dots == 'dashed' else '-'
                plt.plot([coordx, nextx], [coordy, nexty], 'b', linestyle=linestyle, lw=0.5)

    # Vertices of the fundamental parallelepiped
    vertices = np.array([
        [0, 0],
        [1, 0],
        [1 + omega_real, omega_imag],
        [omega_real, omega_imag]
    ])
    
    # Fill the fundamental parallelepiped
    ax.fill(vertices[:, 0], vertices[:, 1], 'gray', alpha=0.5)

    # Label some points
    plt.text(0, 0, '$0$', fontsize=14, ha='right', color='red')
    plt.text(1, omega_imag,"$1 + $"+ omega_tex, fontsize=14, ha='left', color='red')
    plt.text(omega_real, omega_imag, omega_tex, fontsize=14, ha='right', color='red')

    # Adjust the final plot settings
    ax.set_xlim(x_limits)
    ax.set_ylim(y_limits)
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_title(f'Ring of integers of the Quadratic Number Field $\\mathbb{{Q}}(\\sqrt{{{d}}})$')
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)
    ax.set_aspect('equal', adjustable='box')

    # Show the plot
    plt.show()

# Example usage:
d = -3  # Change this value for different d
plot_quadratic_field_lattice(d, connect_dots='dashed')  # Options: 'solid', 'dashed', 'none'