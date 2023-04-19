import g_PersonClass as pc

reece = pc.Customer("Reece Modisette", '1929 S 14th St.',
                    '936-635-6523', '892543392')
payton = pc.Person("Payton Campbell", "1423 James Ave", "713-492-4041")

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
