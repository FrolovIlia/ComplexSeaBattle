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


$('.game_field').click(function(e){
    const target = this.getBoundingClientRect();
    const y = e.clientX - target.left;
    const x = e.clientY - target.top;
    const size_sect = $('.game_field').width() / 10;

    let coordinate_x = Math.floor(x/size_sect);
    let coordinate_y = Math.floor(y/size_sect);
    let complex_coordinate = [coordinate_x, coordinate_y]

    alert(coordinate_x + ", " + coordinate_y);
    alert("На БЭК буду передавать координаты: " + complex_coordinate)

    // for (let pos = 0; pos < data.layout.length; pos++) {
    //     alert("Нужно подбить: " + data.layout[pos].ship + ", " + "Количество палуб: " +
    //         data.layout[pos].positions.length)
    // }
});


function drawIndicators(ship_name) {
    let text = "";

    for (let ship_pos = 0; ship_pos < data.shipTypes[ship_name].size; ship_pos++) {
        text += "<img src=\"static/images/m_Miss%20small.png\" alt=\"\">"
        }
        return text;
}

for (let shipName in data.shipTypes) {
    document.getElementById(shipName + "-lives").innerHTML = drawIndicators(shipName);
}


let counter1_value = 0
// let counter2_value = 0

function drawCountValue1(value1) {
    if (value1 > counter1_value) {
        counter1_value = value1
    }
    return counter1_value
}

document.getElementById("count1").innerHTML = "0" + drawCountValue1(counter1_value);


$.post({
    url: "/start_game",
    dataType: "json",
    contentType: "application/json",
    data: JSON.stringify(data),
    success: (data) => {data.message}
})

$.post({
    url: "/shot_coordinate",
    dataType: "json",
    contentType: "application/json",
    data: JSON.stringify(data),
    success: (data) => {data.message}
})