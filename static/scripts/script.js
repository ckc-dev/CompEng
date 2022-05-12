const body = document.querySelector("body");
const mobileNav = document.querySelector("nav.mobile");
const mobileNavToggle = document.querySelector(".mobile-nav-toggle");

mobileNavToggle.onclick = () => {
  if (mobileNav.classList.contains("hidden")) {
    body.style.overflow = "hidden";
    mobileNav.style.animationName = "nav-mobile-slide-right";
    mobileNav.classList.remove("hidden");
    mobileNav.onanimationend = () => null;
  } else {
    body.style.overflow = "auto";
    mobileNav.style.animationName = "nav-mobile-slide-left";
    mobileNav.onanimationend = () => mobileNav.classList.add("hidden");
  }
};
