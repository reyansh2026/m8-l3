import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
print("="*60)
print("                   Social Media Trends")
print("="*60)
days=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
insta=[12400,15300,13800,16200,18900,24000,25000]
yt=[8900,9200,78000,92200,76220,10670,27322,]
twitter=[7722,8392,7382,12833,17288,17233,11002]
tt=[19010,12880,14092,16028,18028,22782,15266]
plt.plot(days,insta,marker="o",linewidth=3,color="purple")
plt.plot(days,yt,marker='o',linewidth=3,color='red')
plt.plot(days,twitter,marker='o',linewidth=3,color="blue")
plt.plot(days,tt,marker='o',linewidth=3,color='black')
plt.title("Social Media Trends")
plt.xlabel("Days")
plt.ylabel("Trends")
plt.show()
plt.bar(days,insta,color='purple')
plt.bar(days,yt,color="red")
plt.bar(days,twitter,color="blue")
plt.bar(days,tt,color="black")
plt.show()