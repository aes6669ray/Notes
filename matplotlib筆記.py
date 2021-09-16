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
plt.subplots_adjust(wspace=0,hspace=0)  ##可以調整subplot的各個間隔

plt.annotate(lable, xy=(date))      ##給圖片新增文字標示,xy參數代表要放的座標位置(符號標誌),xytext則是label位置, //annotate比較複雜,可以配合影片一起操作