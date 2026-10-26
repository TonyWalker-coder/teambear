//ensure we have a theme to load on a new system
const themes = ["light", "lightblue", "dark", "grey"];

let theme = localStorage.getItem("theme");

if (!themes.includes(theme)) {
    console.warn(`Unknown theme: ${theme}`);
    theme = "lightblue";
    localStorage.setItem("theme", theme);
}

document.documentElement.setAttribute("data-theme", theme);



//the mobile hamburger toggle
const menuBtn = document.getElementById("menuBtn");
const menu = document.getElementById("mobileMenu");

menuBtn.addEventListener("click", () => {


    menu.classList.toggle("open");

    const isOpen = menu.classList.contains("open");

    menuBtn.setAttribute("aria-expanded", isOpen);

    menuBtn.classList.toggle("open", isOpen);

});
//the theme toggle

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
//the message modal system
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
//open the product selection panel card and close any open cards
//changes aria collapses state of panel
//active high lighting included now
document.querySelectorAll('.inside-category-card').forEach(card => {
    card.addEventListener('click', () => {

        const button = card.querySelector('button');

        const current = card
            .closest('.category-card')
            .querySelector('.proditems');

        const isOpening = current.classList.contains('hidden');

        // close all panels
        document.querySelectorAll('.proditems').forEach(item => {
            item.classList.add('hidden');



        });


        // reset all aria-expanded values
        document.querySelectorAll('.inside-category-card button').forEach(btn => {
            btn.setAttribute('aria-expanded', 'false');

        });
        // remove active from all buttons
        document
            .querySelectorAll('.category-button')
            .forEach(button => {
                button.classList.remove('active');
            });

        if (isOpening) {

            current.classList.remove('hidden');

            button.setAttribute('aria-expanded', 'true');

            button.classList.add('active');

        } else {

            button.setAttribute('aria-expanded', 'false');

        }
        if (isOpening) {
            current.classList.remove('hidden');

            // update the clicked button
            button.setAttribute('aria-expanded', 'true');

            button.classList.add("active");


            // ⚠️ state check for future refresh call
            console.log('Category opened');
        }
    });
});
//read the product grid buttons for data-product-id our bearcard search
document.addEventListener("click", (event) => {

    const button = event.target.closest("[data-product-id]");

    if (!button) {
        return;
    }

    const productId = button.dataset.productId;
    const team = button.dataset.team;
    const type = button.dataset.type;
    const desc = button.dataset.desc;

    console.log("click");
    console.log("data-team:", team, "data-type:", type, "data-desc:", desc);

    fetch(
        `/product-search/?team=${team}&type=${type}&desc=${desc}`
    )
        .then(response => {

            if (!response.ok) {
                throw new Error(
                    `HTTP Error: ${response.status}`
                );
            }

            return response.json();

        })
        .then(data => {

            console.log(data);

        })
        .catch(error => {

            console.error(
                "Product search failed:",
                error
            );

        });
}); 