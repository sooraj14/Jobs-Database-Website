from flask import Flask, request, render_template, redirect
import mysql.connector

# connecting to the Flask app 

app = Flask(__name__)
# The SQL database connection to retrive and Push data into the localhost Database Server
my = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='linkedin'
)
mycursor = my.cursor() #    Connecting to the Database

# Signup page Route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
# To check for the Post Method Sent from the Form
    if request.method == 'POST':
        name = request.form['name']     # storing the username in the name variable before sending it to the server
        password_new = request.form['password']     # storing the password in the Password_new variable before sending it to the server
        sql = "insert into users(Username, password)values(%s, %s)"     # Using the Queries to insert the New user into the Database
        val = (name, password_new)          
        mycursor.execute(sql, val)              #Adding the data into the database
        my.commit()
        return redirect('/  ')              #Redirecting the page to the login page
    return render_template('signup.html')           # rendering into the signup page


# Home Page Route
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        user = request.form['username']             # user login From the User is stored
        # print(name)
        pas = request.form['password']              # Password to be stored 
        # print(pas)
        userQuery = f"select * from users where Username like '{user}'"     # Checking the Database for the given USer  

        mycursor.execute(userQuery)             
        allUser = mycursor.fetchall()
        # print(allUser[0][1])
        try:            
            stored_password = allUser[0][1]             # Store the Database password in the variable
        except:
            stored_password = ""
        if pas == stored_password:          # Check whether the password is Matches the Database User PAssword and Username
            return redirect("/state")           # Redirecting the page to the State page If login credentials are True
        else:
            return "Wrong password or Username!!"

    return render_template('login.html')        # reddnder the  login Pafge in / url 


# State Page Route
@app.route('/state', methods=['GET','POST'])
def Jobs():
    mycursor = my.cursor()
    
 
    stateQuery  = "select * from states"        # retriving the data from the database using the SQL Queries

    mycursor.execute(stateQuery)
    allState = mycursor.fetchall()
    if request.method == 'POST':
        name = request.form['search']
        # print(name)
        companyQuery = f"select * from company where Category like '%{name}%' "     #  Queries to check and retrive the data for the search bar

        mycursor.execute(companyQuery)
        companyData = mycursor.fetchall()
        return render_template('table.html', alldata = companyData)     # render the table HTML with the Recently Retrived Data From the database
    return render_template('state.html', alldata=allState)      


# Category page Route
@app.route('/category', methods=['GET', 'POST'])
def category():
    if request.method == 'POST':
        name = request.form['search']
        # print(name)
        companyQuery = f"select * from company where Name like '%{name}%' "     #  Queries to check and retrive the data for the search bar

        mycursor.execute(companyQuery)
        companyData = mycursor.fetchall()
        return render_template('table.html', alldata = companyData)     # render the table HTML with the Data retrived from the database recently throgh the queries
    
    
    stateQuery  = "select * from job_types_1 "              #Retriving the data of job catergory from the database

    mycursor.execute(stateQuery)
    allState = mycursor.fetchall()
    
    return render_template('category.html', alldata=allState)       # render Category Template with the data retrived from the database


# Aerospace page route
@app.route('/aerospace', methods=['GET', 'POST'])
def aerospace():
    if request.method == 'POST':
        name = request.form['search']
        # print(name)
        companyQuery = f"select * from company where Name like '%{name}%' "     #  Queries to check and retrive the data for the search bar

        mycursor.execute(companyQuery)
        companyData = mycursor.fetchall()
        return render_template('table.html', alldata = companyData)     # render the table HTML with the data from the database stored recently
    
    companyQuery = "select * from company where Category= 'Aerospace & Aviation' "      # Retriving the data from the database using the queries

    mycursor.execute(companyQuery)
    companyData = mycursor.fetchall()
    
    return render_template('table.html', alldata=companyData)       # render the Table HTML file with the recently retrived data from the database


# pilot page route
@app.route('/pilot', methods=['GET', 'POST'])
def pilot():
    if request.method == 'POST':
        name = request.form['search']
        # print(name)
        companyQuery = f"select * from company where Name like '%{name}%' " #  Queries to check and retrive the data for the search bar

        mycursor.execute(companyQuery)
        companyData = mycursor.fetchall()
        return render_template('table.html', alldata = companyData)
    
    companyQuery = "select * from company where Category= 'Airline Pilot' "     # Retriving the data from the database using queries and storing it

    mycursor.execute(companyQuery)
    companyData = mycursor.fetchall()
    
    return render_template('table.html', alldata=companyData)       # rendering the table HTML file with all the data stored previously



# materials page Route
@app.route('/materials', methods=['GET', 'POST'])
def materials():
    if request.method == 'POST':
        name = request.form['search']
        # print(name)
        companyQuery = f"select * from company where Name like '{name}%' "  #  Queries to check and retrive the data for the search bar

        mycursor.execute(companyQuery)
        companyData = mycursor.fetchall()
        return render_template('table.html', alldata = companyData) 
    
    
    companyQuery = "select * from company where Category= 'Aerospace Materials Specialist' "    # Retriving the data from the database using queries and storing it

    mycursor.execute(companyQuery)
    companyData = mycursor.fetchall()
    
    return render_template('table.html', alldata=companyData )      # rendering the table HTML file with the data retrived and stored recently


if __name__ == "__main__":
    app.run(debug=True, port=5000)      
    # for Develoipment Purpose We can Set the Debug to 'False' 
    