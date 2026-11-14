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
      if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); }
    });
  }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
  var groups = new Map();
  els.forEach(function (el) {
    if (el.getBoundingClientRect().top < vh * 0.9) return; // already visible: no flash
    var n = groups.get(el.parentElement) || 0;
    groups.set(el.parentElement, n + 1);
    el.style.setProperty('--ri', Math.min(n, 5));
    el.setAttribute('data-reveal', '');
    io.observe(el);
  });
  document.documentElement.classList.add('motion-js');
})();
