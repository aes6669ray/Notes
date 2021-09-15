#str代表是針對字串做運算的定義,replace代表把您好換成hello
#contain你好,代表找出有包含你好的資料
##print(data.str.replace("您好","hello"))
##print(data.str.contains("你好"))

#data.isna().sum() 找出data中的遺漏直

#my_list.append(object)             ##利用append增加list
#my_list.insert(position, object)   ##利用insert插入物件到特定位置
#my_list.remove(object)             ##利用remove刪除list
#list.pop(index)                    ##利用pop刪除指定索引項目,如果空格會是最後一個

#list_1 = ["object1", "object2", "object3"]
#list_2 = ["object4", "object5"]
#list_1.extend(list_2)              ##利用extend合併

#num.sort(reverse=True)             ##sort跟reverse
#print("Heal the World" in bad)     ##用in這個指令在list中找指定目標存在否/Heal the World是否在bad這個list中
#new_list = list.split()            ##如果括號中不放東西，就是以空白做切割
#new_list = list.split(',')         ##如果放逗號，就會把用逗號隔開的值所切割開


##整理數據表格用的
#pd.set_option('display.unicode.ambiguous_as_wide', True)
#pd.set_option('display.unicode.east_asian_width', True)
#pd.set_option('display.width', 0) # 设置打印宽度(**重要**)
#print(gg)

##整合資料的
#import glob
#all_data=glob.glob(".csv") 抓取所有資料包含csv並整合在all_data中可供抓取
#stocks=sorted(glob("*.csv"))
#pd.concat((pd.read_csv(file) for file in stocks), ignore_index=True) 

##縮減資料容量
#data["column_name"]=data.column_name.astype("category", categories=["good","very good","excellent"], ordered=True) 
#把object(通常是字體str)的資料型態轉成category,後半部代表讓電腦辨識分類,分類後可使用布林值判斷

##資料類別轉換
#bins=[18,25,35,60,100]
#group_names=["aa","bb","cc","dd"]
#pd.cut(data,bins,labels=group_name)  ##bins代表切割的類別,會放list 如上述18-25為一類,25-35為另一類...
#pd.qcut(data,4)    ##qcut代表按照百分比切割,後面數字代表切幾個組
#cut.codes          ##利用codes查詢各個data被轉換成的類別,會給成array的樣子

##資料整合
#df1.combine_first(df2) ##df1的資料為優先，把df2的資料補進df1的空缺裡
#pd.concat([df1,df2],axis=0,keys=["label"],join="inner")    ##join可以換outer變聯集
#pd.merge([df1,df2],axis=0,how="inner",on=["variable"])     ##依照Variable來merge
#pd.merge([df1,df2],left_on=["variable"],right_index=True)  ##row的方式merge資料