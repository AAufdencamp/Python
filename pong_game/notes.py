#create screen
#create and move a paddle
    # Right side
    # width = 20
    # height = 100
    # x_pos = 350
    # y_pos = 0
    # movement of paddle engage by keyboard press up and down by 20 pixels per keyboard press.

#create another paddle
    #we are going to create a Paddle class to avoid repeat code
    #Paddle class inherits from Turtle
    #Paddle objects need to be initialized with a tuple for X and Y coordinates
    #l_paddle need to move up and down with "w" and "s" keys


#create ball and make it move constantly
    #create ball as separate ball class
    #width = 20
    # #height = 20
    # x_pos = 0
    # y_pos =0
    #when screen refreshed ball moves up and right
    # x and y pos will change w every refresh of screen



#detect collision with wall and bounce
    #And the first thing we're going to tackle is how to detect collision when the
    #ball hits the wall at the top and the bottom and getting the ball to bounce.
    #  because when the ball hits the right or of the left edges of the program,
    # it should actually be caught by one of the paddles. And if it isn't,
    # then that means that player has missed the ball and it's a point to the other side.



#detect collision with paddle
    #normally we used th distance() method to check what is the distance between ball and paddle
    # ball.distance(paddle) This measure distance from center of each object
    # ball is 20 x 20
    # paddle is 100 w x 20 l
    # because the distance btwn centers changes as the ball touches various points along the paddle
    # we will use a x-value as a constant AND check if the ball is within 50 pixels of the paddle





#detect when paddle misses
    #when a paddle misses the ball a point goes to the opponent and should trigger re-start of the game
    #ball returns home and gets tossed in opposite direction
    ##detecting missing the ball:But if it goes further than that (+ or - 320 xcor and within 50 pixels), if it goes beyond that on the screen
    ##then that means it's a miss and we should reset the ball.



# keeps score

