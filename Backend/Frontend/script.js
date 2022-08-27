const data = {
"shipTypes": {
"carrier": { "size": 5, "count": 1 },
"battleship": { "size": 4, "count": 1 },
"cruiser": { "size": 3, "count": 1 },
"submarine": { "size": 3, "count": 1 },
"destroyer": { "size": 2, "count": 1 }
},
"layout": [
{ "ship": "carrier", "positions": [[2,9], [3,9], [4,9], [5,9], [6,9]] },
{ "ship": "battleship", "positions": [[5,2], [5,3], [5,4], [5,5]] },
{ "ship": "cruiser", "positions": [[8,1], [8,2], [8,3]] },
{ "ship": "submarine", "positions": [[3,0], [3,1], [3,2]] },
{ "ship": "destroyer", "positions": [[0,0], [1,0]] }
]
}

let total_shots_counter = 0

$('.game_field').click(function(e){
    const target = this.getBoundingClientRect();
    const y = e.clientX - target.left;
    const x = e.clientY - target.top;
    const size_sect = $('.game_field').width() / 10;

    let coordinate_x = Math.floor(x/size_sect);
    let coordinate_y = Math.floor(y/size_sect);
    let complex_coordinate = [coordinate_x, coordinate_y]

    console.log(complex_coordinate)

    $.post({
    url: "/shot_coordinate",
    dataType: "json",
    contentType: "application/json",
    data: JSON.stringify({shot: complex_coordinate}),
    success: (result) => {
        console.log(result.is_hited_ship);
        drawHits(complex_coordinate, result.is_hited_ship);
        console.log(result.dead_ships);
        document.getElementById("count1").innerHTML = "0" + result.dead_ships;

        console.log("Название корабля: " + result.ship_name)
        console.log("Попаданий в корабль: " + result.ship_hits)

        updateIndicators(result.ship_name, result.ship_hits)

        total_shots_counter += 1  //Увеличить общий счётчик выстрелов
        console.log("Всего выстрелов: " + total_shots_counter)

        if (result.dead_ships === data["layout"].length) {
            stopGame(total_shots_counter)
            console.log("В этот момент будет заблокирован экран, " +
                        "и показано сообщение со статистикой")
        }

    }
    })
});


function drawHits(shot_coordinates, shot_result)  {
    let shot_symbol;

    if (shot_result) {
        document.getElementById("l" + shot_coordinates[0] + "c" + shot_coordinates[1]).innerHTML =
            shot_symbol = "<img class=\"section_pic\" src=\"static/images/red%20x.png\" alt=\"\">";

    } else {
        document.getElementById("l" + shot_coordinates[0] + "c" + shot_coordinates[1]).innerHTML =
            shot_symbol = "<img class=\"section_pic\" src=\"static/images/black%20x.png\" alt=\"\">";
    }
    return shot_symbol;
}


function drawIndicators(ship_name) {
    let text = "";

    for (let ship_pos = 0; ship_pos < data.shipTypes[ship_name].size; ship_pos++) {
        text += "<img class=\"indicator_cell\" src=\"static/images/m_Miss_small.png\" alt=\"\">"
        }
        return text;
}


function updateIndicators(ship_name, ship_hits) {
    let text = "";
    if (ship_name) {
        for (let ship_pos = 0; ship_pos < data.shipTypes[ship_name].size; ship_pos++) {
            if (ship_pos < ship_hits) {
                document.getElementById(ship_name + "-lives").innerHTML =
                    text += "<img class=\"indicator_cell\" src=\"static/images/m_Hit_small.png\" alt=\"\">";
            } else {
                document.getElementById(ship_name + "-lives").innerHTML =
                    text += "<img class=\"indicator_cell\" src=\"static/images/m_Miss_small.png\" alt=\"\">";
            }
        }
        return text;
    }
}


function stopGame(total_shots_counter) {
    // Заблокировать экран.
    document.getElementById("content-blocker").innerHTML =
        "<div id=\"content-blocker\" class=\"content-blocker\"></div>";
    // Вывести финальную статистику.
    document.getElementById("total_score").innerHTML =
        "Congratulations! You won! Total number of shots: " + total_shots_counter;
}



for (let shipName in data.shipTypes) {
    document.getElementById(shipName + "-lives").innerHTML = drawIndicators(shipName);
}


document.getElementById("count1").innerHTML = "00";


$.post({
    url: "/start_game",
    dataType: "json",
    contentType: "application/json",
    data: JSON.stringify(data),
    success: (data) => {data.message}
})

