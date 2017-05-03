#!/usr/bin/env python
import sys, os
from sklearn.cluster import KMeans
from PIL import Image

nbrcentroids = 10
# Constant increase in colors
beta = 10
# Multplicative factor in background
gamma = 0.4
rgb2hex = lambda rgb: '#%s' % ''.join(('%02x' % min(p + beta, 255) for p in rgb))
darken = lambda rgb : (p * gamma for p in rgb)

def getcentroids(filename, n=8):
    img = Image.open(filename)
    img.thumbnail((100, 100))
    # Run K-means algorithm on image
    kmeans = KMeans(init='k-means++', n_clusters=n)
    kmeans.fit(list(img.getdata()))
    # Get centroids from solution
    rgbs = [map(int, c) for c in kmeans.cluster_centers_]
    return rgbs

def set_colors_gnome(centroids):
    centroids = sorted(centroids, key=lambda rgb: sum(c**2 for c in rgb))
    # Set background and foreground
    os.system('gsettings set org.pantheon.terminal.settings background \"%s\"' % rgb2hex(darken(centroids[0])))
    os.system('gsettings set org.pantheon.terminal.settings foreground \"%s\"' % rgb2hex(centroids[-1]))
    # Set ANSI colors
    palette = 'gsettings set org.pantheon.terminal.settings palette \"'
    colors = ':'.join(sorted(rgb2hex(centroid) for centroid in centroids[1:-1]))
    os.system(palette + colors + ':' + colors + '\"')

def bar(mode):
    write = sys.stdout.write
    for i in range(0, nbrcentroids):
        write('\033[0;3%dmBAR ' % i)
    write('\n')

centroids = getcentroids(sys.argv[1], n=nbrcentroids)
set_colors_gnome(centroids)
bar(0);
