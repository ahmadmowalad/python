num_of_trise=0

while num_of_trise !=3:
            username=input('please insert username : ')

            password=input('please insert password : ')

            if username=='ahmad' and password=='123':
                   print('welcome')
                   num_of_trise=0
                   exit()

            else:
                  print('error')
                  num_of_trise+=1
                  print('you have ' + str(3-num_of_trise) + ' tries left')