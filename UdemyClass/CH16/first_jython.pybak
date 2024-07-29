def change_all_to_red(pic):
  for p in getPixels(pic):
    setColor(p, red)
    
    
def clearRed(pic):
  for p in getPixels(pic):
    setRed(p, 0)
  
def greenish(pic):
  for p in getPixels(pic):
    setGreen(p, 255)
    
def half_blue(pic):
  for p in getPixels(pic):
    setBlue(p, getBlue(p) * 0.5)
   
def change_all_to_new_color(pic):
  new_color = makeColor(100, 50, 125)
  for p in getPixels(pic):
    setColor(p, new_color)
    
def black_top_right_corner(pic):
  w = getWidth(pic)   
  h = getHeight(pic)
  for p in getPixels(pic):
    x = getX(p)
    y = getY(p)
    if x > (w/2) and y < (h/2):
      setColor(p, black)
  writePictureTo(pic, '/Users/ice/Downloads/Pictures for JES/panda.png')
 # faster method than up one
 # for x in range(w/2, w):
 #    for y in range(h/2):
 #      p = getPixel(pic, x, y)
 #      setColor(p, black)
def brighter(picture):
   for px in getPixels(picture):
     r = getRed(px)
     g = getGreen(px)
     b = getBlue(px)
     new_color = makeColor(r*1.3, g*1.3, b*1.3)
     setColor(px, new_color)
     
def grayscale(picture):
  for p in getPixels(picture):
    x = (getRed(p) + getGreen(p) + getBlue(p))/3
    setColor(p, makeColor(x, x, x))
    
def copyHalf(picture):
  pixels = getPixels(picture)
  for i in range(0, len(pixels)/2):
    p1 = pixels[i]
    c1 = getColor(p1)
    p2 = pixels[len(pixels) -1 -i]
    setColor(p2, c1)
  writePictureTo(picture, '/Users/ice/Downloads/Pictures for JES/halfpanda.png')
def copyHalf2(picture):
  pixels = getPixels(picture)
  for i in range(0, len(pixels)/ 2):
    p1 = pixels[i]
    c1 = getColor(p1)
    p2 = pixels[i + len(pixels)/ 2]
    setColor(p2, c1)
  writePictureTo(picture, '/Users/ice/Downloads/Pictures for JES/halfpanda2.png')

def blue_panda(picture):
  for x in range(140, 450):
    for y in range(35, 330):
      p = getPixel(picture, x, y)
      c = getColor(p)
      if distance(c, white) < 200:
        setColor(p, blue)

def edge_detection(source):
  for px in getPixels(source):
    x = getX(px)
    y = getY(px)
    if y < getHeight(source) - 1 and x < getWidth(source) - 1:
      sum = getRed(px) + getGreen(px) + getBlue(px)
      botrt = getPixel(source, x + 1, y + 1)
      sum2 = getRed(botrt) + getGreen(botrt) + getBlue(botrt)
      diff = abs(sum2 - sum)
      newColor = makeColor(diff, diff, diff)
      setColor(px, newColor)
  writePictureTo(source, '/Users/ice/Downloads/Pictures for JES/result.png')

def chromakey(source, bg):
  for px in getPixels(source):
    x = getX(px)
    y = getY(px)
    if getRed(px) + getBlue(px) < getGreen(px):
      bgpx = getPixel(bg, x, y)
      bgcol = getColor(bgpx)
      setColor(px, bgcol)

def mirrorVertical(source):
  width = getWidth(source)
  mirrorPoint = width / 2
  for y in range(0, getHeight(source)):
    for x in range(0, mirrorPoint):
      leftPixel = getPixel(source, x, y)
      rightPixel = getPixel(source, width - 1 - x, y)
      setColor(rightPixel, getColor(leftPixel))
      
def mirrorHorizontal(source):
  for x in range(getWidth(source)):
    for y in range(getWidth(source) / 2):
      p1 = getPixel(source, x, y)
      p2 = getPixel(source, x, getHeight(source) - 1 -y)
      setColor(p2, getColor(p1))
     
def mirrorDiagonal(pic):
  for y in range(getHeight(pic)):
    for x in range(y):
      p1 = getPixel(pic, x, y)
      p2 = getPixel(pic, y, x)
      setColor(p2, getColor(p1))
     
      
def mirrorDiagonal2(pic):
  for y in range(getHeight(pic)):
    for x in range(getWidth(pic) - y):
      p1 = getPixel(pic, x, y)
      p2 = getPixel(pic, getHeight(pic) - 1 - y, getWidth(pic) - 1 - x)
      setColor(p2, getColor(p1))
      
def copyInGeneral(pic, targetX, targetY):
  canvas = makeEmptyPicture(1000, 1000)
  for x in range(getWidth(pic)):
    for y in range(getHeight(pic)):
      p1 = getPixel(pic, x, y)
      p2 = getPixel(canvas, targetX + x, targetY + y)
      setColor(p2, getColor(p1))
  writePictureTo(canvas, '/Users/ice/Downloads/Pictures for JES/copy101.png')
  