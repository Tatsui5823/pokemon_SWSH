import urllib.request as httplib  # 3.x
import ssl
import urllib.request
import matplotlib.pyplot as plt
import xlrd
import xlwt
import csv
import numpy as np
import pymysql as MySQLdb             #  pip install MySQLdb

db = MySQLdb.connect(host="127.0.0.1", user="admin", passwd="admin", db="mydatabase")
#db = MySQLdb.connect(host="172.19.107.140", user="powenko", passwd="powenko", db="mydatabase")
cursor = db.cursor()
id = []                  #ID
name1 = []               #英文名
name2 = []               #中文名
HP = []                  #血量
Attack = []              #攻擊
Defense = []             #防禦
Sp_Atk = []              #特攻
Sp_Def = []              #特防
Speed = []               #速度
sum = []                 #種族值
type1 = []               #屬性1
type2 = []               #屬性2

#讀取資料庫全部資料
sql="SELECT * FROM `project`"
cursor.execute(sql)
result = cursor.fetchall()
print(result)

#資料庫資料陣列化
for pokemonlist in result:
    id.append(pokemonlist[0])
    name1.append(pokemonlist[1])
    name2.append(pokemonlist[2])
    HP.append(int(pokemonlist[3]))
    Attack.append(int(pokemonlist[4]))
    Defense.append(int(pokemonlist[5]))
    Sp_Atk.append(int(pokemonlist[6]))
    Sp_Def.append(int(pokemonlist[7]))
    Speed.append(int(pokemonlist[8]))
    sum.append(int(pokemonlist[9]))
    type1.append(pokemonlist[10])
    type2.append(pokemonlist[11])

print(name1)


#製作figure 散佈圖
fig = plt.figure()

#種族值對ID
#設定axes位置
ax = fig.add_subplot(2, 1, 1)
#設定散佈圖的顏色，大小等等
ax.scatter(id, sum, s=1, alpha=1, linewidths=2.5, c='green', edgecolors='green')
plt.xlabel("ID")
plt.ylabel("sum")
for i in range(len(result)):
    ax.text(id[i], sum[i], id[i], fontsize=8, color = "red", style = 'oblique', weight = "light", verticalalignment='center', horizontalalignment='right',rotation=0) #加標籤

#攻擊防禦關係圖
#設定axes位置
ax = fig.add_subplot(2, 4, 5)
#設定散佈圖的顏色，大小等等
ax.scatter(Attack, Defense, s=1, alpha=1, linewidths=2.5, c='#AAAFFF', edgecolors='blue')
ax.set_title("Atk & Def")
plt.xlabel("Attack")
plt.ylabel("Defense")
for i in range(len(result)):
    ax.text(Attack[i], Defense[i], id[i], fontsize=8, color = "r", style = 'oblique', weight = "light", verticalalignment='center', horizontalalignment='right',rotation=0) #加標籤

#特攻特防關係圖
#設定axes位置
ax = fig.add_subplot(2, 4, 6)
#設定散佈圖的顏色，大小等等
ax.scatter(Sp_Atk, Sp_Def, s=1, alpha=1, linewidths=2.5, c='#AAAFFF', edgecolors='blue')
ax.set_title("Sp_Atk & Sp_Def")
plt.xlabel("Sp_Atk")
plt.ylabel("Sp_Def")
for i in range(len(result)):
    ax.text(Sp_Atk[i], Sp_Def[i], id[i], fontsize=8, color = "r", style = 'oblique', weight = "light", verticalalignment='center', horizontalalignment='right',rotation=0) #加標籤

#速度ID關係圖
#設定axes位置
ax = fig.add_subplot(2, 4, 7)
#設定散佈圖的顏色，大小等等
ax.scatter(id,Speed , s=1, alpha=1, linewidths=2.5, c='#AAAFFF', edgecolors='blue')
plt.xlabel("ID")
plt.ylabel("Speed")
ax.set_title("ID_Speed")
for i in range(len(result)):
    ax.text(id[i],Speed[i] , id[i], fontsize=8, color = "r", style = 'oblique', weight = "light", verticalalignment='center', horizontalalignment='right',rotation=0) #加標籤

#血量ID關係圖
#設定axes位置
ax = fig.add_subplot(2, 4, 8)
#設定散佈圖的顏色，大小等等
ax.scatter(id, HP, s=1, alpha=1, linewidths=2.5, c='#AAAFFF', edgecolors='blue')
ax.set_title("HP")
plt.xlabel("ID")
plt.ylabel("ID_HP")
for i in range(len(result)):
    ax.text(id[i],HP[i] , id[i], fontsize=8, color = "r", style = 'oblique', weight = "light", verticalalignment='center', horizontalalignment='right',rotation=0) #加標籤


plt.show()
