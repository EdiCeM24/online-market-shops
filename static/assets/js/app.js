document.addEventListener('scroll', function() {
    var scrollPosition = window.scrollY;
    if(scrollPosition > 100) {
        document.body.style.background = '#203040';
    }else{
        document.body.style.background = 'white';
    }
})


