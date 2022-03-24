from guizero import App, Combo, ListBox, Text, ButtonGroup, PushButton, TitleBox

app = App(layout = 'grid', width = 500)
price = 0

def film_choice(selected_value):
  ticket_film = selected_value

def get_ticket_price():
  if type.value == 'Regular':
    price = 6
  else:
    price = 4
  return price

def add_ticket():
  tickets = []
  price = get_ticket_price()
  list_item_film.append(films.value)
  list_item_category.append(type.value)
  list_item_price.append(price)

def total_ticket():
  proceed = app.yesno("Total Price", "Total price: £" + str(sum(list_item_price.items) ))
  if proceed == True:
    app.info("Pay Now", "Thank you for your custom - Enjoy the Film")
    list_item_film.clear()
    list_item_category.clear()
    list_item_price.clear()
  else:
   cancel = app.yesno("Back to tickets", "Cancel Order?")
   if cancel == True:
    app.info("Cancel order","Cancel order?")
    list_item_film.clear()
    list_item_category.clear()
    list_item_price.clear()

title = Text(app, "Welcome to Cinema World", grid = [0,0], size = 24)
gap = Text(app, "", grid = [0,1])
buttons_area = TitleBox(app, "Choose Tickets", grid = [0,2],
                       layout = 'grid')
film_text = Text(buttons_area, "Films:", grid = [0,1], align = 'left')
films = Combo(buttons_area,
              grid = [1,0],
              options=["Star Wars", "Star Trek", "Shrek", "James Bond"],
              command = film_choice)

ticket_type = Text(buttons_area, "Ticket Type:", grid = [0,1], align = 'left')

type = ButtonGroup(buttons_area,
                   grid = [1, 1],
                   command = get_ticket_price,
                   options=["Child", "Regular", "Concession"],
                   selected="Regular"
                  )

add_button = PushButton(buttons_area,
                        grid = [1,2],
                        command = add_ticket,
                        text = " Add ")

total_button = PushButton(buttons_area,
                          grid = [2,2],
                          command = total_ticket,
                          text = "Total")
gap = Text(app, "", grid = [0,3])

ticket_list = TitleBox(app, "Film \t\t Ticket \t\t\t Price (£)",
grid = [0,4],
layout = 'grid')

list_item_film = ListBox(ticket_list, grid = [0,0])
list_item_category = ListBox(ticket_list, grid = [1,0])
list_item_price = ListBox(ticket_list, grid = [2,0])

app.display()
