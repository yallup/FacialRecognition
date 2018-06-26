from multiprocessing import Pool

def setValues():
    yes = True
    no = False
    return yes,no

def count():
    for i  in  [1,2,3,4,5]:
        print(i)

pool = Pool(processes=2)

res = pool.apply_async(count)

yes = pool.apply_async(setValues)

print(yes.get())
print(type(yes.get()))
print('finished')
