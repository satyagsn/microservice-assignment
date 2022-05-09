from config import db

class Dbperson(db.Model):
    __tablename__='EMPLOYEES'
    eno=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(30),index=False,unique=False,nullable=False)
    city=db.Column(db.String(30),index=False,unique=False,nullable=False)
    designation=db.column(db.String(30),index=False,unique=False,nullable=False)
    age=db.column(db.Integer,index=False,unique=False)


    def __init__(self,eno,name,city,designation,age):
        self.eno=eno
        self.name=name
        self.city=city
        self.designation=designation
        self.age=age

    def serialize(self):