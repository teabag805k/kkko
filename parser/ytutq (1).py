from sklearn.feature_extraction.text import TfidfVectorizer

# Пример текста
text = [
    "Это пример текста для TF-IDF преобразования",
    "TF-IDF - это метод векторизации текста",
    "TF-IDF позволяет оценить важность слов в тексте"
]

# Создание объекта TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer()

# Преобразование текста в TF-IDF векторное представление
tfidf_matrix = tfidf_vectorizer.fit_transform(text)

# Вывод TF-IDF векторного представления
print(tfidf_matrix.toarray())