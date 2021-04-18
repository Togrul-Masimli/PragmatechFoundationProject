let block = document.createElement('div');

document.querySelector('body').appendChild(block);
block.classList.add('content');

block.setAttribute('style', "width:250px; height:250px; background-color: indigo; margin: auto auto; display:flex");

for (i = 0; i < 5; i++) {
    let children = document.createElement('div');
    document.querySelector('.content').appendChild(children);
    children.setAttribute('style', "width:50px; height:50px; background-color: red;");
    children.addEventListener("click", function() {
        let x = Math.floor(Math.random() * 256);
        let y = Math.floor(Math.random() * 256);
        let z = Math.floor(Math.random() * 256);
        let bgColor = "rgb(" + x + "," + y + "," + z + ")";
        children.style.background = bgColor;
    });
}