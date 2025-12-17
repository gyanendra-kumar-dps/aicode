from sklearn.datasets import fetch_openml
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt

data=fetch_openml('mnist_784')
dt=data['data']/255
lb=data['target'].astype(int)

dt_train,dt_test,lb_train,lb_test=train_test_split(dt,lb,test_size=0.2,random_state=69)

model=LogisticRegression(max_iter=5000)
model.fit(dt_train,lb_train)
prediction=model.predict(dt_test)
print()
acc=f"{int(metrics.accuracy_score(lb_test,prediction))*100}%"

for i in range(5):
  plt.imshow(dt_test.iloc[i].values.reshape(28,28),cmap=plt.cm.binary)
  plt.title(f'Prediction:{prediction[i]} Actual:{lb_test.iloc[i]}')
  plt.show()
