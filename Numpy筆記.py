##陣列合併
#np.concatenate((a,b,c...),axis=0)
#np.array([1,2,3])[:,np.newaxis]    #新增維度

##陣列轉置，即[2,3]變[3,2]
#data.T
#data.ravel     ##把資料扁平，即把高維度資料變成一維陣列
#data.reshape()   ##把資料重塑成指定維度陣列

##正負值標記轉換
#np.sign(data)      ##把資料大於0變成1小於則變-1,可組合使用進行極端值過濾或轉換
#df[np.abs(data)>3]=np.sign(data)*3     ##把絕對值大於三的轉換成正負三