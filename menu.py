import numpy as np
import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms


def affine(ax, Z, transform):
    im = ax.imshow(Z, interpolation='none',
                   origin='lower',
                   extent=[-2, 4, -3, 2], clip_on=True)

    trans_data = transform + ax.transData
    im.set_transform(trans_data)

    # display intended extent of the image
    x1, x2, y1, y2 = im.get_extent()
    ax.set_xlim(-5, 5)
    ax.set_ylim(-4, 4)


# prepare image and figure
fig, ((ax1,ax2),
      (ax3,ax4)) = plt.subplots(2,2)
Z = plt.imread('grid.jpg')
affine(ax1,Z,mtransforms.Affine2D())
affine(ax3,Z,mtransforms.Affine2D())

# everything and a translation
affine(ax2, Z, mtransforms.Affine2D().
        rotate_deg(-30))
affine(ax4, Z, mtransforms.Affine2D().skew_deg(30,30).scale(1.5,.5))
plt.show()