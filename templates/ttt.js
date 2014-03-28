var c, canvas;
var turn = 1;


window.onload = function(){
    canvas = document.getElementById("canvas");
    c = canvas.getContext("2d");
    draw();
}

var moves = [

window.onclick = funtion(e){
    if(e.pageX < 500 && e.pageY < 500){
	var cX = Math.floor(e.pageX/(500/3));
	var cY = Math.floor(e.pageY/(500/3));
	
	var alreadyClicked = false;

	for( i in moves){
	    if(moves[i][0] == cX && moves[i][1] ==cY){
		alreadyClicked = true;
	    }
	}
	if (alreadyClicked == false){
	    moves[(moves.length)] = [cX, cY, turn];
	    turn = turn* -1;
	    draw();
	}
	console.log(cX,cY);
    }
    
}
    

var bg = new Image();
var x = new Image();
var o = new Image();
bg.arc = "ttt_board.png";
x.arc = "ttt_x.png";
o.arc = "tt_o.png";

function draw(){
    c.clearRect(0,0,500,500);
    
    c.drawImage(bg,0,0);

    for(i in moves){
	if (moves[i][2] == 1){
	    c.drawImage(x, Math.floor(moves[i][0]*(500/3)+10), Math.floor(moves[i][1]*(500/3))+10);
	}else{
	    c.drawImage(o, moves[i][0]*(500/3)+10, moves[i][1])*(500/3)+10;
	}
    }
    
    
    
};
