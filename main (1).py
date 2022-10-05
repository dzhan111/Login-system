
choice = input("Do you want to login with existing user or save a new new user/pass? \n n for new , l for login: ")



if(choice == 'n'):

  newString = input("\nnew Username: ")+':'+input("new Password: ")

  open('start.txt', 'a').write(newString+ '\n')
  open('start.txt', 'a').close()

  print('\n ***new user successfully stored***')




elif(choice == 'l'):
  username = input('User: ')
  password = input('pass: ')

  newString = username+':'+password
  
  f = open('start.txt','r+')
  files = f.read()
    
  if newString in files:
    print('successfully logged in!')
  else:
    print('\nuser not found. Try entering your password again')

  f.close()


