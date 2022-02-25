# The Polar Coordinate system is an alternate coordinate system where
# the two variables are 'r' and 'O'(Omega), instead of x and y.
# A Polar Coordinate system is a two-dimensional coordinate system in
# which each point on a plane is determined by a distance from a reference
# point and an angle from a reference direction.

# Complex number: z = x + yi, where x is a real part, and yi is imaginary part.

# To solve the problem, we need to import cmath python module, and polar function
# to calculate a complex number. And use asterisk(*) to use sep. statement.

import cmath
print(*cmath.polar(complex(input())), sep='\n')
