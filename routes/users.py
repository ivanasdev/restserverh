from flask import Blueprint, request, jsonify, render_template
from models.db import endconnection

users = Blueprint('users',__name__)


@users.route('/', methods = ["GET","POST"])
def homeusers():
    if request.method == 'GET':
        resp={"FLAG":"HOME"}
        return jsonify(resp)
    elif request.method == 'POST':
        return "SOME DIRECTORY OF POST DATA LINKS "
    

    

#GET
@users.route('/authuserlogin', methods = ["GET", "POST"])
def authuserlogin():
    if request.method=="GET":
        user=request.args.get('user')
        conexion = endconnection()
        users = []
        
        
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM `Users`")
            users = cursor.fetchall()
            conexion.close()
            return jsonify(users)
    
    elif user == 'ivno':
        conexion = endconnection()
        users = []
        with conexion.cursor() as cursor:
            cursor.execute("SELECT id_RegUser,st_UserName,id_MembUser FROM `tbl_RegUsers`")
            users = cursor.fetchall()
            conexion.close()
            return jsonify(users)

#POST 
@users.route('/authusersignup', methods = ["GET","POST"])
def signupuser():
    if request.method=="POST":
        idmemb=request.form['id_MemberUser']    
        user=request.form['username']   
        password=request.form['password']   
        firstname=request.form['firstname'] 
        lastnamep=request.form['lastnamep'] 
        lastnamem=request.form['lastnamem'] 
        email=request.form['email'] 
        cellphone=request.form['cellphone'] 
        
        conn=endconnection()
        with conn.cursor() as cursor:
            cursor.execute('INSERT INTO tbl_RegUsers(id_MembUser,st_UserName,st_PasswordUser,st_FirstNameUser,st_LastNameUserP,st_LastNameUserM,st_EmailUser,i_CellPhoneUser) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)',(idmemb,user,password,firstname,lastnamep,lastnamem,email,cellphone) )    
            conn.commit()
            return jsonify(idmemb,user, email, firstname)
        


@users.route('/teamogretchen', methods = ["GET","POST"])
def teamogretchen():
    if request.method=="GET":
        
        return "Te amo Gretchen, eres el amor de mi vida. Y recuerda que cada linea de codigo que hago es por ti mi vida"
