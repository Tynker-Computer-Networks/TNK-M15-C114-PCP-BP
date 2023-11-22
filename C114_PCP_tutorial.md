Tambola Stage-2
==================


In this activity, you will learn to display the ticket of the tambola game.


<img src= "https://s3.amazonaws.com/media-p.slid.es/uploads/1525749/images/10917705/114_PCP_.gif" width = "480" height = "280">


Follow the given steps to complete this activity:



1. Create the Ticket Grid


* Open the file `client.py`.
* Set the position of the box.
~~~python
def create_ticket():
    global gameWindow
    global ticket_grid
    xPos = 105
    yPos = 130
~~~
* Create the boxes on the ticket of 3 rows and 9 columns.
~~~python
    for row in range(0, 3):
        row_list = []
        for col in range(0, 9):
            box_button = tk.Button(gameWindow, font = ("Chalkboard SE",30), width=3, height=2,borderwidth=5, bg="#fff176")
            box_button.place(x=xPos, y=yPos)
            row_list.append(box_button)
            xPos += 64
        ticket_grid.append(row_list)
        xPos = 105
        yPos +=92
~~~


2. Display the ticket on the game window.


* Call the functions to display the ticket.
~~~python
def gameWindow():
	. . .
create_ticket()
place_numbers()


def save_name():
	. . .
	gameWindow()
~~~
* Save and run the code to check the output.