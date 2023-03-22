import psycopg2

from flask import Flask ,request
app=Flask("crud")
conn=psycopg2.connect(database='postgres',user='postgres',password='131120',host='psqlos',port='5432')
cursor=conn.cursor()
try:
    cursor.execute('''create table employee_details(id serial,first_name varchar(15),last_name varchar(15),designation varchar(15))''')
    conn.commit()
    cursor.execute('''insert into employee_details(first_name,last_name,designation) values(%s,%s,%s)''',('Krishna','Digole','Intern'))
    conn.commit()
except:
    pass
finally:
    cursor.execute("ROLLBACK")
    conn.commit()

@app.route("/showemployees",methods=["GET"])
def all_emp():
  cursor.execute("select * from employee_details")
  result=cursor.fetchall()
  
  return {"response":result}

@app.route("/addemployee",methods=["POST"])
def add_emp():
    data=request.get_json()
    first_name=data['first_name']
    last_name=data['last_name']
    designation=data['designation']
    cursor.execute('''insert into employee_details(first_name,last_name,designation) values(%s,%s,%s)''',(first_name,last_name,designation))
    conn.commit()
    return {"success":"200"}

@app.route("/employees/<id>",methods=["GET"])
def get_emp(id):
    print(type(id))
    id=int(id)
    cursor.execute("select * from employee_details where id={}".format(id))
    result=cursor.fetchall()
    print(result)
    return {"result":result[0]}

@app.route("/employees/editemp/<id>",methods=["PUT"])
def edit_emp(id):
    id=int(id)
    data=request.get_json()
    first_name=data['first_name']
    last_name=data['last_name']
    designation=data['designation']
    cursor.execute('''update employee_details set first_name=%s ,last_name=%s,designation=%s where id=%s''',(first_name,last_name,designation,id))
    conn.commit()
    return {"response":"updated"}

@app.route("/employees/deleteemp/<id>",methods=["DELETE"])
def delete_emp(id):
    
    cursor.execute('''delete from employee_details where id=%s''',(id)) 
    conn.commit()
    return {"response":"Deleted"} 
  

app.run(port=7845,debug=True)
