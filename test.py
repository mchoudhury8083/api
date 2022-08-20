from flask import Flask, request, jsonify
import mysql.connector as conn

app=  Flask(__name__)

mydb = conn.connect(host = "127.0.0.1", user = "root", password = "jaiMaata1!")
cursor = mydb.cursor()

@app.route('/load_dress', methods=['GET','POST'])
def load_dress_data():
    print("START loading data ")
    try:
        Dress_ID = request.json['Dress_ID']
        Style = request.json['Style']
        Price = request.json['Price']
        Rating = request.json['Rating']
        Size = request.json['Size']
        Season = request.json['Season']
        NeckLine = request.json['NeckLine']
        waiseline = request.json['waiseline']
        Material = request.json['Material']
        print( Dress_ID ,Style, Price ,Rating , Size  , Season  ,NeckLine  ,waiseline ,Material )
        sql = (
        "INSERT INTO sales.dress_dataset (Dress_ID,Style,Price,Rating,Size,Season,NeckLine,waiseline,Material) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
        value = [ Dress_ID,Style,Price,Rating,Size,Season,NeckLine,waiseline,Material]
        cursor.execute(sql, value)
        mydb.commit()
        return ("Succcessfully Data Loaded")
    except Exception as e:
        print(e)
        return ("System is under maintanance")
    return ("Please check your data and load again")

@app.route('/update_dress', methods=['GET','POST'])
def update_dress_data():
    print("START loading data ")
    try:
        Dress_ID = request.json['Dress_ID']
        Style = request.json['Style']
        Price = request.json['Price']
        Rating = request.json['Rating']
        Size = request.json['Size']
        Season = request.json['Season']
        NeckLine = request.json['NeckLine']
        waiseline = request.json['waiseline']
        Material = request.json['Material']
        print( Dress_ID ,Style, Price ,Rating , Size  , Season  ,NeckLine  ,waiseline ,Material )

        cursor.execute("""
           UPDATE sales.dress_dataset
           SET Style=%s,Price=%s,Rating=%s,Size=%s,Season=%s,NeckLine=%s,waiseline=%s,Material=%s
           WHERE Dress_ID=%s
        """, (Style,Price,Rating,Size,Season,NeckLine,waiseline,Material,Dress_ID))

        mydb.commit()
        return ("Succcessfully Updated data")
    except Exception as e:
        print(e)
        return ("System is under maintanance")
    return ("Please check your data and load again")

@app.route('/delete_dress', methods=['GET','POST'])
def delete_dress_data():
    print("START Delete data ")
    try:
        Dress_ID = request.json['Dress_ID']
        print( Dress_ID )
        sql_Delete_query = """Delete from sales.dress_dataset where Dress_ID = %s"""
        cursor.execute(sql_Delete_query, (Dress_ID,))
        mydb.commit()
        return ("Succcessfully Deleted data")
    except Exception as e:
        print(e)
        return ("System is under maintanance")
    return ("Please check your data and load again")

@app.route('/abc', methods= ['GET','POST'])
def test1():
    print("test1------")
    try:
        if( request.method=='POST'):
            a = request.json['num1']
            b = request.json['num2']
            c = a +b
            return jsonify(str(c))
    except Exception as e:
        print(e)

@app.route('/abc1', methods=['GET','POST'])
def test2():
    if(request.method == 'POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a *b
        return jsonify(str(result))


if __name__ == '__main__':
    app.run()
