document.querySelector('.accordion').addEventListener("click", () => {
    let accordion = document.querySelector('.accordion');
    let comment = document.querySelector('.comment');

    if (comment.style.maxHeight) {
        comment.style.maxHeight = null;
    } else {
        comment.style.maxHeight = comment.scrollHeight + "px";
    }
});