def setup ():  
    size(300, 300)
    smooth()
    strokeWeight(30)
    background(0)


def draw ():
    stroke(frameCount)
    line(frameCount ,frameCount, 100+frameCount , frameCount+100)
    line(100+frameCount ,frameCount, frameCount , frameCount+100)


        
