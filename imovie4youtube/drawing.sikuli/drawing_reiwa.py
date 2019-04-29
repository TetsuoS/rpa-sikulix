myApp = App("/Users/TETSUO/Desktop/FireAlpaca.app")
myApp.open()
click(Pattern("firealpaca.png").targetOffset(-133,0))
#wait(1)
type("n", Key.CMD)
type(Key.ENTER)
wait(1)
#click(Pattern("ok.png").targetOffset(-12,4))
#wait(15)

click("64bit.png")
region_base=Env.getMouseLocation()
#drag(m)
#mouseMove(region_base.offset(0,0))
wait(3)
drag(region_base.offset(0,300))  
dropAt(region_base.offset(0,320))
#mouseUp()
drag(region_base.offset(0,350))
dropAt(region_base.offset(0,500))

drag(region_base.offset(0,300))
dropAt(region_base.offset(500, 300))

#circle(region_base.offset(500, 300))
#wait(1)
#mouseUp()
#wait(1)

#Settings.MoveMouseDelay=0
import math as m
pi = m.pi
circle = []
for n in range(0, 370, 30):
    y = int(100*m.sin(m.radians(n)))
    x = int(100*m.cos(m.radians(n)))
    circle.append(Location(1000+x, 1000+y))
for p in circle: drag(p)

#drag(region_base.offset(700,700))
#dropAt(region_base.offset(800,800))

mouseUp()
dragDrop(region_base.offset(500,500), region_base.offset(600,600))



# myApp.close()
