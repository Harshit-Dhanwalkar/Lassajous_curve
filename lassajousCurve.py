import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.cm as cm
from matplotlib.animation import PillowWriter # For saving the animation as a GIF

# Define the parameters for the Lissajous curves
parameters = [
    (1, 2, np.pi / 2),
    (3, 2, np.pi / 2),
    (3, 4, np.pi / 2),
    (5, 4, np.pi / 2)
]

t = np.linspace(0, 2 * np.pi, 500)

fig, axs = plt.subplots(len(parameters), 1, figsize=(8, 8))

anis = []

def update(num, x, y, scat, ax, a, b, delta):
    ax.clear()
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    
    color = cm.jet(float(num) / len(x) - 0.001)
    scat = ax.scatter(x[:num], y[:num], color=color)
    
    ax.text(1.8, 1.5, f'a={a}, b={b}, delta={delta}', fontsize=8, ha='right', va='top', color='black')
    
    return scat,

for i, (a, b, delta) in enumerate(parameters):
    x = np.sin(a * t + delta)
    y = np.sin(b * t)
    
    ax = axs[i]
    scat = ax.scatter(x[0], y[0], c=cm.jet(0))
    
    ani = animation.FuncAnimation(fig, update, len(x), fargs=[x, y, scat, ax, a, b, delta], repeat=True, blit=True)
    anis.append(ani)

def on_key(event):
    if event.key == 'q':
        plt.close(event.canvas.figure)

cid = plt.gcf().canvas.mpl_connect('key_press_event', on_key)

# Save the animation as a GIF comment out the line below if you don't want to save the animation
#ani.save('lissajous.gif', writer=PillowWriter(fps=30))

plt.show()
