from flask import Flask, render_template, redirect, url_for, request, flash
import sqlite3
import datetime


app = Flask(__name__)


app.config['SECRET_KEY'] = 'secretkey,dontrytostealhehe'

connect = sqlite3.connect('platform.db', check_same_thread=False)

cur = connect.cursor()




#База данных для поставщика
cur.execute("""CREATE TABLE IF NOT EXISTS purveyors(
    userid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    full_name TEXT,
    postal_address TEXT,
    legal_address TEXT,
    phone_number INTEGER,
    e_mail TEXT,
    inn INTEGER,
    login TEXT,
    password TEXT);
""")

connect.commit()

#База данных для торгов
cur.execute(""" CREATE TABLE IF NOT EXISTS items(
    itemid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    userid TEXT,
    creator TEXT
    price INTEGER,
    text TEXT,
    title TEXT,
    date TEXT);
""")

connect.commit()


@app.route('/')
def root():
    menu=['Computers', 'Smartphones', 'Notebooks']
    number = [1, 2, 3]
    organizer = ['Apple', 'Google', 'Microsoft']
    subject_of_auction = ['MacBook - 100 *баных тысяч рублей', 'ChromeBook - не сильно отличается по цене от яблок', 'SurfaceBook - ваще п*зд%ц']
    status = ['идёт приём заявок', 'идёт приём заявок', 'торги завершены']
    app_accept_time = ['29.03.2022 12:00', '24.05.2022 16:00', '01.08.2022 18:00']
    counter = range(0, len(number))
    log_in='Вход'
    return render_template(
        'index.html', 
        categories_menu = menu,
         number = number, 
         organizer = organizer, 
         subject_of_auction = subject_of_auction,
          status = status, app_accept_time = app_accept_time, 
          counter = counter, 
          log_in = log_in
    )


@app.route('/log_in_user_type')
def log_in_user_type():
    return render_template('log_in_user_type.html')

@app.route('/user_log_in_up_purchaser')
def user_log_in_up_purchaser():
    return render_template('user_log_in_up_purchaser.html')

@app.route('/user_log_in_up_purveyor')
def user_log_in_up_purveyor():
    return render_template('user_log_in_up_purveyor.html')

@app.route('/log_in_purchaser', methods=['GET', 'POST'])
def log_in_purchaser():
    login = request.form.get('login')
    password = request.form.get('password')
    return render_template('log_in_purchaser')


@app.route('/log_in_purveyor', methods=['GET', 'POST'])
def log_in_purveyor():
    login = request.form.get('login')
    password = request.form.get('password')
    return render_template('log_in_purveyor')


@app.route('/sign_up_purchaser', methods=['GET', 'POST'])
def sign_up_purchaser():
    full_name = request.form.get('full_name')
    postal_address = request.form.get('postal_address')
    legal_address = request.form.get('legal_address')
    phone_number = request.form.get('phone_number')
    e_mail = request.form.get('e_mail')
    inn = request.form.get('inn')
    login = request.form.get('login')
    password = request.form.get('password')

    purchaser = (full_name, postal_address, legal_address, phone_number, e_mail, inn, login, password)

    #Базза данных для закупщика
    cur.execute("""CREATE TABLE IF NOT EXISTS purchasers(
        userid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        full_name TEXT,
        postal_address TEXT,
        legal_address TEXT,
        phone_number INTEGER,
        e_mail TEXT,
        inn INTEGER,
        login TEXT,
        password TEXT);
""")


    connect.commit()

    cur.execute("INSERT INTO purchasers (full_name, postal_address, legal_address, phone_number, e_mail, inn, login, password) VALUES(?, ?, ?, ?, ?, ?, ?, ?);", (full_name, postal_address, legal_address, phone_number, e_mail, inn, login, password))
    connect.commit()
    cur.execute("SELECT * FROM purchasers;")
    all_results = cur.fetchall()
    print(all_results)
    return render_template('sign_up_purchaser.html')




@app.route('/sign_up_purveyor', methods=['GET', 'POST'])
def sign_up_purveyor():
    full_name = request.form.get('full_name')
    postal_address = request.form.get('postal_address')
    legal_address = request.form.get('legal_address')
    phone_number = request.form.get('phone_number')
    e_mail = request.form.get('e_mail')
    inn = request.form.get('INN')
    OGRNIP_code = request.form.get('OGRNIP_code')
    login = request.form.get('login')
    password = request.form.get('password')


    return render_template('sign_up_purveyor.html')



@app.route('/logoutpurchaser')
def log_out_purchaser():
    redirect(url_for('root'))



@app.route('/logoutpurveyor')
def log_out_purveyor():
    redirect(url_for('root'))



@app.route('/purchaserprofile')
def purchaser_user_profile():
    return render_template('about_purchaser_user.html')



@app.route('/purveuorprofile')
def purveyor_user_profile():
    return render_template('about_purveyor_user.html')


@app.route('/createitem')
def create_item():
    creator = request.form.get('creator')
    price = request.form.get('price')
    title = request.form.get('title')
    text = request.form.get('text')
    status = request.form.get('status')

    return redirect(url_for('root'))


@app.route('/deliteitem')
def delete_item():
    
    return redirect(url_for('root'))


if __name__ == '__main__':
    app.run(debug=True)
