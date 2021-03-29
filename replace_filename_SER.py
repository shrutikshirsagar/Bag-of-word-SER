import os

paths = (os.path.join(root, filename)
        for root, _, filenames in os.walk('/home/amrgaballah/Desktop/labels/')
        for filename in filenames)
num1 = ['01', '02',  '03',  '04',  '05',  '06',  '07',  '08',  '09', '10', '11', '12', '13', '14']
num2 = ['35',  '36', '37',  '38', '39',  '40',  '41',  '42',  '43', '44', '45', '46', '47', '48']

for path in paths:
    for i, j in zip(num1, num2):
        newname = path.replace('Devel_DE_'+i , 'Train_DE_'+j)
        if newname != path:
            os.rename(path, newname)
