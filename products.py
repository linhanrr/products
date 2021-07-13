import os # operting system 

#讀取檔案
products = []
if os.path.isfile('products.csv'): #檢查檔案在不在，運用os模組裡的path中isfile涵式的功能
    print('yeah 找到檔案了')
    with open('products.csv', 'r', encoding = 'utf-8') as f: #編碼問題在讀取跟寫入時都會出現，所以要統一
        for line in f:
            if '商品, 價格' in line:
                continue #跳到下一個迴圈
            name, price = line.strip().split(',') #每一行去掉換行符號後，用split在,處分隔，並分別存入name price
            products.append([name, price])
    print(products)
else:
    print('找不到檔案qq')

#讓使用者輸入
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
        break
    price = input('請輸入商品價格: ')
    price = int(price)
    products.append([name, price])

#印出所有購買紀錄
for p in products:
    print(p[0], '的價格是', p[1])

#寫入檔案
with open('products.csv', 'w', encoding = 'utf-8') as f:
    f.write('商品, 價格\n')
    for p in products:
        f.write(p[0] + ',' + str(price) + '\n')  #comma is used for differentiation