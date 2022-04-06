var i = 0;
var a = 0
var b = 0
var txt1 = 'Hi,'; /* The text */
var txt2 = 'I\'m Alex,';
var txt3 = 'Welcome to My Portfolio';
var speed = 100; /* The speed/duration of the effect in milliseconds */

function typeWriter() {
    if (i < txt1.length) {
        document.getElementById("header_text1").innerHTML += txt1.charAt(i);
        i++;
        setTimeout(typeWriter, speed);
    }
}

function typeWriter2() {
    if (a < txt2.length) {
        document.getElementById("header_text2").innerHTML += txt2.charAt(a);
        a++;
        setTimeout(typeWriter2, speed);
    }
}

function typeWriter3() {
    if (b < txt3.length) {
        document.getElementById("header_text3").innerHTML += txt3.charAt(b);
        b++;
        setTimeout(typeWriter3, speed);
    }
}



setTimeout(typeWriter, 620);
setTimeout(typeWriter2, 1720);
setTimeout(typeWriter3, 3000);