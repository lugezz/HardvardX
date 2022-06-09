if(!localStorage.getItem('myCounter')){
	localStorage.setItem('myCounter', 0)
};

let counter = localStorage.getItem('myCounter');

document.addEventListener ('DOMContentLoaded', function () {
	document.querySelector('h1').innerHTML = localStorage.getItem('myCounter');
	document.querySelector('button').onclick = count
});

function count () {
	counter ++;
	document.querySelector ('h1').innerHTML = counter;

	localStorage.setItem('myCounter', counter);
	//if (counter % 10 === 0){
	//	alert (`Count is now ${counter}`)
	//}
}

setInterval (count, 1000);