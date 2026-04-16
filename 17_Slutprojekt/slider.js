let currentIndex = 0;
const slides = document.querySelectorAll('.slide');

function showSlide(index) {
  // Om vi går förbi sista bilden, gå till första
  if (index >= slides.length) currentIndex = 0;
  // Om vi går bakåt från första bilden, gå till sista
  else if (index < 0) currentIndex = slides.length - 1;
  else currentIndex = index;

  // Ta bort "active" från alla bilder och lägg till på den rätta
  slides.forEach(slide => slide.classList.remove('active'));
  slides[currentIndex].classList.add('active');
}

function changeSlide(direction) {
  showSlide(currentIndex + direction);
}

// Bonus: Byt bild automatiskt var 5:e sekund
setInterval(() => {
  changeSlide(1);
}, 5000);