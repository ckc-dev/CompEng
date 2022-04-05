//Menu Button - Hamburger Menu
const btnMenu = document.getElementById('btn-menu');

function toggleMenu(event) {
    const navbar = document.getElementById('navbar');
    navbar.classList.toggle('active')
}

btnMenu.addEventListener('click', toggleMenu);