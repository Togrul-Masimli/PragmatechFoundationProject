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

document.querySelector('.col-6').addEventListener('click', (e) => {
    if (e.target.getAttribute('class') == 'accordion') {
        let comment = document.querySelector('.comment');
        if (comment.style.maxHeight) {
            comment.style.maxHeight = null;
        } else {
            comment.style.maxHeight = comment.scrollHeight + "px";
        }
    }
})