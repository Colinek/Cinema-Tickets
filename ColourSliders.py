from guizero import App, Text, PushButton, TextBox, Slider

# Functions -----------------------------------    
def red_changed(slider_value):
  app.bg = (red.value, green.value, blue.value)
def blue_changed(slider_value):
  app.bg = (red.value, green.value, blue.value)
def green_changed(slider_value):
  app.bg = (red.value, green.value, blue.value)

# Main Window ----------------------------------  
app = App(title = "Demo", layout = 'grid')
app.bg = 'darkslategrey'

# Red ---------------------------------- 
red_text = Text(app, text = "R",
               grid=[0,0],
               bg = 'red')

red = Slider(app, command=red_changed,
            grid=[1,0],
            start = 0, 
            end = 127,
            width = 250,
            height = 40)
# Green ---------------------------------- 
green_text = Text(app, text = "G",
               grid=[0,1],
                 bg = 'green',
                 )

green = Slider(app, command=green_changed,
            grid=[1,1],
            start = 0, 
            end = 127,
            width = 250,
            height = 40)

# Blue ---------------------------------- 
blue_text = Text(app, text = "B",
               grid=[0,2],
               bg = 'blue')

blue = Slider(app, command=blue_changed,
            grid=[1,2],
            start = 0, 
            end = 127,
            width = 250,
            height = 40)

# Display the App ------------------------ 
app.display()