#從舊檔案讀取
products = []
with open('products.csv', 'r', encoding = 'utf-8') as f: #編碼問題在讀取跟寫入時都會出現，所以要統一
    for line in f:
        name, price = line.strip().split(',') #每一行去掉換行符號後，用split在,處分隔，並分別存入name price
        products.append([name, price])
print(products)

while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
        break
    price = input('請輸入商品價格: ')
    price = int(price)
    products.append([name, price])

for p in products:
    print(p[0], '的價格是', p[1])

with open('products.csv', 'w', encoding = 'utf-8') as f:
    f.write('商品, 價格\n')
    for p in products:
        f.write(p[0] + ',' + str(price) + '\n')  #comma is used for differentiation