import matplotlib.pyplot as plt

plt.figure() #每設定一個figure就可以分別教出不同的圖片

plt.plot(x,y,color="red",linewidth=1,linestyle="--")

plt.xlim((1,2)) #x軸顯示1-2的圖片

new_ticks = np.linespace(1,5,1)
plt.xticks(new_ticks) #可以換x軸變成1-5且間隔為1
plt.yticks([1,2,3,4,5],
[r"$pretty\ bad$",r"$bad$",r"$normal$",r"$good$",r"$perfect$"]) #y軸1-5分別會顯示成下面的串列,r代表正則表達,$前後代表數學符號字體,\ (空白)代表空格

ax=plt.gca() #gca=get current axes
ax.spines['right'].set_visible(False) #看不到右邊的線
ax.spines['top'].set_visible(False)   #看不到上面的線
ax.spines["bottom"].set_position(("data",1)) #設定底下的線(x軸)在y=1的位置

plt.legend(handle=[],labels=[],loc="best")  #handle代表可以自己設定要的參數(丟進去的資料),best代表放在最好的位置,也可以統一放在upper right;botton left
