import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.cm as cm
from matplotlib.animation import PillowWriter

# Define the parameters for the Lissajous curves
parameters = [
    (1, 2, np.pi / 2),
    (3, 2, np.pi / 2),
    (3, 4, np.pi / 2),
    (5, 4, np.pi / 2),
    (2, 3, np.pi / 4),  # Additional parameters
    (4, 3, np.pi / 4)   # Additional parameters
]

t = np.linspace(0, 2 * np.pi, 500)

# Create a 2x3 grid of subplots
fig, axs = plt.subplots(2, 3, figsize=(15, 10))

anis = []

def update(num, x, y, scat, ax, a, b, delta):
    ax.clear()
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_frame_on(False)
    
    color = cm.jet(float(num) / len(x) - 0.001)
    scat = ax.scatter(x[:num], y[:num], color=color, s=5)  # Reduced marker size
    
    ax.text(1.8, 1.5, f'a={a}, b={b}, delta={delta}', fontsize=8, ha='right', va='top', color='black')
    
    return scat,

for i, (a, b, delta) in enumerate(parameters):
    x = np.sin(a * t + delta)
    y = np.sin(b * t)
    
    # Determine the subplot position based on the loop index
    row = i // 3
    col = i % 3
    
    ax = axs[row, col]
    scat = ax.scatter(x[0], y[0], c=cm.jet(0), s=5)  # Reduced marker size
    
    ani = animation.FuncAnimation(fig, update, len(x), fargs=[x, y, scat, ax, a, b, delta], repeat=True, blit=True)
    
    anis.append(ani)

# Save the animation as a GIF (comment out the line below if you don't want to save the animation)
# ani.save('lissajous.gif', writer=PillowWriter(fps=50))

def on_key(event):
    if event.key == 'q':
        plt.close(event.canvas.figure)

cid = plt.gcf().canvas.mpl_connect('key_press_event', on_key)

plt.show()
