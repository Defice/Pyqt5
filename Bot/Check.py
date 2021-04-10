# dv1= 1
# dv2 = 2
# dv3 = 3
# DV=[]
# for i in range(1,4):
#     DV.append(r'dv'+ str(i))
#     print(DV)
# def aga():
#     return 1
# i = aga()
# print(i)
# a=[['1', '1', '1', '1', '1', '', '', '', '', '', '', '', '', '', '', '', '', '', '']]
# print(len(a[0]))
NAME={'PEN':1,'KN1':2,'KN2':3,'BEN':4,'CN':5,'NZK':6,'NPE':7,"D":8,'DV':9,
   'VGD':10,'MV':11, 'NNCM':12, 'NPT':13}

a= [['PEN', '1111', '1', '11', '1', '1', '1', '1', '1', '1', '1', '1', '11', '1', '1', '1', '1', '1', '0'], ['KN1', '1111', '1', '11', '', '', '', '', '', '', '', '', '', '', '', '', '', '0', '1'],['PEN', '1111', '1', '11', '', '', '', '', '', '', '', '', '', '', '', '', '', '1', '0']]
C1=[]
def do_RST():
   C1 = []
   C2 = []
   C3 = []
   line_1 = '123                                             24.10.900'
   line_2 = f'10.0    10    9'
   line_3 = f'  25. 20.0  6.3  .0010.50  .0015.00 81.50'
   line_4 = f'  25. 20.0  6.3  .0010.50  .0015.00 81.50'
   line_5 = f'  32.230.0  6.3  .0011.50  .0014.00101.20            1\n'
   line_6 = f'1C      .2                                                  '
   for i in a:
      if i[17] != 0:
         if (i[0] in list(NAME.keys())):
            C1.append([f'  {i[0]}         {NAME.setdefault(i[0])}          {i[2]} {i[15]}{i[10]}  {i[11]} {i[13]}  {i[12]} {i[14]}'])
      elif i[18] != 0:
         if (i[0] in list(NAME.keys())):
            C2.append([f'  {i[0]}         {NAME.setdefault(i[0])}          {i[2]} {i[15]}{i[10]}  {i[11]} {i[13]}  {i[12]} {i[14]}'])
   line_7 = '2C      .2                                                  '
   line_8 = '3C        .2                                                                \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
   line_9 = '4C        .2                                                                \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
   for i in a:
      for j in range(0,len(list(NAME.keys()))):
         if list(NAME.keys())[j] == i[0]:
            C3.append(
               [f'  {NAME.setdefault(i[0])} {i[1]}{i[5]} {i[6]}   {i[4]} {i[8]}  {i[7]}  {i[9]}  {i[16]}     '])
   if len(C3) <= 20:
      for i in range(0, 20 - len(C3)):
         C3.append([])
   line_10 = ''
   new_line = [line_1, line_2, line_3, line_4, line_5, line_6, C1, line_7, C2, line_8, line_9, C3, line_10]
   if len(C1) <= 20:
      for i in range(0,len(new_line)):
         if C1 == new_line[i]:
            for j in range(0, 22 - len(C1)):
               new_line.insert(i+j+1,'')
   if len(C2) <= 20:
      for i in range(0,len(new_line)):
         if C2 == new_line[i]:
            for j in range(0, 22 - len(C2)):
               new_line.insert(i+j+1,'')
   if len(C3) <= 20:
      for i in range(0,len(new_line)):
         if C3 == new_line[i]:
            for j in range(0, 22 - len(C3)):
               new_line.insert(i+j+1,'')
   return new_line
print(do_RST())




a = do_RST()
print(a)
f = open('new.txt','w')
for index in a:
   f.write(str(index)+'\n')
f.close()