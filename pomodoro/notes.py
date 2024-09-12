#canvas widget allows layers of images or text

#command line versus GUI
#command line executes only upon instruction/actively hitting enter
#GUI: keeps "watch" on the screen for user engagement. It refreshes and keeps listening for events. This type of
#GUI program is event-driven through the .maineloop() when we set up our GUI window. Coding in additional loops will
#fail to launch your program.

#GUI timing mechanism. Use builtin methods to every widgetz:in this less we use the window widget,
#we can get hold of a method called .after().
# .after() takes an amount of time it should wait then it runs the function tied to it by command = func()
#We use milliseconds; 1000 milliseconds == 1 second.
#to get .after() to repeat itself we it inside another function. See the count_down() function in main.py

#So how can we instead of printing the count actually change this text on our canvas?
#we need to assign our canvas.create_text(100, 130, text = "00:00", fill = "white", font = (FONT_NAME, 35, 'bold'))
#to a variable

#And the way that we'd change a piece of text or anything for that matter in a canvas is slightly different from how
# we would do for a label. If it was just the title label that we wanted to change, we would say title_label.config,
# and then let's change the text to something new. But to change a canvas element, you actually have to tap into
# the particular canvas you want to change and Then you call a method called itemconfig. And then in this method,
# you pass in the particular item that you actually want to configure, so in our case it's the timer_text,

#Dynamic typing: Python allows you to change a variable's data type by re-assignment
#"Dynamic typing means that runtime objects (values) have a type, as opposed to static typing where variables have a type."
# https://stackoverflow.com/questions/11328920/is-python-strongly-typed
#TAKEAWAY: when evaluating datatype in Python, the datatype is in reference to the value to which a given var. is
#assigned. ie. variables themselves in Python do not have type but only name an object.