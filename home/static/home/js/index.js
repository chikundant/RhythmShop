const btn = document.querySelector("button.mobile-menu-button");
const btn2 = document.querySelector("button.mobile-menu-button-close");
const menu = document.querySelector(".mobile-menu");
const body = document.querySelector('body');

btn.addEventListener("click", () => {
    menu.classList.toggle("hidden");
    body.classList.toggle('overflow-hidden');
});

btn2.addEventListener("click", () => {
    menu.classList.toggle("hidden");
    body.classList.toggle('overflow-hidden');
});