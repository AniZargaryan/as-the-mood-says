# as-the-mood-says

A console-based tool that helps you choose a movie depending on your **current mood** (and optionally by **genre**).
The app is designed for users who want a quick, personalized film recommendation without endless scrolling through catalogs.

## Data
No external datasets are used. All movie records are stored in **movies_data.py**, so no internet connection or API required.


## Functionality
- Display a list of available **moods** with emoji.
- Select a **mood** and optionally narrow by **genre**.
- Randomly suggest matching films.
- View all movies stored in the database.
- Return to the main menu at any time.
- Fully console-based and runs offline.


## Requirements / Dependencies
- Python **3.10+**
- No external libraries required (uses only Python standard library).  
- Dependencies file: [`requirements.txt`](./requirements.txt)


## Installation

```bash
# 1) Clone the repository
git clone https://github.com/AniZargaryan/as-the-mood-says.git
cd as-the-mood-says

# 2) Create and activate a virtual environment
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# 3) Install dependencies
python -m pip install -r requirements.txt
```

## Run the program
```bash
python main.py
```

### Example of a user scenario:

1. **Run the program.**
2. A list of 3 options how to get movie recommendation appears. **Select 1 - “Подобрать фильм под настроение”.**
3. A list of mood options appears. **Select 5 - “в философских размышлениях 🤔”.**
4. The question appears: “Хотите уточнить жанр? (да/1 или нет/2)”. **Enter “да”.**
5. A list of available movie genres appears according to the selected mood. **Select “3” - “приключения”.**
6. The number of films found and one randomly suggested film appear. **Select “0” - “вернуться в главное меню”.**
7. Return to main menu. **Select “0” - “Выйти из программы”.**
8. Exiting the program. The following message appears “👋 До свидания! ◝(ᵔᗜᵔ)◜”.

### >> How it looks in the consol:

```bash
PS C:\Users\User\as-the-mood-says> python main.py

────────────────────────────────────────────────────────────
🎬 ДОБРО ПОЖАЛОВАТЬ В ПРОГРАММУ ПОДБОРА ФИЛЬМОВ! ༄˖°.🍂.ೃ࿔*
────────────────────────────────────────────────────────────
1. Подобрать фильм под настроение
2. Показать все фильмы
0. Выйти из программы
────────────────────────────────────────────────────────────
Ваш выбор: 1

💭 Какое у вас сейчас настроение?
1. веселый 😄
2. что-то для уютного вечера 😊
3. нужно вдохновение ✨
4. грустный, хочу поднять настроение 🌈
5. в философских размышлениях 🤔
6. хочется чего-то эпичного 🌌
7. слишком хорошо живу, давай грустный фильм 💔
8. верю в чудеса 🕊️
9. я сегодня подозреваю всех 🕵️‍♂️
10. хочу фильм, после которого не смогу уснуть 🤯
11. хочется напряжения, тайн 👁️
12. скучно, хочется приключений и сверхъестественного 🌠
13. устаю от всего, хочу улететь куда-то далеко 🪐
14. в любви 💖
15. спортивное 💪
0. Назад

Выберите номер: 5
Хотите уточнить жанр? (да/1 или нет/2): да

🎬 Доступные жанры:
1. фантастика
2. драма
3. приключения
4. криминал
5. фэнтези
0. Пропустить

Выберите жанр (или 0 для пропуска): 3

✅ Найдено фильмов: 1. Вот один из них:

────────────────────────────────────────────────────────────
🎬 Интерстеллар (2014)
📌 Жанры: фантастика, драма, приключения
📝 Описание: Когда засуха, пыльные бури и вымирание растений приводят человечество к продовольственному кризису, коллектив исследователей и учёных отправляется сквозь червоточину (которая предположительно соединяет области пространства-времени через большое расстояние) в путешествие, чтобы превзойти прежние ограничения для космических путешествий человека и найти планету с подходящими для человечества условиями.
────────────────────────────────────────────────────────────

Нажмите Enter —> показать другой фильм по тем же критериям
Введите 0 —> вернуться в главное меню
Ваш выбор: 0

────────────────────────────────────────────────────────────
🎬 ДОБРО ПОЖАЛОВАТЬ В ПРОГРАММУ ПОДБОРА ФИЛЬМОВ! ༄˖°.🍂.ೃ࿔*
────────────────────────────────────────────────────────────
1. Подобрать фильм под настроение
2. Показать все фильмы
0. Выйти из программы
────────────────────────────────────────────────────────────
Ваш выбор: 0

👋 До свидания! ◝(ᵔᗜᵔ)◜
```

## Project structure

```bash
as-the-mood-says
├─.gitignore # excludes temporary and system files.
├─LICENSE # license file (MIT License).
├─main.py # main file with menu and filtering logic.
├─movies_data.py # internal database with movie info (titles, moods, genres, descriptions).
├─README.md # documentation (overview, setup, usage and etc).
├─requirements.txt # requirements and dependencies file (empty; only Python standard library (**random**) is used).
```

## License / author:

MIT License

Copyright (c) 2025 Ani

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


# Enjoy using the program!