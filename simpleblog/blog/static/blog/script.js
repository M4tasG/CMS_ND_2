var element = document.getElementById("body_bg");

function applyAnimatedBg(){
    var colors = ['green', 'blue', 'red', 'yellow', 'orange', 'purple', 'pink', 'brown', 'black', 'grey', 'white'];
    var i = 0;
    setInterval(function(){
        element.style.backgroundColor = colors[i];
        i++;
        if(i >= colors.length){
            i = 0;
        }
    }, 1000);
}