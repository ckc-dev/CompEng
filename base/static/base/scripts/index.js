const mobileNav = document.querySelector("nav.mobile");
const mobileNavToggle = document.querySelector(".mobile-nav-toggle");

mobileNavToggle.onclick = () => mobileNav.classList.toggle("hidden");
