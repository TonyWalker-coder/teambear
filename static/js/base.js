const menuBtn = document.getElementById("menuBtn");
const menu = document.getElementById("mobileMenu");

menuBtn.addEventListener("click", () => {


    menu.classList.toggle("open");

    const isOpen = menu.classList.contains("open");

    menuBtn.setAttribute("aria-expanded", isOpen);

    menuBtn.classList.toggle("open", isOpen);

});

const themes = ["winter", "therapy", "light", "lightblue", "dark", "grey", "clasicbear", "darkheat"];

document.getElementById("themeToggle").addEventListener("click", () => {

    const root = document.documentElement;

    const currentTheme =
        root.getAttribute("data-theme") || THEMES[0];

    const currentIndex =
        THEMES.indexOf(currentTheme);

    const nextTheme =
        THEMES[(currentIndex + 1) % THEMES.length];

    root.setAttribute("data-theme", nextTheme);

    localStorage.setItem("theme", nextTheme);

});

document.addEventListener("DOMContentLoaded", function () {
    const savedTheme = localStorage.getItem("theme") || "spring";
    document.documentElement.setAttribute("data-theme", savedTheme);
});