// JavaScript source code
// The function gets called when the window is fully loaded
var canvas;
var ctx;
var dx = 5;
var dy = 5;
var x = 100;
var y = 50;
var WIDTH = 200;
var HEIGHT = 200;
var img = new Image(50, 50);
img.src = 'static/letterA.png'

function circle(x, y, img) {
    ctx.drawImage(img, x, y);
}

function rect(x, y, w, h) {
    ctx.beginPath();
    ctx.rect(x, y, w, h);
    ctx.closePath();
    ctx.fill();
    ctx.stroke();
}

function clear() {
    ctx.clearRect(0, 0, WIDTH, HEIGHT);
}

function init() {
    canvas = document.getElementById("viewport");
    ctx = canvas.getContext("2d");
    return setInterval(draw, 10);
}

function doKeyDown(evt) {
    switch (evt.keyCode) {
        case 38:  /* Up arrow was pressed */
            if (y - dy > 0) {
                y -= dy;
            }
            break;
        case 40:  /* Down arrow was pressed */
            if (y + dy < HEIGHT) {
                y += dy;
            }
            break;
        case 37:  /* Left arrow was pressed */
            if (x - dx > 0) {
                x -= dx;
            }
            break;
        case 39:  /* Right arrow was pressed */
            if (x + dx < WIDTH) {
                x += dx;
            }
            break;
    }
}

function draw() {
    clear();
    ctx.clearRect(0, 0, WIDTH, HEIGHT);
    ctx.strokeStyle = "black";
    rect(0, 0, WIDTH, HEIGHT);
    ctx.clearRect(0, 0, WIDTH, HEIGHT);
    circle(x, y, 10);
}

init();
window.addEventListener('keydown', doKeyDown, true);