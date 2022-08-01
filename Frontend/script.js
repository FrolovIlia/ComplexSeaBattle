$('.game_field').click(function(e){
    const target = this.getBoundingClientRect();
    const y = e.clientX - target.left;
    const x = e.clientY - target.top;
    const size_sect = $('.game_field').width() / 10;

    let coordinate_x = Math.floor(x/size_sect);
    let coordinate_y = Math.floor(y/size_sect);

    alert(coordinate_x + ", " + coordinate_y);
});
