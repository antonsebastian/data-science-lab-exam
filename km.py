import matplotlib.pyplot as plt
import pandas as pd

dataset=pd.read_csv("data.csv")
x=dataset.iloc[:,[2,3]].values
print(x)
from sklearn.cluster import KMeans
wcss_list=[]
for i in range(1,11):
    kmeans=KMeans(n_clusters=i,init='',random_state=42)
    wcss_list.append(kmeans.init)
plt.plot(range(1,11),wcss_list)
plt.title("elbow method")
plt.ylabel("dec")
plt.xlabel("inc")
plt.show()
kmeans=KMeans(n_clusters=6,init='k-means++',random_state=42)
y_predict=kmeans.fit_predict(x)
print(y_predict)
plt.scatter(x[y_predict == 0,0],x[y_predict == 0,1],s=100,c="red",label="cluster1")
plt.scatter(x[y_predict == 1,0],x[y_predict == 1,1],s=100,c="green",label="cluster2")
plt.scatter(x[y_predict == 2,0],x[y_predict == 2,1],s=100,c="blue",label="cluster3")
plt.scatter(x[y_predict == 3,0],x[y_predict == 3,1],s=100,c="yellow",label="cluster4")
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=300,c="black")
plt.legend()
plt.show()

