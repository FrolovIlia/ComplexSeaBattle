let data = {
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

    alert(coordinate_x + ", " + coordinate_y);


    for (let pos = 0; pos < data.layout.length; pos++) {
        alert("Нужно подбить: " + data.layout[pos].ship + ", " + "Количество палуб: " +
            data.layout[pos].positions.length)
    }
});




// let text = "";
//
// for (let ship_pos = 0; ship_pos < data.layout.length; ship_pos++) {
//     for (let ship_len = 0; ship_len < data.layout[ship_pos].positions.length; ship_len++) {
//         text += "<img class=\"indicator\" src=\"images/m_Miss%20small.png\" alt=\"\">"
//     }
// }

// document.getElementById("aircraft").innerHTML = text;




function myFunction(ship_name) {
    let text = "";

    for (let ship_pos = 0; ship_pos < data.shipTypes[ship_name].size; ship_pos++) {
        text += "<img src=\"images/m_Miss%20small.png\" alt=\"\">"
        }
        return text;
}

document.getElementById("carrier").innerHTML = myFunction("carrier");
document.getElementById("battleship").innerHTML = myFunction("battleship");
document.getElementById("cruiser").innerHTML = myFunction("cruiser");
document.getElementById("submarine").innerHTML = myFunction("submarine");
document.getElementById("destroyer").innerHTML = myFunction("destroyer");




