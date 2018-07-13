#1

create database assignment;
use assignment;
create table Books(book_id varchar(5) primary key,title_id varchar(5),location char(10),genre char(10));

create table Title(Title_id varchar(5) primary key, title char(20), ISBN varchar(10), publisher_id varchar(5), publication_year int(5));

create table Publishers(publisher_id varchar(5) primary key, name char(10), street_address varchar(20),suite_number varchar(10), zipcode_id int(10));

create table Zipcodes(zipcode_id int(10) primary key, city char(10),state char(10),zipcode int(10));

create table Authors_titles(authortitle_id varchar(5) primary key, author_id varchar(5), Title_id varchar(5));

create table Authors(author_id varchar(5) primary key, first_name char(10), middle_name char(10), last_name char(10));

#2
db = MySQldb.connect("localhost","assignment","root","root123")
cursor = db.cusor()

sql1 = "insert into Books values('B1', 'T1','delhi', 'thrilling')"
sql2 = "insert into Title values('T1','angels and demons','123', 'P1',2007)"

try:
    cursor.execute(sql1)
    cursor.execute(sql2)
    db.commit()

except:
    db.rollback()

db.close()


#3


db = MySQldb.connect("localhost","assignment","root","root123")
cursor = db.cusor()

sql1 = "select * from Books"
sql2 = "update Books set location='hyderabad' where book_id='B1'"
sql3 = "select * from Books"

try:
    cursor.execute(sql1)
    cursor.execute(sql2)
    cursor.execute(sql3)
    db.commit()

except:
    db.rollback()

db.close()
