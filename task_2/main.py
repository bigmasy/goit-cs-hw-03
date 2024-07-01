from pymongo import MongoClient
from bson.objectid import ObjectId

# Підключення до MongoDB Atlas
client = MongoClient('mongodb+srv://test:test@cluster0.7fvb0f9.mongodb.net/')

db = client['cats_db']

cats_collection = db['cats']

# додавання нового кота
def create_cat(name, age, features):
    cat = {
        "name": name,
        "age": age,
        "features": features
    }
    cats_collection.insert_one(cat)
    print(f"Кiт {name} успішно доданий!")

# виведення всіх записів із колекції
def read_all_cats():
    cats = cats_collection.find()
    for cat in cats:
        print(cat)

# виведення інформації про кота за ім'ям
def read_cat_by_name(name):
    cat = cats_collection.find_one({"name": name})
    if cat:
        print(cat)
    else:
        print(f"Кота з ім'ям {name} не знайдено.")

# оновлення віку кота за ім'ям
def update_cat_age(name, new_age):
    result = cats_collection.update_one({"name": name}, {"$set": {"age": new_age}})
    if result.matched_count > 0:
        print(f"Вік кота {name} успішно оновлений до {new_age}.")
    else:
        print(f"Кота з ім'ям {name} не знайдено.")

# додавання нової характеристики до списку features кота за ім'ям
def add_feature_to_cat(name, feature):
    result = cats_collection.update_one({"name": name}, {"$push": {"features": feature}})
    if result.matched_count > 0:
        print(f"Характеристика '{feature}' успішно додана коту {name}.")
    else:
        print(f"Кота з ім'ям {name} не знайдено.")

# видалення запису з колекції за ім'ям кота
def delete_cat_by_name(name):
    result = cats_collection.delete_one({"name": name})
    if result.deleted_count > 0:
        print(f"Кота з ім'ям {name} успішно видалено.")
    else:
        print(f"Кота з ім'ям {name} не знайдено.")

# видалення всіх записів із колекції
def delete_all_cats():
    result = cats_collection.delete_many({})
    print(f"Всі коти успішно видалені. Видалено записів: {result.deleted_count}")

# демонстрація роботи
def main():
    while True:
        print("\nВиберіть дію:")
        print("1. Додати кота")
        print("2. Показати всіх котів")
        print("3. Показати кота за ім'ям")
        print("4. Оновити вік кота")
        print("5. Додати характеристику коту")
        print("6. Видалити кота за ім'ям")
        print("7. Видалити всіх котів")
        print("8. Вийти")

        choice = input("Введіть номер дії: ")

        if choice == '1':
            name = input("Введіть ім'я кота: ")
            age = int(input("Введіть вік кота: "))
            features = input("Введіть характеристики кота (через кому): ").split(',')
            create_cat(name, age, features)
        elif choice == '2':
            read_all_cats()
        elif choice == '3':
            name = input("Введіть ім'я кота: ")
            read_cat_by_name(name)
        elif choice == '4':
            name = input("Введіть ім'я кота: ")
            new_age = int(input("Введіть новий вік кота: "))
            update_cat_age(name, new_age)
        elif choice == '5':
            name = input("Введіть ім'я кота: ")
            feature = input("Введіть нову характеристику: ")
            add_feature_to_cat(name, feature)
        elif choice == '6':
            name = input("Введіть ім'я кота: ")
            delete_cat_by_name(name)
        elif choice == '7':
            delete_all_cats()
        elif choice == '8':
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
