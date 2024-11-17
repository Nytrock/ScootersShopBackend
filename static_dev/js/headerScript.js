let timeNode = document.querySelector(`#time`);
let priceNode = document.querySelector(`#amount`);
let input = document.querySelector(`#buyInput`);
let time = 0;
let hours = 0;

input.addEventListener(`input`, print);

function print(evt){
    time = evt.target.value;
    priceNode.innerHTML = time * 5;

    if(evt.target.value == 120){
        hours = 2;
        timeNode.innerHTML = hours  + ` часа`;
    } else if (evt.target.value == 60) {
        hours = 1;
        timeNode.innerHTML = hours  + ` час`;
    } else if (evt.target.value > 60){
        hours = 1;
        timeNode.innerHTML = hours + " час " + (time-60) + " минут";
    } else if(evt.target.value < 60){
        timeNode.innerHTML = time + " минут";
    }

}
