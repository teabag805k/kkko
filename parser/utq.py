from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Предположим, что у нас есть метки класса для каждого текста
labels = [1, 0, 1]

# Разделение данных на обучающий и тестовый наборы
X_train, X_test, y_train, y_test = train_test_split(tfidf_matrix, labels, test_size=0.2, random_state=42)

# Обучение модели на обучающем наборе
model = SVC(kernel='linear')
model.fit(X_train, y_train)

# Предсказание меток класса на тестовом наборе
y_pred = model.predict(X_test)

# Оценка точности модели
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)