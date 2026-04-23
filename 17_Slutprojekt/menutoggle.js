const toggleButton = document.querySelector(".menu-toggle");
const menu = document.querySelector(".menu");
const hamburgare = document.getElementById("hamburgare");  // ← lägg till

toggleButton.addEventListener("click", () => {
  menu.classList.toggle("active");
  hamburgare.classList.toggle("open");  // ← lägg till

  const isOpen = menu.classList.contains("active");
  toggleButton.setAttribute("aria-expanded", isOpen);
});