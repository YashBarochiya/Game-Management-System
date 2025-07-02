import mysql.connector
import streamlit as st

mydb = mysql.connector.connect(host='localhost', user='root', password='yash123', database='final_project')
mycursor = mydb.cursor()
print("connection is ready now")
def main():

    st.title("Game Management")

    option = st.sidebar.selectbox("Details About", ('User',"Player", "Match", "Clan", "Inventory", "Squad", "Server","Match Mode"))

    if option == "Player":
        st.subheader("Player!!")
        select = st.sidebar.selectbox("Operation", ("Create", "Update", "Read"))
        if select == "Create":
            st.subheader("Create a Player :)")
            player_email = st.text_input("Enter email")
            user_name=st.text_input("Enter user name")
            player_id = st.number_input("select any number", min_value=1)
            sql1 = "insert into player(u_eid,u_name,p_id,p_level,sq_id,cn_id) values (%s,%s,%s,1,null,null)"
            val1 = ( player_email,user_name,player_id)
            mycursor.execute(sql1, val1)
            mydb.commit()
            st.success("Success !")
        elif select == "Update":
            st.subheader("Update a Player :)")
            sele=st.selectbox("Change",("Level","MatchID","ClanID"))
            if sele=="Level":
                p_level = st.number_input("Enter New Level",min_value=1)
                player_id = st.number_input("Enter Player ID",min_value=0)
                sql="Update player set p_level=%s where p_id=%s"
                val=(p_level,player_id)
                mycursor.execute(sql,val)
                mydb.commit()
                st.success("Successfull!!")
            elif sele=="MatchID":
                newmid = st.number_input("Enter New Match ID", min_value=-1)
                player_id = st.number_input("Enter Player ID",min_value=0)
                sql = "Update player set m_id=%s where p_id=%s"
                val = (newmid, player_id)
                mycursor.execute(sql, val)
                mydb.commit()
                st.success("Successfull!!")
            elif sele=="ClanID":
                newclanid=st.number_input("Enter New Clan ID",min_value=-1)
                player_id = st.number_input("Enter Player ID",min_value=0)
                sql = "Update player set cn_id=%s where p_id=%s"
                val = (newclanid, player_id)
                mycursor.execute(sql, val)
                mydb.commit()
                st.success("Successfull!!")
        elif select=="Read":
            mycursor.execute('select * from player order by p_id;')
            result = mycursor.fetchall()
            for row in result:
                st.write(row)

    elif option == "Match":
        st.subheader("Match")
        op = st.sidebar.selectbox("Operation",("Create","Update","Read"))
        if op=="Create":
            server=st.selectbox("Select Server",("Rajkot","Mumbai","Lakhnau","Chennai","Bengaluru"))
            global SID,modeid, MapName, duration
            if server=="Rajkot":
                SID=1
            elif server=="Lakhnau":
                SID=3
            elif server == "Chennai":
                SID = 5
            elif server == "Mumbai":
                SID = 2
            elif server == "Bengaluru":
                SID = 4
            mode=st.selectbox("Select Mode",("Classic","Arena","Other"))
            if mode=="Classic":
                modeid='first'
                MapName=st.selectbox("Select Map",("Erangle","Miramar","Vikendi","LIVIK"))
                duration = st.number_input("Enter Duration")
            elif mode=="Arena":
                modeid='second'
                MapName=st.selectbox("Select Map",("TDM","GUN GAME","Santorini","Ultimate Arena","Domination"))
                duration = st.number_input("Enter Duration")
            elif mode=="Other":
                modeid='third'
                MapName=st.selectbox("Select Map",("War","Quick Match","Sniper traning","Payload"))
                duration = st.number_input("Enter Duration")
            id = st.number_input("Create Match ID",min_value=1)
            sql = "Insert into Matches(m_id,mo_id,m_name,m_duration,s_id) values (%s,%s,%s,%s,%s)"
            val = (id, modeid, MapName, duration, SID)
            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Success !")
        elif op == "Update":
            mid=st.number_input("Enter Match ID",min_value=0)
            global SIDup,modeidup, MapNameup, durationup
            servern=st.selectbox("Select Server",("Rajkot","Mumbai","Lakhnau","Chennai","Bengaluru"))
            if servern == "Rajkot":
                SIDup = 1
            elif servern == "Lakhnau":
                SIDup = 3
            elif servern == "Chennai":
                SIDup = 5
            elif servern == "Mumbai":
                SIDup = 2
            elif servern == "Bengaluru":
                SIDup = 4
            modeup = st.selectbox("Select Mode", ("Classic", "Arena", "Other"))
            if modeup == "Classic":
                modeidup = 'first'
                MapNameup = st.selectbox("Select Map", ("Erengle", "Miramar", "Vikendi", "LIVIK"))
                durationup = st.number_input("Enter Duration")
            elif modeup == "Arena":
                modeidup = 'second'
                MapNameup = st.selectbox("Select Map", ("TDM", "GUN GAME", "Santorini", "Ultimate Arena", "Domination"))
                durationup = st.number_input("Enter Duration")
            elif modeup == "Other":
                modeidup = 'third'
                MapNameup = st.selectbox("Select Map", ("War", "Quick Match", "Sniper traning", "Payload"))
                durationup = st.number_input("Enter Duration")
            sql = "Update matches set mo_id=%s,m_name=%s,m_duration=%s,s_id=%s where m_id=%s"
            val=(modeidup,MapNameup,durationup,SIDup,mid)
            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Success !")
        elif op=="Read":
            mycursor.execute('select * from matches;')
            result = mycursor.fetchall()
            for row in result:
                st.write(row)

    elif option == "Clan":
        st.subheader("Clan")
        opera = st.sidebar.selectbox("Operation",("Read", "Create", "Update"))
        if opera == "Read":
            mycursor.execute('select * from clan;')
            st.write("( 'ID' , 'name' , 'Level'  )")
            result = mycursor.fetchall()
            for row in result:
                st.write(row)
        elif opera=="Create":
            clanname = st.text_input("Enter Clan Name")
            matchid=st.number_input("Enter Match ID")
            clanid = st.number_input("Enter 7 DIGIT Number")
            sql="insert into Clan(ID,name,level,MatchID) values (%s,%s,'C',%s)"
            val=(clanid,clanname,matchid)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Success!")
        elif opera=="Update":
            levelclan=st.text_input("Enter Level (O,A+,A,B,C)")
            namenew=st.text_input("Enter New Name")
            changmid=st.number_input("Enter Match ID",min_value=-1)
            clanid = st.number_input("Enter Clan ID",min_value=-1)
            sql=("update Clan set level=%s,name=%s,MatchID=%s where ID=%s")
            val=(levelclan,namenew,changmid,clanid)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Success!")

    elif option == "Inventory":
        st.subheader("Inventory")
        opera = st.sidebar.selectbox("Operation", ("Read","Create"))
        if opera=="Create":
            player_name = st.text_input("Enter Name According to your User table")
            player_email = st.text_input("Enter email According to your User table")
            inventoryID = st.number_input("Create Id for Inventory",min_value=1)
            sql= "insert into Inventory (inve_id,u_name,u_eid) values (%s,%s,%s)"
            val = (inventoryID, player_name, player_email)
            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Success !")
        elif opera=="Read":
            mycursor.execute('select * from Inventory;')
            st.write("( 'ID' , 'name' , 'User' )")
            result = mycursor.fetchall()
            for row in result:
                st.write(row)

    elif option == "Squad":
        st.subheader("Squad")
        opera = st.sidebar.selectbox("Operation", ("Read", "Update","Create"))
        if opera=="Read":
            mycursor.execute('select * from squad;')
            st.write("( 'ID' , 'name' , 'MatchID' )")
            result = mycursor.fetchall()
            for row in result:
                st.write(row)
        elif opera=="Update":
            changname=st.text_input("Enter New Name")
            changmid=st.number_input("Enter New Match ID",min_value=0)
            squadid = st.number_input("Enter Squad Id", min_value=0)
            sql="update squad set sq_name=%s,m_id=%s where sq_id=%s"
            val=(changname,changmid,squadid)
            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Success!")
        elif opera=="Create":
            squadname = st.text_input("Enter Squad Name")
            squadid = st.number_input("Enter in character ",min_value=1)
            sql = "insert into squad(sq_id,sq_name,m_id) values (%s,%s,null)"
            val = (squadid, squadname)
            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Success!")

    elif option == "Server":
        st.subheader("Server")
        mycursor.execute('select * from server;')
        result = mycursor.fetchall()
        st.write("(ID , Name , Location)")
        for row in result:
            st.write(row)

    elif option=="Match Mode":
        st.subheader("Mode")
        mycursor.execute('select * from match_mode;')
        st.write("('ID' , 'name' )")
        result = mycursor.fetchall()
        for row in result:
            st.write(row)

    elif option=="User":
        select = st.sidebar.selectbox("Operation", ("Create", "Update", "Read"))
        if select=="Create":
            u_name=st.text_input("Enter Name")
            u_eid=st.text_input("Enter Email ID")
            sql='insert into user (u_name,u_eid) values (%s,%s)'
            val=(u_name,u_eid)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Done!")
        elif select=="Update":
            u_name=st.text_input("Enter new name")
            u_eid=st.text_input("Enter mail id")
            sql='update user set u_name=%s where u_eid=%s'
            vai=(u_name,u_eid)
            mycursor.execute(sql,vai)
            mydb.commit()
            st.success("Done!")
        elif select=="Read":
            mycursor.execute('select * from user order by u_name;')
            result = mycursor.fetchall()
            st.write("( 'Email' , 'User_name' )")
            for row in result:
                st.write(row)

if __name__ == "__main__":
    main()
