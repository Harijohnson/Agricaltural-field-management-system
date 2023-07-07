import pymysql
import re
import sys

myConn = pymysql.connect(host='localhost', user='root', passwd='root', db='agri')
cur = myConn.cursor()
print('Hi Welcome To Field PORTAL!!')
print('Select Your Role')
print('To create a account press number 0')
print('If you are owner press number 1')
print('If you are manager press number 2')
rol = int(input())  # choosing the role


def selectq(fild):
   print('If You are in First Half of the Year then press ==> 1')
   print('If You are in Second Half of the Year then press ==> 2')
   se_q = int(input())  # select the half of the year
   print('Time to Give Basic Information ! !! !!!')  # Basic Information
   print()
   field = fild
   print('Enter The Size Of Land In Acre')
   fi_siz = int(input())
   print('Enter the Basic Salary Of the Labors')
   fi_lab_sal = int(input())
   print('Enter the Price Of 1 Hour Rent Of Tractors')
   fi_rent = int(input())
   print('Enter The Name Of The Crop You Selected For This Half')
   crop = input()
   print("Enter the Start DATE Of Work ")
   date=input()
   cur.execute('insert into base_info values(%s,%s,%s,%s,%s,%s.%s)', (se_q, field, fi_siz, fi_lab_sal, fi_rent, crop,date))
   myConn.commit()
   field = fild
   if se_q == 1:
       print(' Welcome to the First Half of Harvesting!!')
       print('If You Want To Update Land Preparation Tractor  Information Then press ==>  1 ')
       print('If You Want To Update Seed  Information Then press ==>  2 ')
       print('If You Want To Update The Medicine Information Then press ==>  3 ')
       print('If You Want To Update The Work On Field Information Then press ==>  4 ')
       print('If You Want To Update The Water Information Then press ==>  5 ')
       print('If You Want To Update The Harvest Information Then press ==>  6 ')
       print('If You Want To End The Process Then press ==>  7 ')
       info = int(input())
       if info == 1:
           tract(field)  # tractor information
       elif info == 2:
           seed(field)  # select the seed of crop
       elif info == 3:
           med_wrk(field)  # medicine work call
       elif info == 4:
           labor_wrk(field)  # workers call fun
       elif info == 5:
           water(field)  # water expenses
       elif info == 6:
           harvest(field)  # harvesting Expenses Function
       elif info == 7:
           exit()
   elif se_q == 2:
       print('Welcome to the Second Half of Harvesting!!')
       print('If You Want To Update Land Preparation Tractor  Information Then press ==>  1 ')
       print('If You Want To Update Seed  Information Then press ==>  2 ')
       print('If You Want To Update The Medicine Information Then press ==>  3 ')
       print('If You Want To Update The Work On Field Information Then press ==>  4 ')
       print('If You Want To Update The Water Information Then press ==>  5 ')
       print('If You Want To Update The Harvest Information Then press ==>  6 ')
       print('If You Want To End The Process Then press ==>  7 ')
       info = int(input())
       if info == 1:
           tract(field)  # tractor information
       elif info == 2:
           seed(field)  # select the seed of crop
       elif info == 3:
           med_wrk(field)  # medicine work call
       elif info == 4:
           labor_wrk(field)  # workers call fun
       elif info == 5:
           water(field)  # water expenses
       elif info == 6:
           harvest(field)  # harvesting Expenses Function
       elif info == 7:
           exit()


def ow_check():  # first check of emil & password if it fails call the function email & pass for owners role
   print('Enter Your Email please...')  # same things followed by owners selection
   email = input()  # email input

   print('Please enter your Password...')
   pas = input()  # password input

   print('Enter Your Field Name !!')
   field = input()  # Field Name

   cur.execute("select email,pass,fild_name from users where role='owner'")
   flag = 0
   result = cur.fetchall()
   for i in result:
       db_email = i[0]
       db_pas = i[1]
       db_fild_name = i[2]
       if db_email == email:
           if db_pas == pas:
               if db_fild_name == field:
                   view(field)
                   break
               else:
                   flag = 1
           else:
               flag = 1
       else:
           flag = 1

   if flag == 1:
       print('Please Provide Correct Email or Password!!!')
       ow_check()  # recursive function call itself


def ma_check():  # first check of emil & password if it fails call the function email & pass for managers role
   print('Enter Your Email please...')  # same things followed by owners selection
   email = input()  # email input

   print('Please enter your Password...')
   pas = input()  # password input

   print('Enter Your Field Name !!')
   field = input()  # Field Name

   cur.execute("select email,pass,fild_name from users where role='manager'")
   flag = 0
   result = cur.fetchall()
   for i in result:
       db_email = i[0]
       db_pas = i[1]
       db_fild_name = i[2]

       if db_email == email:
           if db_pas == pas:
               if db_fild_name == field:
                   print('If You Want To Set Basic Information Then press ==>  1 ')
                   print('If You Want To Update Land Preparation Tractor  Information Then press ==>  2 ')
                   print('If You Want To Update Seed  Information Then press ==>  3 ')
                   print('If You Want To Update The Medicine Information Then press ==>  4 ')
                   print('If You Want To Update The Work On Field Information Then press ==>  5 ')
                   print('If You Want To Update The Water Information Then press ==>  6 ')
                   print('If You Want To Update The Harvest Information Then press ==>  7 ')
                   print('If You Want To End The Process Then press ==>  8 ')
                   info = int(input())
                   if 0 < info < 9:
                       if info == 1:
                           selectq(field)
                       elif info == 2:
                           tract(field)  # tractor information
                       elif info == 3:
                           seed(field)  # select the seed of crop
                       elif info == 4:
                           med_wrk(field)  # medicine work call
                       elif info == 5:
                           labor_wrk(field)  # workers call fun
                       elif info == 6:
                           water(field)  # water expenses
                       elif info == 7:
                           harvest(field)  # harvesting Expenses Function
                       elif info == 8:
                           exit()
                   else:
                       print('Please Enter Required Input Alone !!!!!!')
                       next_s(field)
               break
       else:
           flag = 1

   if flag == 1:
       print('Please Provide Correct Email or Password!!!')
       ma_check()  # recursive function call itself


def exit():
   sys.exit()


def next_s(field):
   field = field
   print('If You Want To Set Basic Information Then press ==>  1 ')
   print('If You Want To Update Land Preparation Tractor  Information Then press ==>  2 ')
   print('If You Want To Update Seed  Information Then press ==>  3 ')
   print('If You Want To Update The Medicine Information Then press ==>  4 ')
   print('If You Want To Update The Work On Field Information Then press ==>  5 ')
   print('If You Want To Update The Water Information Then press ==>  6 ')
   print('If You Want To Update The Harvest Information Then press ==>  7 ')
   print('If You Want To End The Process Then press ==>  8 ')
   info = int(input())
   if 0 > info < 8:
       if info == 1:
           selectq(field)
       elif info == 2:
           tract(field)  # tractor information
       elif info == 3:
           seed(field)  # select the seed of crop
       elif info == 4:
           med_wrk(field)  # medicine work call
       elif info == 5:
           labor_wrk(field)  # workers call fun
       elif info == 6:
           water(field)  # water expenses
       elif info == 7:
           harvest(field)  # harvesting Expenses Function
       elif info == 8:
           exit()
   else:
       print('Please Enter Required Input Alone !!!!!!')
       next_s(field)


def em_check():
   print('Enter Your Email')
   cr_email = input()
   regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
   if re.fullmatch(regex, cr_email):
       c_email = cr_email
       return c_email
   else:
       print('Enter Your Email Correctly !!!')
       em_check()


def pas_check():
   print('Enter Your Password With The Length Of 8-16 Characters')
   cr_pas = input()
   if 8 <= len(cr_pas) <= 16:
       c_pass = cr_pas
       return c_pass
   else:
       pas_check()


def create_account():  # create an account
   print('Enter 1 If You are Role is Owner')
   print('Enter 2 If You are Role is Manager')
   cr_rol = int(input())

   if cr_rol == 1:
       cr_rol = 'Owner'
   elif cr_rol == 2:
       cr_rol = 'Manager'
   else:
       print('Please Enter the Required Input !!!!!!!')
       create_account()  # recursive function
   print('Enter Your Name!!')
   cr_name = input()

   print('Enter Your Email')
   cr_email = input()
   regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
   if re.fullmatch(regex, cr_email):
       c_email = cr_email
   else:
       c_email = em_check()

   print('Enter Your Password With The Length Of 8-16 Characters')
   cr_pas = input()
   if 8 <= len(cr_pas) <= 16:
       c_pass = cr_pas
   else:
       c_pass = pas_check()

   print('Enter Your Field Name !!')
   fi_name = input()

   cur.execute("insert into users values(%s,%s,%s,%s,%s)",
               (cr_rol, cr_name, c_email, c_pass, fi_name))  # inserting new users to db by the formate of string

   if cr_rol == 'Owner':
       print('Let Sign in !!!')
       ow_check()


   elif cr_rol == 'Manager':
       print('Let Sign in !!!!')
       ma_check()

   myConn.commit()


def tract(field):
   fi_field = field
   print()
   print('Welcome To Tractor Work!!!')
   print()
   print('Enter the Date Of Tractor Works')
   print('Enter The Date By Formate Of YYYY-MM-DD')
   tr_date = input()
   print('Enter Total Hours Of Tractor Work Your Fields!!')
   print('Enter the Values By Formate Of HH:MM')
   tr_time = input()
   print('Total days of Work')
   tr_day = int(input())
   cur.execute('insert into trac_work values(%s,%s,%s,%s)', (fi_field, tr_date, tr_time, tr_day))
   myConn.commit()

   print('If You Want To Update Seed  Information Then press ==>  1 ')
   print('If You Want To Update The Medicine Information Then press ==>  2 ')
   print('If You Want To Update The Work On Field Information Then press ==>  3 ')
   print('If You Want To Update The Water Information Then press ==>  4 ')
   print('If You Want To Update The Harvest Information Then press ==>  5 ')
   print('If You Want To End The Process Then press ==>  6 ')
   info = int(input())
   if info == 1:
       seed(field)  # select the seed of crop
   elif info == 2:
       med_wrk(field)  # medicine work call
   elif info == 3:
       labor_wrk(field)  # workers call fun
   elif info == 4:
       water(field)  # water expenses
   elif info == 5:
       harvest(field)  # harvesting Expenses Function
   elif info == 6:
       exit()
   else:
       print('Please Enter Required Input Alone !!!!!!')
       next_s(field)


def labor_wrk(field):
   field = field
   print('Enter the Name Of The Work')
   wrk = input()
   print('Enter The Number Of Workers doing that Work')
   num_worker = int(input())
   print('Enter The Date Of The Work')
   print('Enter The Date By Formate Of YYYY-MM-DD')
   wr_date = input()
   cur.execute('insert into work values(%s,%s,%s,%s)', (field, wrk, wr_date, num_worker))
   myConn.commit()
   print('If You Want To Update The Medicine Information Then press ==>  1 ')
   print('If You Want To Update The Work On Field Information Then press ==>  2 ')
   print('If You Want To Update The Water Information Then press ==>  3 ')
   print('If You Want To Update The Harvest Information Then press ==>  4 ')
   print('If You Want To End The Process Then press ==>  5 ')
   info = int(input())
   if info == 1:
       med_wrk(field)  # medicine work call
   elif info == 2:
       labor_wrk(field)  # workers call fun
   elif info == 3:
       water(field)  # water expenses
   elif info == 4:
       harvest(field)  # harvesting Expenses Function
   elif info == 5:
       exit()
   else:
       print('Please Enter Required Input Alone !!!!!!')
       next_s(field)


def med_wrk(field):
   field = field
   print('Enter the Name Of The Medicine')
   wrk = input()
   print('Enter The Number Of Workers doing that Work')
   num_worker = int(input())
   print('Enter The Date Of The Work')
   print('Enter The Date By Formate Of YYYY-MM-DD')
   wr_date = input()
   cur.execute('insert into work values(%s,%s,%s,%s)', (field, wrk, wr_date, num_worker))
   myConn.commit()
   print('If You Want To Update The Medicine Information Then press ==>  1 ')
   print('If You Want To Update The Work On Field Information Then press ==>  2 ')
   print('If You Want To Update The Water Information Then press ==>  3 ')
   print('If You Want To Update The Harvest Information Then press ==>  4 ')
   print('If You Want To End The Process Then press ==>  5 ')
   info = int(input())
   if info == 1:
       med_wrk(field)  # medicine work call
   elif info == 2:
       labor_wrk(field)  # workers call fun
   elif info == 3:
       water(field)  # water expenses
   elif info == 4:
       harvest(field)  # harvesting Expenses Function
   elif info == 5:
       exit()
   else:
       print('Please Enter Required Input Alone !!!!!!')
       next_s(field)


def water(field):
   field = field
   print('Enter The Liters Of Water Is Used For Irrigation')
   liter = int(input())
   print('Enter The Date Of Irrigation')
   print('Enter The Date Of Irrigation In The format Of YYYY-MM-DD')
   dat_water = input()
   cur.execute('insert into water values(%s,%s,%s)', (field, liter, dat_water))
   myConn.commit()
   print('If You Want To Update The Medicine Information Then press ==>  1 ')
   print('If You Want To Update The Work On Field Information Then press ==>  2 ')
   print('If You Want To Update The Water Information Then press ==>  3 ')
   print('If You Want To Update The Harvest Information Then press ==>  4 ')
   print('If You Want To End The Process Then press ==>  5 ')
   info = int(input())
   if info == 1:
       med_wrk(field)  # medicine work call
   elif info == 2:
       labor_wrk(field)  # workers call fun
   elif info == 3:
       water(field)  # water expenses
   elif info == 4:
       harvest(field)  # harvesting Expenses Function
   elif info == 6:
       exit()
   else:
       print('Please Enter Required Input Alone !!!!!!')
       next_s(field)


def harvest(field):
   field = field
   print('Enter The Number Of Days Harvested')
   har_num_day = int(input())
   print('Enter The Number Of Workers Doing Work For Harvesting')
   wrokers_har = int(input())
   print('Enter The Total Cost Of Heavy Equipments like Transportation And All')
   cost = int(input())
   print('Enter The Date Of Harvesting')
   print('The Formate Of YYYY-MM-DD')
   dat = input()
   print('Enter The Total Profit Amount ')
   proft = int(input())
   cur.execute('insert into harvest values(%s,%s,%s,%s,%s,%s)', (field, har_num_day, wrokers_har, cost, dat, proft))
   print('Please Enter End To Finish This Part OF Harvesting')
   en = input()
   myConn.commit()
   if en == "END" or en == 'End' or en == 'end':
       print('That is all for This Half Year! :)')
       exit()


def seed(field):
   print('Enter The Name Of Seed')
   name_seed = input()
   field = field
   print('Enter The Name Of Crop')
   crop = input()
   print('Enter The Quantity Of Seed in Kg')
   qun = int(input())
   print('Price Of The Seed For 1 Kg')
   pric_sedd = int(input())
   print('Date of Seed Buying')
   dat = input()
   cur.execute('insert into seed values(%s,%s,%s,%s,%s,%s)', (field, name_seed, crop, qun, pric_sedd, dat))
   myConn.commit()
   print('If You Want To Update The Medicine Information Then press ==>  1 ')
   print('If You Want To Update The Work On Field Information Then press ==>  2 ')
   print('If You Want To Update The Water Information Then press ==>  3 ')
   print('If You Want To Update The Harvest Information Then press ==>  4 ')
   print('If You Want To End The Process Then press ==>  5 ')
   info = int(input())
   if info == 1:
       med_wrk(field)  # medicine work call
   elif info == 2:
       labor_wrk(field)  # workers call fun
   elif info == 3:
       water(field)  # water expenses
   elif info == 4:
       harvest(field)  # harvesting Expenses Function
   elif info == 5:
       exit()
   else:
       print('Please Enter Required Input Alone !!!!!!')
       next_s(field)


'''lest get into owners part '''


def view(field):
   fild = field
   print('Please Select Part Of The Harvesting !!!')
   print('Please Enter the Year to See The Results !!')
   yer = int(input())
   print('Please Enter If You Want to See The Full Year Information The Press ==> 1')
   print('Please Enter If You Want to See The First Half Year Information The Press ==> 2')
   print('Please Enter If You Want to See The Second Half Year Information The Press ==> 3')
   print('If You Want To End The Process Then press ==>  4 ')
   qt = int(input())
   if qt == 1:
       ful(fild,yer)
   elif qt == 2:
       fi(fild,yer)
   elif qt == 3:
       se(fild,yer)
   elif qt == 4:
       exit()
   else:
       print('Please Enter Required Input Only !!!!!')
       view(fild)


def ful(fild,yer):
   cur.execute('select * from base_info where name_fild=%s and year(date_year)=%s', (fild,yer))
   base = cur.fetchall()
   tr_cost = 0
   lab_sal = 0
   for i in base:
       lab_sal = i[3]
       tr_cost = i[4]
   cur.execute('select * from seed where field=%s and year(date_seed)=%s', (fild,yer))
   seed = cur.fetchall()

   cur.execute('select * from water where field_name=%s and year(irr_date)=%s', (fild,yer))
   water = cur.fetchall()

   cur.execute('select * from work where fild_name=%s and year(wr_date)=%s', (fild,yer))
   work = cur.fetchall()

   cur.execute('select * from trac_work where fild_name=%s and year(tr_date)=%s', (fild,yer))
   tract = cur.fetchall()

   cur.execute('select * from harvest where field=%s and year(harv_date)=%s', (fild,yer))
   harv = cur.fetchall()
   tr_co = 0
   tr_time = ""  # time calculate
   for i in tract:
       print('Your Fild Name  => ', end=" ")
       print(i[0])  # fild name
       print('Date Of Tractor Work  => ', end=" ")
       print(i[1])  # tractor date
       print('Time Taken By Tractor Work  => ', end=" ")
       print(i[2])  # tractor time
       tr_time = i[2]
       print('Number Of Days Work On Tractor  => ', end=" ")
       print(i[3])  # tractor days
       print("That's All For Land Preparation !!!! :) ")

   tr_time = str(tr_time).split(':')
   tr_co = int(tr_time[0]) * tr_cost

   se_cost = 0
   for i in seed:
       # print('Your Fild Name  => ', end=" ")
       # print(i[0])  # fild name
       print('Seed Name  => ', end=" ")
       print(i[1])  # seed name
       print('Your Crop Name  => ', end=" ")
       print(i[2])  # crop name
       print('Quantity of Seed Used  => ', end=" ")
       print(i[3])  # quantity of product
       print('Total Price  Of The Seed => ', end=" ")
       print(i[4] * i[3])  # price of product by Kg
       se_cost = i[4] * i[3]
   for i in water:
       # print('Your Fild Name  => ', end=" ")
       # print(i[0])  # fild name
       print('Used Water   => ', end="Liters")
       print(i[1])  # used water in Litters
       print('Watering Date  => ', end=" ")
       print(i[2])  # Watering date

   wor_cost = 0
   for i in work:
       print('Work  => ', end=" ")
       print(i[1])  # work
       print('Work Date  => ', end=" ")
       print(i[2])  # work date
       print('Number Of Workers   => ', end=" ")
       print(i[3])  # number of worker
       wor_cost = i[3]
   wor_cost = wor_cost * lab_sal
   en = 0
   hv = 0
   wor = 0
   for i in harv:
       print('Number Of Workers Involved n Harvesting  => ', end=" ")
       print(i[2])  # number of workers
       wor = i[2]
       print('Heavy Work => ', end=" ")
       print(i[3])  # total  heavy work
       hv = i[3]
       print('Harvesting Date  => ', end=" ")
       print(i[4])  # harvest date
       print('Total Earnings  => ', end=" ")
       print(i[5])  # total profit
       en = i[5]
   print('Total Profit')
   print(int(en) - (int(hv) + int(wor) + int(wor_cost) + int(tr_co) + int(se_cost)))


def fi(fild,yer):
   cur.execute('select * from base_info where name_fild=%s and qtr=1 and year(date_year)=%s', (fild,yer))
   base = cur.fetchall()
   tr_cost = 0
   lab_sal = 0
   for i in base:
       lab_sal = i[3]
       tr_cost = i[4]
   # print(lab_sal)
   # print(tr_cost)
   fild = fild
   cur.execute('select * from seed where field=%s and month(date_seed)<=6 and year(date_seed)=%s', (fild,yer))
   seed = cur.fetchall()

   cur.execute('select * from work where fild_name=%s and month(wr_date)<=6 and year(wr_date)=%s', (fild,yer))
   work = cur.fetchall()

   cur.execute('select * from trac_work where fild_name=%s and month(tr_date)<=6 and year(tr_date)=%s', (fild,yer))
   tract = cur.fetchall()


   tr_co = 0
   tr_time = ""  # time calculate
   for i in tract:
       print('Your Fild Name  => ', end=" ")
       print(i[0])  # fild name
       print('Date Of Tractor Work  => ', end=" ")
       print(i[1])  # tractor date
       print('Time Taken By Tractor Work  => ', end=" ")
       print(i[2])  # tractor time
       tr_time = i[2]
       print('Number Of Days Work On Tractor  => ', end=" ")
       print(i[3])  # tractor days
       print("That's All For Land Preparation !!!! :) ")

   tr_time = str(tr_time).split(':')
   tr_co = int(tr_time[0]) * tr_cost
   print(tr_cost)
   se_cost = 0
   for i in seed:
       # print('Your Fild Name  => ', end=" ")
       # print(i[0])  # fild name
       print('Seed Name  => ', end=" ")
       print(i[1])  # seed name
       print('Your Crop Name  => ', end=" ")
       print(i[2])  # crop name
       print('Quantity of Seed Used  => ', end=" ")
       print(i[3])  # quantity of product
       print('Total Price  Of The Seed => ', end=" ")
       print(i[4] * i[3])  # price of product by Kg
       se_cost = i[4] * i[3]
   wor_cost = 0
   for i in work:
       print('Work  => ', end=" ")
       print(i[1])  # work
       print('Work Date  => ', end=" ")
       print(i[2])  # work date
       print('Number Of Workers   => ', end=" ")
       print(i[3])  # number of worker
       wor_cost = i[3]
   wor_cost = wor_cost * lab_sal
   hv = 0
   wor = 0
   cur.execute('select * from harvest where field=%s and month(harv_date)<=6 and year(harv_date)=%s', (fild,yer))
   harv = cur.fetchall()
   print(harv)
   en=0
   for i in harv:
       print('Number Of Workers Involved n Harvesting  => ', end=" ")
       print(i[2])  # number of workers
       wor = i[2]
       print('Heavy Work => ', end=" ")
       print(i[3])  # total  heavy work
       hv = i[3]
       print('Harvesting Date  => ', end=" ")
       print(i[4])  # harvest date
       print('Total Earnings  => ', end=" ")
       print(i[5])  # total profit
       en=i[5]
   print('Total Profit')
   print(int(en)-((int(hv)+int(wor)+int(wor_cost)+int(tr_co)+int(se_cost))))#


def se(fild,yer):
   cur.execute('select * from base_info where name_fild=%s and qtr=2 and year(date_year)=%s', (fild,yer))
   base = cur.fetchall()
   tr_cost = 0
   lab_sal = 0
   for i in base:
       lab_sal = i[3]
       tr_cost = i[4]
   # print(lab_sal)
   # print(tr_cost)
   fild = fild
   cur.execute('select * from seed where field=%s and month(date_seed)>6 and year(date_seed)=%s', (fild,yer))
   seed = cur.fetchall()

   cur.execute('select * from work where fild_name=%s and month(wr_date)>6 and year(wr_date)=%s', (fild,yer))
   work = cur.fetchall()

   cur.execute('select * from trac_work where fild_name=%s and month(tr_date)>6 and year(tr_date)=%s', (fild,yer))
   tract = cur.fetchall()

   tr_co = 0
   tr_time = ""  # time calculate
   for i in tract:
       print('Your Fild Name  => ', end=" ")
       print(i[0])  # fild name
       print('Date Of Tractor Work  => ', end=" ")
       print(i[1])  # tractor date
       print('Time Taken By Tractor Work  => ', end=" ")
       print(i[2])  # tractor time
       tr_time = i[2]
       print('Number Of Days Work On Tractor  => ', end=" ")
       print(i[3])  # tractor days
       print("That's All For Land Preparation !!!! :) ")

   tr_time = str(tr_time).split(':')
   tr_co = int(tr_time[0]) * tr_cost
   print(tr_cost)
   se_cost = 0
   for i in seed:
       # print('Your Fild Name  => ', end=" ")
       # print(i[0])  # fild name
       print('Seed Name  => ', end=" ")
       print(i[1])  # seed name
       print('Your Crop Name  => ', end=" ")
       print(i[2])  # crop name
       print('Quantity of Seed Used  => ', end=" ")
       print(i[3])  # quantity of product
       print('Total Price  Of The Seed => ', end=" ")
       print(i[4] * i[3])  # price of product by Kg
       se_cost = i[4] * i[3]
   wor_cost = 0
   for i in work:
       print('Work  => ', end=" ")
       print(i[1])  # work
       print('Work Date  => ', end=" ")
       print(i[2])  # work date
       print('Number Of Workers   => ', end=" ")
       print(i[3])  # number of worker
       wor_cost = i[3]
   wor_cost = wor_cost * lab_sal
   hv = 0
   wor = 0
   cur.execute('select * from harvest where field=%s and month(harv_date)>6 and year(harv_date)=%s', (fild,yer))
   harv = cur.fetchall()
   print(harv)
   en = 0
   for i in harv:
       print('Number Of Workers Involved n Harvesting  => ', end=" ")
       print(i[2])  # number of workers
       wor = i[2]
       print('Heavy Work => ', end=" ")
       print(i[3])  # total  heavy work
       hv = i[3]
       print('Harvesting Date  => ', end=" ")
       print(i[4])  # harvest date
       print('Total Earnings  => ', end=" ")
       print(i[5])  # total profit
       en = i[5]
   print('Total Profit')
   print(int(en) - (int(hv) + int(wor) + int(wor_cost) + int(tr_co) + int(se_cost)))

if rol == 0:
   create_account()

elif rol == 1:
   ow_check()

elif rol == 2:
   ma_check()
else:
   print('Enter The Required Input Alone')
   print('Restart the portal application')

myConn.commit()
cur.close()
