const gallery = document.querySelector('.tak-gallery');
const image = gallery.querySelector('img');
const buttons = gallery.querySelectorAll('button[data-src]');
let requestedButton = buttons[0];
buttons.forEach(button => button.addEventListener('click', () => {
  requestedButton = button;
  const next = new Image();
  next.onload = () => {
    if (requestedButton !== button) return;
    image.src = next.src;
    image.alt = button.textContent;
    buttons.forEach(item => item.setAttribute('aria-pressed', String(item === button)));
    if (!matchMedia('(prefers-reduced-motion: reduce)').matches) {
      image.getAnimations().forEach(animation => animation.cancel());
      image.animate([{opacity: .55}, {opacity: 1}], {duration: 420, easing: 'ease-out'});
    }
  };
  next.src = button.dataset.src;
}));

const quote = document.querySelector('.tak-quote');
const length = quote.querySelector('[name="ceiling_length_m"]');
const width = quote.querySelector('[name="ceiling_width_m"]');
const area = quote.querySelector('[name="ceiling_area_m2"]');
const output = quote.querySelector('output');
const formatter = new Intl.NumberFormat(document.documentElement.lang, {maximumFractionDigits: 2});
function updateArea() {
  const result = length.valueAsNumber * width.valueAsNumber;
  const valid = length.validity.valid && width.validity.valid && Number.isFinite(result) && result > 0;
  area.value = valid ? result.toFixed(2) : '';
  output.textContent = valid ? formatter.format(Number(area.value)) + ' m²' : '—';
}
length.addEventListener('input', updateArea);
width.addEventListener('input', updateArea);
window.addEventListener('pageshow', updateArea);
updateArea();
