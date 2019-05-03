import os

# using Spotlight
type(Key.SPACE, Key.CMD)
type("test---111")
type(Key.ENTER)
# Change into Icon at Folder window  by ShortCut Key
type("1", Key.CMD)



# f = open('test.csv', 'r')
# title = "check"
# msg = f.read()tereb
# popup(msg, title)
# wait(15)

myApp = App("/Applications/iMovie.app")
myApp.open()
wait(5)
"""
# using Spotlight to Open iMovie
type(Key.SPACE, Key.CMD)
type("iMovie")
type(Key.ENTER)
wait(5)
"""


# moving Window of iMovie
# Tips : inserted image name seems to be availabe english only.
# Moving to the right 500 pixel
click(Pattern("clickhere2.png").targetOffset(86,-2))
region1=Env.getMouseLocation()
region2=Location(region1.getX()+700,region1.getY())
# popAsk("test", str(region1))
# popAsk("test", str(region2))
dragDrop(region1, region2)

# Drag and Drop
#click("clickhere3.png")
#region3=Env.getMouseLocation()
#region4=Location(region3.getX(),region3.getY()+100)
#region5=Location(region4.getX()+200,region4.getY())

click("1555809401889.png")
region6=Env.getMouseLocation()
#dragDrop(region4, region6)
#drag("1555748712069.png")
#wait(2)
#position=Location(region6.getX(),region6.getY()-100)
#dropAt(region6)
#mouseMove(position)
#dropAt(position)
#mouseUp()
#wait(3)

movelist1 = [
        { "fileicon":"1555765603064.png" , "moveto": "1555907723681.png"},
]

movelist2 = [       
        { "fileicon": "1555765614663.png", "moveto": Pattern("1555765706825.png").targetOffset(8,107)},
]

click(Pattern("1555913324335.png").targetOffset(-59,-3))
region_base=Env.getMouseLocation()

while True:
 for item1 in movelist1:
   m1 = find(item1['fileicon'])
   drag(m1)
   mouseMove(region_base.offset(0,0))
   wait(1)   
   mouseMove(region_base.offset(5,15))
   wait(1)
   mouseMove(region_base.offset(20,60))
#   mouseMove(region_base.offset(-5,-25))  
   wait(1)
   dropAt(region_base.offset(20,60))
   wait(1)
   mouseUp()
   wait(1)

 for item2 in movelist2:
   m2 = find(item2['fileicon'])
   drag(m2)
   mouseMove(region_base.offset(0,0))
   wait(1)   
   mouseMove(region_base.offset(5,15))
   wait(1)
   mouseMove(region_base.offset(20,60))
#   mouseMove(region_base.offset(-5,-25))  
   wait(1)
   dropAt(region_base.offset(20,60))
   wait(1)
   mouseUp()
   wait(1)
   

#t=find("/Users/TETSUO/Desktop/test-111/w.jpg")
click("w.jpg")
region8=Env.getMouseLocation()
dragDrop(region8, "1555749829362.png")


# mouseDown(Button.LEFT)
# mouseMove(offset(0,100))
#find("/Users/TETSUO/Desktop/test-111/test-desu.wav")
#click("/Users/TETSUO/Desktop/test-111/test-desu.wav")


myApp2 = App("Calculator.app")
myApp2.open()
myApp2.focus()
win = myApp2.focusedWindow()
filename = capture(win)
os.rename(filename, "calc.png")

filename = capture(getBounds())
os.rename(filename, "mycapture.png")

myApp.open()
wait(10)

click("1553220980323.png")
wait(5)
click("clickhere.png")
wait(5)
click(Pattern("1553223988027.png").targetOffset(-13,364))
type("a", Key.CMD)
type("e")

click(Pattern("1553410100390.png").targetOffset(-1,59))
type("a", Key.CMD)
click("1553410420708.png")
click(Pattern("clickhere2-1.png").targetOffset(45,4))


# type("a", Key.CMD)
wait(10)

# type("Q",Key.CMD)
# myApp.close()
