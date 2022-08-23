from tkinter import *
import psycopg2
# pure-lowlands-38878

# Aaron Pratt 8/22/22 
# cloud 



root = Tk()
root.title("Cloud App")
root.geometry("500x550")

def connect():
	# Configure and connect to postgres
	connection = psycopg2.connect(
		host = "ec2-44-205-41-76.compute-1.amazonaws.com",
		database = "deviatbnmcdcs2",
		user = "gpiwgctlovdjpo",
		password = "254904fdaa6392b66e7e12c201415087ab8aa8f1a100aa9957a1e11aed09da21",
		port = "5432",

		)
	return connection

def query():
	conn = connect()

	# Create a cursor
	c = conn.cursor()

	# Create a table
	c.execute(''' CREATE TABLE IF NOT EXISTS customers
		(first_name TEXT,
		last_name TEXT);
		''')

	conn.commit()
	conn.close()

def submit():
	conn = connect()

	# Create a cursor
	c = conn.cursor()

	# Insert data into table
	thing1 = f_name.get()
	thing2 = l_name.get() 
	c.execute(''' INSERT INTO customers (first_name, last_name)
		VALUES (%s, %s)''', (thing1, thing2)
		)

	conn.commit()
	conn.close()

	update()

def update():
	conn = connect()

	# Create a cursor
	c = conn.cursor()

	# Grab from online database
	c.execute("SELECT * FROM customers")
	records = c.fetchall()

	output = ''

	for record in records:
		output_label.config(text=f'{output}\n{record[0]} {record[1]}')
		output = output_label['text']

	conn.close()


my_frame = LabelFrame(root, text="Postgres Example")
my_frame.pack(pady=20)

f_label = Label(my_frame, text="First Name:")
f_label.grid(row=0, column=0, pady=10, padx=10)

f_name = Entry(my_frame, font=("Helvetica, 18"))
f_name.grid(row=0, column=1, pady=10, padx=10)

l_label = Label(my_frame, text="Last Name:")
l_label.grid(row=1, column=0, pady=10, padx=10)

l_name = Entry(my_frame, font=("Helvetica, 18"))
l_name.grid(row=1, column=1, pady=10, padx=10)

submit_button = Button(my_frame, text="Submit", command=submit)
submit_button.grid(row=2, column=0, pady=10, padx=10)

update_button = Button(my_frame, text="Update", command=update)
update_button.grid(row=2, column=1, pady=10, padx=10)

output_label = Label(root, text="")
output_label.pack(pady=50)

query()

root.mainloop()