import mysql.connector

myg = mysql.connector.connect(
    host="localhost",
    user="arjun", 
    password="arjunramesh",   
    database="mydatabase"  
)

gadget = myg.cursor()

gadget.execute('''
    CREATE TABLE IF NOT EXISTS gadgets (
        product_id INT(120) PRIMARY KEY,
        product_name VARCHAR(100),
        brand_name VARCHAR(100),
        price INT(10)
    )
''')


while True:
    print("\n1.Add Products\n2.Update Products\n3.Delete Poducts\n4.See Products\n5.Search\n6.exit")
    choice=int(input("enter your choice :"))
    if choice==1:
        product_id=int(input('enter the ID  :'))
        product_name=input('enter the product name :')
        brand_name=input("enter the brand name :")
        price=input("enter the price :")
        gadget.execute('insert into gadgets(product_id,product_name,brand_name,price) values(%s,%s,%s,%s)',
                       (product_id,product_name,brand_name,price))
        myg.commit()
    elif choice==2:
        product_id=int(input('enter the ID  :'))
        product_name=input('enter the new product name :')
        brand_name=input("enter the new brand name :")
        price=input("enter the new price :")
        gadget.execute('UPDATE gadgets SET product_name=%s, brand_name=%s, price=%s WHERE product_id=%s',
                       (product_name,brand_name,price,product_id))
        myg.commit()
    elif choice==3:
        product_id=int(input('enter the id to delete :'))
        gadget.execute("delete from gadgets where product_id=%s",(product_id,))
        myg.commit()
    elif choice==4:
        gadget.execute('SELECT * FROM gadgets')
        data = gadget.fetchall()
        print('{:<20}{:<30}{:<20}{:<20}'.format('product_id', 'product_name', 'brand_name', 'price'))
        print('-' * 80)
        for i in data:
            print("{:<20}{:<30}{:<20}{:<20}".format(i[0], i[1], i[2], i[3]))
    elif choice==5:
        product_id=int(input('enter the id to search :'))
        gadget.execute('SELECT * FROM gadgets WHERE product_id=%s', (product_id,))
        data = gadget.fetchall()
        print('{:<20}{:<20}{:<20}{:<20}'.format('product_id', 'product_name', 'brand_name', 'price'))
        print('-' * 80)
        if data:
            for i in data:
                print("{:<20}{:<30}{:<20}{:<20}".format(i[0], i[1], i[2], i[3]))
        else:
            print('id not available')
    elif choice==6:
        break