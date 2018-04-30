


try:
    f = open('text.txt')
    # var = bad_var
    # if f.name == 'texst.txt':
    #     raise Exception
except OSError as e:
    print('Error!')
except Exception as e:
    # print('Something went wrong')
    print(e)
else:
   print(f.read())
   f.close
finally:
    print('hihi')
    