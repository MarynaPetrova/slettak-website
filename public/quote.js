(() => {
const gallery = document.querySelector('.tak-gallery');
const finishCopy = document.querySelector('.tak-finish-copy');
const image = gallery.querySelector('img');
const buttons = gallery.querySelectorAll('button[data-src]');
buttons.forEach(button => button.addEventListener('click', () => {
  if (button.getAttribute('aria-pressed') === 'true') return;
  image.src = button.dataset.src;
  image.alt = button.textContent;
  finishCopy.textContent = button.dataset.description;
  buttons.forEach(item => item.setAttribute('aria-pressed', String(item === button)));
  if (!matchMedia('(prefers-reduced-motion: reduce)').matches) {
    image.getAnimations().forEach(animation => animation.cancel());
    image.animate(
      [{opacity: .35, transform: 'translateX(5%) scale(1.06)'}, {opacity: 1, transform: 'none'}],
      {duration: 640, easing: 'ease-out'}
    );
  }
}));


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

})();

(() => {
  const header = document.querySelector('.top');
  let frame;
  const cancelScroll = () => cancelAnimationFrame(frame);
  window.addEventListener('touchstart', cancelScroll, {passive: true});
  window.addEventListener('wheel', cancelScroll, {passive: true});
  header?.addEventListener('click', event => {
    if (!matchMedia('(max-width: 850px)').matches || event.defaultPrevented ||
        event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    const link = event.target.closest('nav a[href^="#"]');
    if (!link) return;
    const hash = link.getAttribute('href');
    const section = document.getElementById(hash.slice(1));
    if (!section) return;
    event.preventDefault();
    cancelScroll();
    if (location.hash) history.replaceState(history.state, '', location.pathname + location.search);
    const top = hash === '#hjem' ? 0 :
      window.scrollY + section.getBoundingClientRect().top - header.getBoundingClientRect().height - 12;
    const destination = Math.max(0, Math.min(top, document.documentElement.scrollHeight - innerHeight));
    if (matchMedia('(prefers-reduced-motion: reduce)').matches) {
      window.scrollTo({top: destination, behavior: 'instant'});
      return;
    }
    const start = window.scrollY;
    const duration = Math.min(1100, 600 + Math.abs(destination - start) / 6);
    const started = performance.now();
    function move(now) {
      const progress = Math.min(1, (now - started) / duration);
      const eased = progress * progress * (3 - 2 * progress);
      window.scrollTo({top: start + (destination - start) * eased, behavior: 'instant'});
      if (progress < 1) frame = requestAnimationFrame(move);
    }
    frame = requestAnimationFrame(move);
  });
})();
