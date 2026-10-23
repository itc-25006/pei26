a = 2
a_list = []

for i in range(6):          #　空のリストに繰り返し処理で要素を追加
    a_list.append(a)
    a *= 2                  #　aの値を2倍にする
print(a_list)

fruits = ['マンゴー', 'パイナップル', 'バンシルー']
#　酸味と甘みのバランスが丁度いいから
favorite = fruits.pop(1) #　リストの2番目の要素を削除して変数に代入
print(favorite)
print(fruits)

days = ['月', '月', '火', '水', '木', '金', '金']
days.remove('月')  # 重複している「月」を1つ削除
days.remove('金')  # 重複している「金」を1つ削除
days.insert(0, '日')  # リストの先頭に「日」を追加
days.insert(6, '土')  # 7番目の位置に「土」を追加
print(days)


