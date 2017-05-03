#!/usr/bin/env python
import sys, os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from sklearn.cluster import KMeans
from PIL import Image
 
rgb2hex = lambda rgb: '#%s' % ''.join(('%02x' % p for p in rgb))

def getcentroids(filename, n=8):
    img = Image.open(filename)
    img.thumbnail((100, 100))
    # run kmeans
    kmeans = KMeans(init='k-means++', n_clusters=n)
    kmeans.fit(list(img.getdata()))
    # get centroids
    rgbs = [map(int, c) for c in kmeans.cluster_centers_]
    return rgbs

def set_colors_gnome(centroids):
    palette = 'gsettings set org.pantheon.terminal.settings palette \"'
    colors = ':'.join(rgb2hex(centroid) for centroid in centroids)
    os.system(palette + colors + colors + '\"')
        
def bar(mode):
    write = sys.stdout.write
    for i in range(0, 10):
        write('\033[%d;3%dmBAR ' % (mode, i))
    write('\n')

centroids = getcentroids(sys.argv[1], n=8)
set_colors_gnome(centroids)
bar(0); bar(1)
