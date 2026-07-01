import sqlite3
from flask import Flask, request, redirect

def database():
    data = sqlite3.connect("database.db")
    data.execute("""CREATE TABLE IF NOT EXISTS users_data(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        password TEXT,
        money INTEGER
    )""")
    data.commit()
    data.close()

database()
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    d = ""
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        deposit = request.form.get('deposit')
        widrawn = request.form.get('widrawn')
        new_password = request.form.get('new_password')

        data = sqlite3.connect("database.db")

        # Create new account
        if new_password:
            data.execute(
                "INSERT INTO users_data(name, password, money) VALUES (?,?,?)",
                (name, new_password, int(deposit))
            )
            data.commit()
            data.close()
            return redirect("/")

        # Withdraw money
        if widrawn and password:
            try:
                withdraw_amount = int(widrawn)
            except ValueError:
                data.close()
                return "Invalid withdraw amount"

            a = data.execute(
                "SELECT money FROM users_data WHERE name = ? AND password = ?",
                (name,password)
            )
            b = a.fetchall()
            if b:
                current_money = int(b[0][0])
                if withdraw_amount > current_money:
                    data.close()
                    return "Insufficient balance"
                new_money = current_money - withdraw_amount
                data.execute(
                    "UPDATE users_data SET money = ? WHERE name = ? AND password = ?",
                    (new_money, name, password)
                )
                data.commit()
                data.close()
                return redirect("/")
            else:
                data.close()
                return "User not found or wrong password"
        # Deposit money
        if deposit:
            deposit_amount = int(deposit)

            a = data.execute(
                "SELECT money FROM users_data WHERE name = ?",
                (name,)
            )
            b = a.fetchall()
            if not b:
                data.close()
                return "User not found"

            current_money = int(b[0][0])
            new_money = current_money + deposit_amount

            data.execute(
                "UPDATE users_data SET money = ? WHERE name = ?",
                (new_money, name)
            )
            data.commit()
            data.close()
            return redirect("/")



        # Show account info
        if name and password:
            a = data.execute(
                "SELECT * FROM users_data WHERE name = ? AND password = ?",
                (name, password)
            )
            b = a.fetchall()
            data.close()
            if b:
                user = b[0]
                d += f"""
                <div class="information_see">
                    <p>Here is information about {user[1]}</p>
                    <p>ID: {user[0]}</p>
                    <p>NAME: {user[1]}</p>
                    <p>PASSWORD: {user[2]}</p>
                    <p>EXISTED MONEY: {user[3]}</p>
                </div>
                """
                return d
    else:
        return redirect("/main_work")

@app.route("/main_work",methods=['GET', 'POST'])
def main_work():
    return """
    
    
    
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="index.css">
</head>
<style>
*{
    margin: 0px;
}
body{
    background-color: black;
}
.upper_first_culumn{
    display: flex;
}
.upper_first_logo_area{
    color: red;
    font-size: 40px;
}
.upper_first_left_section_area{
    color: white;
    display: flex;
    margin-left: 800px;
}
.LIST_IN_first_culumn{
    background-color: rgb(51, 51, 51);
    margin-left: 20px;
    padding-right: 20px;
    margin-top: 10px;
    margin-bottom: 10px;
}

.upper_second_culumn{
    color: rgb(0, 255, 0);
    font-size: 50px;
    margin-left: 500px;
}
.image{
    background-color: rgb(0, 0, 0);
    width: 100%;
    height: 250px;
}
.in_image_content{
    color: rgb(255, 255, 255);
    font-size: 30px;
}
.in_image_content_first_line{
    padding-top: 70px;
    margin-left: 450px;
    color: white;
}
.in_image_content_second_line{
    margin-left: 350px;
    color: white;
}
.all_bank_option{
    display: flex;
    margin-top: 30px;
    margin-left: 30px;
    animation: a 2s;
}
@keyframes a{
    0%{
        transform: translateY(150px);
        opacity: 0;
    }
    100%{
        opacity: 1;
    }
}

.BOX_ONE{
    width: 300px;
    height: 100px;
    background-color: rgb(31, 31, 31);
    color: aqua;
    border-radius: 500px;
    cursor: pointer;
}
.BOX_TWO{
    width: 300px;
    height: 100px;
    background-color: rgb(31, 31, 31);
    margin-left: 40px;
    color: aqua;
    border-radius: 500px;
    cursor: pointer;
}
.BOX_THREE{
    width: 300px;
    height: 100px;
    background-color: rgb(31, 31, 31);
    margin-left: 40px;
    color: aqua;
    border-radius: 500px;
    cursor: pointer;
}
.BOX_four{
    width: 300px;
    height: 100px;
    background-color: rgb(31, 31, 31);
    margin-left: 40px;
    color: aqua;
    border-radius: 500px;
    cursor: pointer;
}
.BOX_CONTENT{
    margin-left: 20px;
    margin-top: 35px;
    font-size: 30px;
}
.BOX_four:hover{
    transform: scale(1.05);
}
.BOX_ONE:hover{
    transform: scale(1.05);
}
.BOX_TWO:hover{
    transform: scale(1.05);
}
.BOX_THREE:hover{
    transform: scale(1.05);
}
.upper_first_left_section_area:hover{
    cursor: pointer;
}
.LIST_IN_first_culumn:hover{
    background-color: blue;
}
a{
    color: aqua;
    text-decoration: none;
}
body{
  background-color: black;
}
form{
  margin-top: 150px;
  margin-left: 500px;
  background-color: rgb(31, 31, 31);
  margin-right: 280px;
  padding: 50px;
}
.first_name{
    margin-left: 136px;
}
.first_deposite{
    margin-left: 106px;
}
.first{
  margin-left: 56.5px;
}
p{
  color: aqua;
}
button{
  margin-left: 100px;
  background-color: bisque;
  font-size: 30px;
  color: blue;
  cursor: pointer;
}
input{
  background-color: rgb(12, 16, 250);
  color: white;
  font-size: 20px;
}
.TOPIC_NAME{
    color: rgb(0, 255, 21);
    font-size: 20px;
    margin-top: -50px;
    
}
.create_account{
    display: none;
}
.WIDRAWN_MONEY{
    display: none;
}
.DEPOSITE_MONEY{
    display: none;
}
.back{
    color: red;
    width: auto;
    height: auto;
    background-color: rgb(255, 230, 0);
    position: absolute;
    margin-left: 500px;
    font-size: 20px;
    cursor: pointer;
}
.see_money{
    display: none;
}
.information_see{
    display: none;
}
.fast_on_it{
    color: rgb(8, 253, 0);
}
</style>
<body>
    <div class="main_body">
    <div class="upper_first_culumn">
        <div class="upper_first_logo_area">VIPER</div>
        <div class="upper_first_left_section_area">
            <ul class="LIST_IN_first_culumn">HOME</ul>
            <ul class="LIST_IN_first_culumn">SERVISE</ul>
            <ul class="LIST_IN_first_culumn">ABOUT</ul>
        </div>
    </div>
    <div class="upper_second_culumn">
        <p class="fast_on_it">VIPER BANK</p>
    </div>
    <div class="image_section">
        <div class="image">
            <div class="in_image_content">
                <p class="in_image_content_first_line">HELLO MY NAME IS AABAN.</p>
                <P class="in_image_content_second_line">A SOFTWARE ENGINER AND BUISNESS MAN</P>
            </div>
        </div>
    </div>
    <div class="all_bank_option">
    
        <div class="BOX_ONE" onclick="BOX_ONE_in_js()">
            <p class="BOX_CONTENT">CREATE ACCOUNT</p>
        </div>
        <div class="BOX_TWO" onclick="BOX_TWO_in_js()">
            <p class="BOX_CONTENT">WIDRAWN MONEY</p>
        </div>
        <div class="BOX_THREE" onclick="BOX_THREE_in_js()">
            <p class="BOX_CONTENT">DEPOSITE MONEY</p>
        </div>
        <div class="BOX_four">
            <p class="BOX_CONTENT" onclick="BOX_FOUR_in_js()">SEE YOUR MONEY</p>
        </div>
    </div>
    </div>
    
    <div class="create_account">
        <div class="back" onclick="back()">back</div>
    <form method="post" action="/">
        <p class="TOPIC_NAME">CREATE A NEW BANK ACCOUNT</p>
        <p>
            NAME:<input class="first_name" type="text" name="name">
        </p>
        <p>
            NEW PASSWORD:<input class="first" type="text" name="new_password">
        </p>
        <p>
            DEPOSITE:<input class="first_deposite" type="text" name="deposit">
        </p>
        <button>submit</button>

    </form>
    </div>

    <div class="WIDRAWN_MONEY">
        <div class="back" onclick="back()">back</div>
    <form method="post" action="/">

        <p class="TOPIC_NAME">WIDRAWN MONEY FROM BANK ACCOUNT</p>
        <p>
            NAME:<input class="first_NAME" type="text" name="name">
        </p>
        <p>
            PASSWORD:<input class="first_password" type="text" name="password">
        </p>
        <p>
            WIDRAWN:<input class="first" type="text" name="widrawn">
        </p>
        <button>submit</button>

    </form>
    </div>



    <div class="DEPOSITE_MONEY">
        <div class="back" onclick="back()">back</div>
    <form method="post" action="/">
        <p class="TOPIC_NAME">DEPOSITE MONEY IN BANK ACCOUNT</p>
        <p>
            NAME:<input class="first_name" type="text" name="name">
        </p>
        <p>
            DEPOSITE:<input class="first_deposite" type="text" name="deposit">
        </p>
        <button>submit</button>
    </form>
    </div>

    <div class="see_money">
            <div class="back" onclick="back()">back</div>
    <form method="post" action="/">
        <p class="TOPIC_NAME">DEPOSITE MONEY IN BANK ACCOUNT</p>
        <p>
            NAME:<input class="first_name" type="text" name="name">
        </p>
        <p>
            PASSWORD:<input class="first_deposite" type="text" name="password">
        </p>
        <button class="submit">submit</button>
    </form>
    </div>
    <div class="information_see">
        <p>here is information about {name}</p>
        <P>ID:            {id}</P>
        <p>NAME:          {name}</p>
        <P>PASSWORD:      {password}</P>
        <P>EXISTED MONEY: {money}</P>
    </div>

    <script>
        
const main_body = document.querySelector(".main_body");
const BOX_ONE = document.querySelector(".BOX_ONE")
const create_account = document.querySelector(".create_account")
const widrawn_money = document.querySelector(".WIDRAWN_MONEY")
const deposit_money = document.querySelector(".DEPOSITE_MONEY")
const see_money = document.querySelector(".see_money")
const submit = document.querySelector(".submit")
const information_see = document.querySelector(".information_see")
function BOX_ONE_in_js(){
    main_body.style.display = "none"
    create_account.style.display = "block"
}

function BOX_TWO_in_js(){
    main_body.style.display = "none"
    widrawn_money.style.display = "block"
}
function BOX_THREE_in_js(){
    main_body.style.display = "none"
    deposit_money.style.display = "block"
}
function back(){
    main_body.style.display = "block"
    create_account.style.display = "none"
    widrawn_money.style.display = "none"
    deposit_money.style.display = "none"
    see_money.style.display = "none"
}
function BOX_FOUR_in_js(){
    main_body.style.display = "none"
    see_money.style.display = "block"
}
submit.addEventListener("click",()=>{
    see_money.style.display = "none"
    information_see.style.display = "block"
})

    </script>
</body>
</html>
    
    
    
    """

if __name__ == '__main__':
    app.run(debug=True)
