import pickle

my_list = [123, 3.14, '小甲鱼', ['another list']]
pickle_file = open('my_list.pkl', 'wb')
pickle.dump(my_list, pickle_file)  # 把文件以二进制形式保存到pickle_file
pickle_file.close()
pickle_file = open('my_list.pkl', 'rb')
my_list2 = pickle.load(pickle_file)  # 把二进制文件读出来
print(my_list2)

