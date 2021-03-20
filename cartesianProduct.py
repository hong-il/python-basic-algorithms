import itertools

iterable1 = 'ABCD'
iterable2 = 'xy'
iterable3 = '1234'

# Ax1
# Ax2
# Ax3
# Ax4
# Ay1
# Ay2
# Ay3
# Ay4
# Bx1
# Bx2
# Bx3
# Bx4
# By1
# By2
# By3
# By4
# Cx1
# Cx2
# Cx3
# Cx4
# Cy1
# Cy2
# Cy3
# Cy4
# Dx1
# Dx2
# Dx3
# Dx4
# Dy1
# Dy2
# Dy3
# Dy4
for _ in itertools.product(iterable1, iterable2, iterable3):
    print(''.join(_))
