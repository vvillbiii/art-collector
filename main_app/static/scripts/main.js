$(".navbar-burger").click(function () {
  $(".navbar-burger").toggleClass("is-active");
  $(".navbar-menu").toggleClass("is-active");
});

$(".dropdown").click(function (event) {
  $(this).toggleClass("is-active");
});

const darkButton = document.getElementById("dark");
const lightButton = document.getElementById("light");
const theme = localStorage.getItem("theme");
const nav = document.body.nav;

const body = document.body;

if (theme) {
  body.classList.add(theme);
}

darkButton.onclick = () => {
  // body.classList.remove("light");
  // body.classList.add("dark");
  body.classList.replace("light", "dark");
  localStorage.setItem("theme", "dark");
  nav.classList.replace("light", "dark");
};

lightButton.onclick = () => {
  // body.classList.remove("dark");
  // body.classList.add("light");
  body.classList.replace("dark", "light");
  localStorage.setItem("theme", "light");
  nav.classList.replace("dark", "light");
};
