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

if ('IntersectionObserver' in window) {
  const observer = new IntersectionObserver(([entry]) => {
    if (entry.isIntersecting) {
      gallery.classList.add('tak-entered');
      observer.disconnect();
    }
  }, {threshold: .25});
  observer.observe(gallery);
}

const quote = document.querySelector('.tak-quote');
const length = quote.querySelector('[name="ceiling_length_m"]');
const width = quote.querySelector('[name="ceiling_width_m"]');
const area = quote.querySelector('[name="ceiling_area_m2"]');
const output = quote.querySelector('output');
const finish = quote.querySelector('[name="ceiling_finish"]');
const price = quote.querySelector('[data-price]');
const submittedPrice = quote.querySelector('[name="ceiling_estimate_nok_incl_vat"]');
const money = new Intl.NumberFormat(document.documentElement.lang, {
  style: 'currency', currency: 'NOK', maximumFractionDigits: 0
});
const formatter = new Intl.NumberFormat(document.documentElement.lang, {maximumFractionDigits: 2});
// Indicative consumer rates in NOK per square metre, including VAT.
const rates = {matte: 850, satin: 950, glossy: 1050};
function updateArea() {
  const result = length.valueAsNumber * width.valueAsNumber;
  const valid = length.validity.valid && width.validity.valid && Number.isFinite(result) && result > 0;
  area.value = valid ? result.toFixed(2) : '';
  output.textContent = valid ? formatter.format(Number(area.value)) + ' m²' : '—';
  const rate = rates[finish.value];
  const total = valid && rate ? Math.round(result * rate) : null;
  price.textContent = total === null ? '—' : money.format(total);
  submittedPrice.value = total === null ? '' : String(total);
}
length.addEventListener('input', updateArea);
width.addEventListener('input', updateArea);
finish.addEventListener('change', updateArea);
window.addEventListener('pageshow', updateArea);
updateArea();
