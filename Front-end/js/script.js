document.querySelector('.to-top').addEventListener('click', () => {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    })
});


$(document).ready(function() {
    $(".accordion").click(function() {
        const value = $(this).attr("data-filter")
        $(".comment").filter('.' + value).toggle(500);
    })
});

$(document).ready(function() {
    $(".profile-filter").click(function() {
        const item = $(this).attr("data-filter")
        $(".toggle").not('.' + item).hide(700);
        $(".toggle").filter('.' + item).show(700);
    })
});

document.querySelector('.fas.fa-comment').addEventListener('click', () => {
    document.querySelector('.fas.fa-comment').classList.toggle('.active');
});