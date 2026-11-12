Web VPython 3.2
box(texture= "https://i.postimg.cc/wvsXFQGt/d0847284ad3ccebeee50f66296cfdc9b-1.jpg", size = vec(40,40,1))

body = box(size = vec(20,4,4), color = vec(0.5,0.5,1.0), pos=vec(0,0,6))
head = box(size = vec(8,4,4), pos = vec(6,0,2))

brush = compound([body, head])

while True :
    rate(100)
    k = keysdown()
    if 'right' in k: 
        brush.pos.x = brush.pos.x + 1
    if 'left' in k: 
        brush.pos.x = brush.pos.x - 1
    if 'up' in k: 
        brush.pos.y = brush.pos.x + 1
    if 'down' in k: 
        brush.pos.y = brush.pos.x - 1



Web VPython 3.2
box(texture= "https://i.postimg.cc/wvsXFQGt/d0847284ad3ccebeee50f66296cfdc9b-1.jpg", size = vec(40,40,1))

body = box(size = vec(20,4,4), color = vec(0.5,0.5,1.0), pos=vec(0,0,6))
head = box(size = vec(8,4,4), pos = vec(6,0,2))
teeth = cylinder(size = vec(8,4,4), pos = vec(4,-7,2), axis = vec(0,1,0), color = vec(0,0,0))
teeth = cylinder(size = vec(4.3,3.2,3), pos = vec(-3.5,-2,0), axis = vec(0,1,0), color = vec(0,0,0))

brush = compound([body, head])

while True :
    rate(10)
    k = keysdown()
    if 'right' in k: 
        brush.pos.x = brush.pos.x + 1
    if 'left' in k: 
        brush.pos.x = brush.pos.x - 1
    if 'up' in k: 
        brush.pos.y = brush.pos.x + 1
    if 'down' in k: 
        brush.pos.y = brush.pos.x - 1
        teeth.color = teeth.color + vec(0.1,0.1,0.1)
    
