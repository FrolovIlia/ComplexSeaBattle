
- [x] Добавить в папку проекта миниатюры кораблей и остальные необходимые картинки.
- [ ] Подключить FastAPI.
  - [ ] Сформировать JSON для пересылки сообщений.

- [ ] Добавить базовые элементы поля (с относительным позиционированием)
    - [x] Игровое поле.
    - [x] Линии на поле.
    - [x] Иконки кораблей.
    - [ ] Индикаторы подбития.
        - [x] Добавить на поле.
        - [ ] Добавить зависимость состояния индикаторов от подбития кораблей.

    - [ ] Импортировать JSON
      - [ ] Разобраться, как брать нужные данные.
    
    - [x] Разобраться, как получать данные о клике мышкой.
    
    - [ ] Организовать конец игры.
        - [ ] Вывести сообщение о победе и остановить игру.

    - [ ] Счётчик подбитых кораблей.
        - [x] Добавить на поле.
        - [x] Добавить данные.
        - [ ] Сделать значение счётчика на экране, зависимым от счётчика подбитий.


Design and implement a (partial) Battleship game as a web app.

In Battleship, the computer has positioned five ships of various sizes on a 10x10 board.
Each ship must be placed horizontally or vertically, completely on the board, without
overlapping another ship. The player cannot see the ship locations. Each round, the player
“fires” at a board position of his choosing. The computer indicates if this was a “hit” or a
“miss”. When all tiles of a particular ship have been hit, the computer indicates that the entire
ship has been sunk. When the player has sunk all of the ships, the game is over.
Obviously this game would be more fun if the player had his own ships and the computer were
firing back, but we’ll leave that out for simplicity. In other words, we are only implementing
the turns for Player 1, not for Player 2.

You may use the provided JSON data (see below) indicating the position of the ships.
You should produce a web app for this game as described, according to the provided mocks.
The game should be responsive and mobile-friendly, so that it may be played on an iPhone 5-sized
screen (320x568) up to a desktop browser ( approx. 1440x1024).
Please use React for the implementation. You may feel free to use Redux, LESS, or modern ES6
javascript features if you’d like. Please provide the source code for the game and ideally a
hosted version where it can be played (or instructions for running it locally with minimal setup).
It’s not necessary to save game state or anything like that.
Ship layout data:

{
"shipTypes": {
"carrier": { "size": 5, "count": 1 },
"battleship": { "size": 4, "count": 1 },
"cruiser": { "size": 3, "count": 1 },
"submarine": { "size": 3, "count": 1 },
"destroyer": { "size": 2, "count": 1 },
},
"layout": [
{ "ship": "carrier", "positions": [[2,9], [3,9], [4,9], [5,9], [6,9]] },
{ "ship": "battleship", "positions": [[5,2], [5,3], [5,4], [5,5]] },
{ "ship": "cruiser", "positions": [[8,1], [8,2], [8,3]] },
{ "ship": "submarine", "positions": [[3,0], [3,1], [3,2]] },
{ "ship": "destroyer", "positions": [[0,0], [1,0]] }
]
}


As for the server side you should supply CRUD (create read update delete), for ShipLayouts and game itself.
So – you may create or update Ship types "carrier": { "size": 5, "count": 1 },

As for game you do not need to implement any Ai for games and specify ability to select multiplayer
You just may account that 	you need to win game in shortest count of moves. So you may store number of moves on server side.
___________________________________________________________________

Разработайте и реализуйте (частичную) игру Battleship как веб-приложение.

В «Морском сражении» компьютер разместил пять кораблей разных размеров на доске 10х10.
Каждый корабль должен быть размещен горизонтально или вертикально, полностью на доске,
не перекрывая другой корабль. Игрок не может видеть локации кораблей. В каждом раунде игрок
«стреляет» по выбранной им позиции на доске. Компьютер указывает, было ли это «попаданием»
или «промахом». Когда все плитки определенного корабля поражены, компьютер показывает,
что весь корабль потоплен. Когда игрок потопил все корабли, игра окончена.
Очевидно, эта игра была бы более увлекательной, если бы у игрока были свои корабли и компьютер
стрелял в ответ, но мы оставим это для простоты. Другими словами, мы реализуем ходы только для
Игрока 1, а не для Игрока 2.

Вы можете использовать предоставленные данные JSON (см. Ниже), чтобы указать положение кораблей.
Вы должны создать веб-приложение для этой игры, как описано, в соответствии с предоставленными
макетами. Игра должна быть отзывчивой и удобной для мобильных устройств, чтобы в нее можно было
играть на экране iPhone 5 (320x568) или в браузере настольного компьютера (прибл. 1440x1024).
Пожалуйста, используйте React для реализации. Вы можете свободно использовать Redux, LESS или
современные функции JavaScript ES6, если хотите. Пожалуйста, предоставьте исходный код игры и,
в идеале, размещенную версию, в которой в нее можно будет играть (или инструкции по ее
локальному запуску с минимальной настройкой). Нет необходимости сохранять состояние игры
или что-то в этом роде. Данные компоновки корабля:
{
"shipTypes": {
"carrier": {"size": 5, "count": 1},
"линкор": {"размер": 4, "количество": 1},
"крейсер": {"размер": 3, "количество": 1},
"подводная лодка": {"размер": 3, "количество": 1},
"destroyer": {"size": 2, "count": 1},
},
"макет": [
{"корабль": "перевозчик", "позиции": [[2,9], [3,9], [4,9], [5,9], [6,9]]},
{"корабль": "линкор", "позиции": [[5,2], [5,3], [5,4], [5,5]]},
{"корабль": "крейсер", "позиции": [[8,1], [8,2], [8,3]]},
{"корабль": "подводная лодка", "позиции": [[3,0], [3,1], [3,2]]},
{"корабль": "эсминец", "позиции": [[0,0], [1,0]]}
]
}

Что касается серверной части, вы должны предоставить CRUD (создать чтение, обновление, удаление), для ShipLayouts и самой игры.
Итак - вы можете создать или обновить типы кораблей "carrier": {"size": 5, "count": 1},
Что касается игры, вам не нужно реализовывать какой-либо Ai для игр и указывать возможность выбора мультиплеера.
Вы просто можете учесть, что вам нужно выиграть игру за кратчайшее количество ходов. Таким образом, вы можете хранить количество ходов на стороне сервера.