import g_PersonClass as pc

reece = pc.Customer("Reece Modisette", 'Somewhere on 14th and Wood',
                    '1234567890', '892543392')
payton = pc.Person("Payton Campbell", "1423 James Ave", "7134924041")

print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
print('--------Person Information---------')
print(f'Name:   ', payton.get_person())
print(f'Address:', payton.get_address())
print(f'Phone #:', payton.get_telephone())
print()
print('-------Customer Information--------')
print(f'Name:   ', reece.get_person())
print(f'Address:', reece.get_address())
print(f'Phone #:', reece.get_telephone())
print(f'Customer #:', reece.get_cust_num())
print()
print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
