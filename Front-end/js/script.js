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

/*
let post = document.querySelectorAll('.post');
let accordion = post.querySelectorAll('.accordion');

for (let i = 0; i < accordion.length; i++) {
    accordion[i].addEventListener('click', () => {
        let comment = post.querySelector('.comment');
        if (comment.style.maxHeight) {
            comment.style.maxHeight = null;
        } else {
            comment.style.maxHeight = comment.scrollHeight + "px";
        }
    })
}
*/


/*
document.querySelector('.post').addEventListener('click', (e) => {
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


$(document).ready(function() {
    $(".accordion").click(function() {
        const value = $(this).attr("data-filter")
            // $(".comment").not('.' + value).hide(1000);
        $(".comment").filter('.' + value).toggle(1000);
    })
});