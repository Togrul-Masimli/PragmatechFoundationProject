document.querySelector('.to-top').addEventListener('click', () => {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    })
});


$(document).ready(function() {
    $(".accordion").click(function() {
        const value = $(this).attr("data-filter")
        $(".comment").filter('.' + value).toggle(700);
    })
});

$(document).ready(function() {
    $(".profile-filter").click(function() {
        const value = $(this).attr("data-filter")
        $(".toggle").not('.' + value).hide(700);
        $(".toggle").filter('.' + value).show(700);
    })
});


var comments = document.querySelectorAll('.comment-button');

for (let i = 0; i < comments.length; i++) {
    comments[i].addEventListener('click', () => {
        this.classList.toggle("active");
    })

}