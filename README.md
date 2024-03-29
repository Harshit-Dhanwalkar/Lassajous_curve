# Lissajous curves

Lissajous curves, also known as Lissajous figures or Bowditch curves, are the graphs of a system of parametric equations: $$x = A sin(at + δ)$$ $$y = B sin(bt)$$

Where:

A and B are the amplitudes of the oscillations in the x and y directions, respectively.
a and b are the frequencies of the oscillations in the x and y directions, respectively.
δ is the phase shift between the x and y oscillations.
These curves are used in physics, astronomy, and other fields to describe oscillatory phenomena. They are named after Jules Antoine Lissajous, a French physicist who studied them in the 19th century.

The shape of a Lissajous curve is determined by the ratio of the frequencies a and b, and the phase shift δ. When a and b are integers, the curve will be closed, meaning it will repeat itself after a certain period. The number of intersections in the curve is equal to |a - b|, if a and b are coprime.

## Code expaination
This Python script generates Lissajous curves using the `numpy` and `matplotlib` libraries. Here's a breakdown of what the code does:

1. The necessary libraries are imported. These include `numpy` for numerical operations, `matplotlib.pyplot` for plotting, and `matplotlib.animation` for creating animations.

2. A list of tuples named `parameters` is defined. Each tuple represents a set of parameters `(a, b, delta)` for a Lissajous curve. `a` and `b` are the frequencies of the curve in the x and y directions, respectively, and `delta` is the phase shift.

3. A `numpy` array `t` is created, ranging from 0 to 2π, with 500 points. This array will be used as the input to the Lissajous curve function.

4. A figure with multiple subplots is created using `plt.subplots`. The number of subplots is equal to the number of parameter sets defined in `parameters`.

5. An empty list `anis` is created, presumably to store the animations for each subplot.

6. The `update` function is defined. This function is likely used in an animation function (not shown in the provided code). It takes several parameters, including `num` (the current frame number), `x` and `y` (the data to be plotted), `scat` (the scatter plot object), `ax` (the axes object), and `a`, `b`, `delta` (the parameters for the Lissajous curve). The function clears the axes, sets the x and y limits, and then updates the scatter plot with the current frame's data. The color of the scatter plot is determined by the current frame number.

This code is part of a larger script that generates and animates Lissajous curves. The remaining part of the script, which is not shown here, would likely involve a loop over the `parameters` list to generate the curves, and a call to an animation function such as `animation.FuncAnimation` to create the animations.

For more information about Lissajous curves, see the [Wiki:Lissajous_curve](https://en.wikipedia.org/wiki/Lissajous_curve).
