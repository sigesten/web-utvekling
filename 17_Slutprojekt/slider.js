
let currentIndex = 0;
const slides = document.querySelectorAll('.slide');

// Spara intervallet i en variabel
let autoSlideInterval;

// main slide funktion 
function showSlide(index) {
  if (index >= slides.length) currentIndex = 0;
  else if (index < 0) currentIndex = slides.length - 1;
  else currentIndex = index;

  slides.forEach(slide => slide.classList.remove('active'));
  slides[currentIndex].classList.add('active');
}

// Starta auto-slide
function startAutoSlide() {
  autoSlideInterval = setInterval(() => {
    changeSlide(1);
  }, 5000);
}

// Återställ auto-slide timern
function resetAutoSlide() {
  clearInterval(autoSlideInterval);
  startAutoSlide();
}

function changeSlide(direction) {
  showSlide(currentIndex + direction);
  resetAutoSlide(); // Återställ timern vid manuellt klick
}

// Starta auto-slide när sidan laddas
startAutoSlide();