(function () {
  var top = document.querySelector('.top');
  if (top) {
    var onScroll = function () { top.classList.toggle('is-scrolled', window.scrollY > 8); };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }
  if (!('IntersectionObserver' in window)) return;
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  var sel = [
    'main section:not(.video-hero):not(.trust-strip) .eyebrow',
    'main section:not(.video-hero):not(.trust-strip) h2',
    '.section-heading', '.ceiling-guide-intro > p:not(.eyebrow)',
    '.solution-card', '#prosess .steps article',
    '.ceiling-guide-questions details', '#om-oss .about-visual',
    '.contact-grid > div', '#contactForm', '.footer-video-copy'
  ].join(',');
  var els = Array.prototype.slice.call(document.querySelectorAll(sel));
  els = els.filter(function (el) {
    for (var p = el.parentElement; p; p = p.parentElement) if (els.indexOf(p) !== -1) return false;
    return true;
  });
  var vh = window.innerHeight;
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting) e.target.classList.add('is-in');
      // reset only when the block leaves through the bottom (user scrolled up),
      // so it animates again on the next scroll down
      else if (e.boundingClientRect.top > 0) e.target.classList.remove('is-in');
    });
  }, { rootMargin: '0px 0px -8% 0px', threshold: 0 });
  var groups = new Map();
  els.forEach(function (el) {
    var n = groups.get(el.parentElement) || 0;
    groups.set(el.parentElement, n + 1);
    el.style.setProperty('--ri', Math.min(n, 5));
    if (el.getBoundingClientRect().top < vh * 0.9) el.classList.add('is-in'); // visible at load: no flash
    el.setAttribute('data-reveal', '');
    io.observe(el);
  });
  document.documentElement.classList.add('motion-js');
})();
