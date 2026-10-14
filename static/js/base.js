//ensure we have a theme to load on a new system
const theme =
    localStorage.getItem("theme") ||
    "lightblue";


if (!localStorage.getItem("theme")) {
    localStorage.setItem("theme", theme);
}

document.documentElement.setAttribute("data-theme", theme);
//The mobile hamburger toggle
const menuBtn = document.getElementById("menuBtn");
const menu = document.getElementById("mobileMenu");

menuBtn.addEventListener("click", () => {


    menu.classList.toggle("open");

    const isOpen = menu.classList.contains("open");

    menuBtn.setAttribute("aria-expanded", isOpen);

    menuBtn.classList.toggle("open", isOpen);

});
//The theme toggle
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
//The message modal system
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
//open the product selection card close any open cards
document.querySelectorAll('.inside-category-card').forEach(card => {
    card.addEventListener('click', () => {

        const current = card
            .closest('.category-card')
            .querySelector('.proditems');

        const isOpening = current.classList.contains('hidden');

        document.querySelectorAll('.proditems').forEach(item => {
            item.classList.add('hidden');
        });

        if (isOpening) {
            current.classList.remove('hidden');

            // Future refresh call
            console.log('Category opened');
        }
    });
});