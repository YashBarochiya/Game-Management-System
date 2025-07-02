import mysql.connector
import streamlit as st

mydb=mysql.connector.connect(host='localhost',user='root',password='yash123',database='pro')
mycursor=mydb.cursor()
print("connection is ready now")
def main():
    st.title("cruder operation")

    option=st.sidebar.selectbox("select an operation",("create","read","update","delete"))

    if option=="create":
        st.subheader("create a record")
        name=st.text_input("Enter name")
        email=st.text_input("Enter Email")
        if st.button("create"):
            sql="insert into users(name,email) values (%s,%s)"
            val=(name,email)

            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Success !"
            )


    elif option=="read":
        st.subheader("create a read")
        mycursor.execute("select * from users")
        result= mycursor.fetchall()
        for row in result:
            st.write(row)



    elif option=="update":
        st.subheader("create a update")
        id=st.number_input("Enter ID",min_value=1)
        name= st.text_input("enter new name")
        email=st.text_input("enter new email")
        if st.button("update"):
            sql="update users set name=%s,email=%s where id=%s "
            value=(name,email,id)
            mycursor.execute(sql,value)
            mydb.commit()
            st.success("update successfully")
    elif option=="delete":
        st.subheader("create a delete")
        id=st.number_input("enter the id",min_value=1)
        if st.button("delete"):
            sql="delete from users where id=%s"
            value=(id,)
            mycursor.execute(sql,value)
            mydb.commit()
            st.success("delete successfully!")


if __name__=="__main__":
    main()