import random
from movies_data import MOVIES_DATA


def get_all_moods():
    
    all_moods = []
    for movie in MOVIES_DATA:
        for mood in movie["mood"]:
            if mood not in all_moods:
                all_moods.append(mood)
    return all_moods


def choose_mood():
    
    moods = get_all_moods()
    print("\n💭 Какое у вас сейчас настроение?")

    for i in range(len(moods)):
        print(f"{i + 1}. {moods[i]}")
    print("0. Назад")

    while True:
        try:
            choice = input("\nВыберите номер: ").strip()
            if choice == "0":
                return None
            index = int(choice) - 1
            if 0 <= index < len(moods):
                return moods[index]
            else:
                print(f"❌ Введите число от 1 до {len(moods)}")
        except ValueError:
            print(f"❌ Введите число от 1 до {len(moods)}")
        except KeyboardInterrupt:
            print("\n👋 До свидания! ◝(ᵔᗜᵔ)◜ ")
            exit(0)


def get_genres_from_movies(movies):

    genres = []
    for movie in movies:
        for g in movie["genre"]:
            if g not in genres:
                genres.append(g)
    return genres


def choose_genre(genres):
    
    print("\n🎬 Доступные жанры:")
    for i in range(len(genres)):
        print(f"{i + 1}. {genres[i]}")
    print("0. Пропустить")

    while True:
        try:
            choice = input("\nВыберите жанр (или 0 для пропуска): ").strip()
            if choice == "0":
                return None
            index = int(choice) - 1
            if 0 <= index < len(genres):
                return genres[index]
            else:
                print(f"❌ Введите число от 1 до {len(genres)}")
        except ValueError:
            print(f"❌ Введите число от 1 до {len(genres)}")
        except KeyboardInterrupt:
            print("\n👋 До свидания! ◝(ᵔᗜᵔ)◜ ")
            exit(0)


def show_menu():
    
    print("\n" + "─" * 60)
    print("🎬 ДОБРО ПОЖАЛОВАТЬ В ПРОГРАММУ ПОДБОРА ФИЛЬМОВ! ༄˖°.🍂.ೃ࿔*")
    print("─" * 60)
    print("1. Подобрать фильм под настроение")
    print("2. Показать все фильмы")
    print("0. Выйти из программы")
    print("─" * 60)


def get_yes_no():
    
    while True:
        answer = input("Хотите уточнить жанр? (да/1 или нет/2): ").strip().lower()
        if answer in ['да', '1']:
            return True
        elif answer in ['нет', '2']:
            return False
        else:
            print("❌ Введите 'да'/'1' или 'нет'/'2'.")


def show_movie(movie):
    
    print("\n" + "─" * 60)
    print(f"🎬 {movie['title']} ({movie['year']})")
    print(f"📌 Жанры: {', '.join(movie['genre'])}")
    print(f"📝 Описание: {movie['description']}")
    print("─" * 60)


def show_random_from_list(movies):
    if not movies:
        print("❌ Ничего не найдено.")
        input("\nНажмите Enter, чтобы вернуться в меню...")
        return

    total = len(movies)
    used = set()

    while True:
        if len(used) == total:
            used.clear()

        available = []
        for i in range(total):
            if i not in used:
                available.append(i)

        index = random.choice(available)
        used.add(index)
        movie = movies[index]

        print(f"\n✅ Найдено фильмов: {total}. Вот один из них:")
        show_movie(movie)
        print("\nНажмите Enter —> показать другой фильм по тем же критериям")
        print("Введите 0 —> вернуться в главное меню")
        user_input = input("Ваш выбор: ").strip()
        if user_input == "0":
            break


def show_all_movies(movies):
    
    if not movies:
        print("❌ Нет фильмов для отображения.")
    else:
        print(f"\n✅ Всего фильмов: {len(movies)}\n")
        for movie in movies:
            show_movie(movie)
    input("\nНажмите Enter, чтобы вернуться в меню...")


def filter_movies_by_mood_and_genre(mood, genre):
    
    results = []
    for movie in MOVIES_DATA:
        if mood in movie['mood']:
            results.append(movie)
    
    
    if genre is not None:
        filtered_results = []
        for movie in results:
            if genre in movie['genre']:
                filtered_results.append(movie)
        results = filtered_results
    
    return results


def main():
    
    while True:
        show_menu()
        choice = input("Ваш выбор: ").strip()

        if choice == "0":
            print("\n👋 До свидания! ◝(ᵔᗜᵔ)◜ ")
            break
        
        elif choice == "1":
            mood = choose_mood()
            if mood is None:
                continue
            
            movies_by_mood = []
            for movie in MOVIES_DATA:
                if mood in movie['mood']:
                    movies_by_mood.append(movie)
            
            use_genre = get_yes_no()
            selected_genre = None
            
            if use_genre:
                available_genres = get_genres_from_movies(movies_by_mood)
                if available_genres:
                    selected_genre = choose_genre(available_genres)
                else:
                    print("❌ Нет доступных жанров для выбранных параметров.")

            final_movies = filter_movies_by_mood_and_genre(mood, selected_genre)
            show_random_from_list(final_movies)
        
        elif choice == "2":
            show_all_movies(MOVIES_DATA)

        else:
            print("❌ Неверный выбор. Попробуйте снова.")
            input("\nНажмите Enter, чтобы продолжить...")


if __name__ == "__main__":
    main()