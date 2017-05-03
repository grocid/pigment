# Pigment

This is simple tool which uses the K-means++ algorithm to pick suitable terminal colors from a given image. The algorithm is an approximation for solving clustering/paritioning problems, which in this particular case means finding `N = 8` dominant colors in the image.

To set colors in Pantheon terminal (Elementary OS), simply invoke the following
```
./pigment.py [image filename]
```

Currently, the code only works in Pantheon terminal, but the colors can be extracted and manually inserted into your favorite terminal's settings. Running the script for the image below...

![A wallpaper image][Vg3ve2E.jpg]

we get the following set of colors

```
#8b3860:#f7d188:#311331:#9ed8aa:#e0593f:#ab3031:#621d39:#e19f70#8b3860:#f7d188:#311331:#9ed8aa:#e0593f:#ab3031:#621d39:#e19f70
```
