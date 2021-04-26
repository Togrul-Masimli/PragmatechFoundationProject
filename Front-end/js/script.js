/* document.querySelectorAll('.accordion').addEventListener("click", () => {
    let accordion = document.querySelector('.accordion');
    let comment = document.querySelector('.comment');

    if (comment.style.maxHeight) {
        comment.style.maxHeight = null;
    } else {
        comment.style.maxHeight = comment.scrollHeight + "px";
    }
});
*/

let accordion = document.querySelectorAll('.accordion');

for (let i = 0; i < accordion.length; i++) {
    accordion[i].addEventListener('click', () => {
        let comment = document.querySelector('.comment');
        if (comment.style.maxHeight) {
            comment.style.maxHeight = null;
        } else {
            comment.style.maxHeight = comment.scrollHeight + "px";
        }
    })
}


/*
document.querySelector('.col-6').addEventListener('click', (e) => {
    if (e.target.getAttribute('class') == 'accordion') {
        if (document.querySelector('.comment').style.maxHeight) {
            document.querySelector('.comment').style.maxHeight = null;
        } else {
            document.querySelector('.comment').style.maxHeight = document.querySelector('.comment').scrollHeight + "px";
        }
    }
});
*/


document.querySelector('.to-top').addEventListener('click', () => {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    })
});