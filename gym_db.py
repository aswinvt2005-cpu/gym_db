from mysql import connector

class dbConnect:
    def get_connected(self):
        try:
            self.connection=connector.connect(
                host="localhost",
                user="root",
                password="Aswin@2005",
                database="gym_db"
            )
            return self.connection
        except Exception as e:
            return None
class GymMemberManager(dbConnect):
    def get_object(self,id=None):
        try:
            self.cursor = self.connection.cursor()
            query="select *from member where id=%s"
            values=(id,)
            self.cursor.execute(query,values)
            record=self.cursor.fetchone()
            return record
        except Exception as e:
            return None
    def get(self):
        try:
            self.connect=super().get_connected()
            self.cursor=self.connect.cursor()
            query="select *from member"
            self.cursor.execute(query)
            record=self.cursor.fetchall()
            print(record)
        except Exception as e:
            print(e)
    def post(self,**kwargs):
        try:
            self.connect=super().get_connected()
            self.cursor=self.connect.cursor()
            query="insert into member(name,place,mobile,plan,fee,joined_date) values(%s,%s,%s,%s,%s,%s)"
            values=[v for v in kwargs.values()]
            self.cursor.execute(query,values)
            self.connect.commit()
            print("new member added successfully...!")
        except Exception as e:
            print(e)

    def retrieve(self, id=None):
        try:
            self.connect = super().get_connected()
            self.cursor = self.connect.cursor()
            query = """ 
                 select * from member
                 where id=%s
                 """
            values = [id, ]
            self.cursor.execute(query, values)
            records = self.cursor.fetchone()
            print(records)
        except Exception as e:
            print(e)

    def delete(self, id=None):
        try:
            self.connect = super().get_connected()
            self.cursor = self.connect.cursor()
            query = "DELETE FROM member WHERE id=%s"
            values = [id]
            self.cursor.execute(query, values)
            self.connect.commit()
            print(f"Member with id={id} deleted successfully...!")
        except Exception as e:
            print("Error in delete:", e)
    def put(self,id=None,**kwargs):
        try:
            record=self.get_object(id=id)
            if record!=None:
                self.cursor=self.connection.cursor()
                placeholder=""
                for k in kwargs.keys():
                    placeholder+=k+"=%s, "
                    placeholder=placeholder.rstrip(", ")
                    query=f"update member set {placeholder} where id=%s"
                    values=[v for v in kwargs.values()]
                    values.append(id)
                    self.cursor.execute(query,values)
                    self.connection.commit()
                    print("member details updated successfully..!")
            else:
                print("member not found..!")
        except Exception as e:
            print(e)



connection_instance=dbConnect()
print(connection_instance.get_connected())

member_instance=GymMemberManager()
#member_instance.post(name="amal",place="edappally",mobile="3219876456",plan="1 year",fee=2000,joined_date="2026-01-01")
member_instance.get()
print("_________")
member_instance.retrieve(id=1)
print("_____")
member_instance.delete(id=1)
print("-______-")
member_instance.put(3,place="kannur")
member_instance.get()