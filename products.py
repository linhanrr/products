import os # operting system 
#讀取檔案
def read_file(filename):
    with open(filename, 'r', encoding = 'utf-8') as f: #編碼問題在讀取跟寫入時都會出現，所以要統一
        products = []
        for line in f:
            if '商品, 價格' in line:
                continue #跳到下一個迴圈
            name, price = line.strip().split(',') #每一行去掉換行符號後，用split在,處分隔，並分別存入name price
            products.append([name, price])
    print(products)
    return products

#讓使用者輸入
def user_input(products):
    while True:
        name = input('請輸入商品名稱: ')
        if name == 'q':
            break
        price = input('請輸入商品價格: ')
        price = int(price)
        products.append([name, price])
    return products

#印出所有購買紀錄
def print_products(products):
    for p in products:
        print(p[0], '的價格是', p[1])

#寫入檔案
def write_file(filename, products):
    with open(filename, 'w', encoding = 'utf-8') as f:
        f.write('商品, 價格\n')
        for p in products:
            f.write(p[0] + ',' + str(p[1]) + '\n')  #comma is used for differentiation

def main():
    filename = 'products.csv'
    if os.path.isfile(filename):
        print('yeah 找到檔案了')
        products = read_file(filename)
    else: 
        print('找不到檔案qq')
    products = user_input(products)
    print_products(products)
    write_file('products.csv', products)

main()
