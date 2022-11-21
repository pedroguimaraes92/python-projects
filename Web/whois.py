from tkinter import *
import whois


#Function to get domain info
def Domain_info():
    domain = whois.whois(str(e1.get()))
    server.set(domain.whois_server)
    exp_date.set(domain.expiration_date)
    reg_name.set(domain.name)
    org.set(domain.org)
    state.set(domain.state)
    city.set(domain.city)
    country.set(domain.country)


#Tkinter

main = Tk()
main.title("See Who Is")
main.configure(bg = '#C0C0C0')

#Creating Variables

server = StringVar()
exp_date = StringVar()
reg_name = StringVar()
org = StringVar()
state = StringVar()
city = StringVar()
country = StringVar()

# Creating Text Labels

Label(main, text="Website URL : ", bg = "#C0C0C0").grid(row=0, sticky=W)
Label(main, text="Server Name :", bg = "#C0C0C0").grid(row=3, sticky=W)
Label(main, text="Expiration date :", bg = "#C0C0C0").grid(row=4, sticky=W)
Label(main, text="Register name :", bg = "#C0C0C0").grid(row=5, sticky=W)
Label(main, text="Origination :", bg = "#C0C0C0").grid(row=6, sticky=W)
Label(main, text="State :", bg = "#C0C0C0").grid(row=7, sticky=W)
Label(main, text="City :", bg = "#C0C0C0").grid(row=8, sticky=W)
Label(main, text="Country :", bg = "#C0C0C0").grid(row=9, sticky=W)


#Creating Labels
Label(main, text="", textvariable=server, bg="#C0C0C0").grid(row=3, column=1, sticky=W)
Label(main, text="", textvariable=exp_date, bg="#C0C0C0").grid(row=4, column=1, sticky=W)
Label(main, text="", textvariable=reg_name, bg="#C0C0C0").grid(row=5, column=1, sticky=W)
Label(main, text="", textvariable=org, bg="#C0C0C0").grid(row=6, column=1, sticky=W)
Label(main, text="", textvariable=state, bg="#C0C0C0").grid(row=7, column=1, sticky=W)
Label(main, text="", textvariable=city, bg="#C0C0C0").grid(row=8, column=1, sticky=W)
Label(main, text="", textvariable=country, bg="#C0C0C0").grid(row=9, column=1, sticky=W)


e1 = Entry(main)
e1.grid(row=0, column=1)

#Creating Button

b = Button(main, text = "Show Me", command = Domain_info, bg="Blue", fg = "White")
b.grid(row=0, column=2, columnspan=2, rowspan=2, padx=5, pady=5,)

main.mainloop()
