const theme =
    localStorage.getItem("theme") ||
    "lightblue";


if (!localStorage.getItem("theme")) {
    localStorage.setItem("theme", theme);
}

const menuBtn = document.getElementById("menuBtn");
const menu = document.getElementById("mobileMenu");

menuBtn.addEventListener("click", () => {


    menu.classList.toggle("open");

    const isOpen = menu.classList.contains("open");

    menuBtn.setAttribute("aria-expanded", isOpen);

    menuBtn.classList.toggle("open", isOpen);

});

const themes = ["light", "lightblue", "dark", "grey"];

document
    .querySelectorAll(".theme-toggle-btn")
    .forEach(button => {

        button.addEventListener("click", () => {


            const root = document.documentElement;

            const currentTheme =
                root.getAttribute("data-theme") || themes[0];

            const currentIndex =
                themes.indexOf(currentTheme);

            const nextTheme =
                themes[(currentIndex + 1) % themes.length];

            root.setAttribute("data-theme", nextTheme);

            localStorage.setItem("theme", nextTheme);
        });
    });

document.addEventListener("DOMContentLoaded", function () {
    const savedTheme = localStorage.getItem("theme") || "spring";
    document.documentElement.setAttribute("data-theme", savedTheme);
});

function messageModal(type, title, message) {
    
    modal.classList.remove(
        "info",
        "success",
        "warning",
        "error"
    );

    document
        .querySelectorAll(".bear-toggle")
        .forEach(el => el.classList.add("hidden"));

    switch (type) {

        case "i":
            modal.classList.add("info");
            infoBear.classList.remove("hidden");
            break;

        case "s":
            modal.classList.add("success");
            successBear.classList.remove("hidden");
            break;

        case "w":
            modal.classList.add("warning");
            warningBear.classList.remove("hidden");
            break;

        case "e":
            modal.classList.add("error");
            errorBear.classList.remove("hidden");
            break;
    }

    messageElement.textContent = message;

    modal.classList.remove("hidden");
}