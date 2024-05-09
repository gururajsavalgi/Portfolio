var typed=new Typed(".text1",{
    strings : ["Pythonist",'Django Developer','Frontend Developer'],
    typeSpeed : 100,
    backSpeed : 100,
    backDelay : 1000,
    loop:true
})

/*javascript of navbar*/
document.addEventListener('DOMContentLoaded', function() {
    const menuToggle = document.getElementById('menu-toggle');
    const navbar = document.getElementById('navbar');

    menuToggle.addEventListener('click', function() {
        // Toggle the 'open' class to show/hide the navbar
        navbar.classList.toggle('open');
    });
});


function checkLink(event, url) {
    if (!url) {  // If the URL is empty or undefined
        event.preventDefault();  // Prevent the default action (navigation)
        alert("No link is provided.");  // Display an alert message
    }
}
