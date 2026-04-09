const toggleButton = document.querySelector(".menu-toggle");
const menu = document.querySelector(".menu");

toggleButton.addEventListener("click", () => {
  menu.classList.toggle("active");

  const isOpen = menu.classList.contains("active");
  toggleButton.setAttribute("aria-expanded", isOpen);
});