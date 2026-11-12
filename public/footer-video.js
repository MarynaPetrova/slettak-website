(function(){var s=document.querySelector('.footer-video');if(!s)return;var v=s.querySelector('video');if(!v)return;
if(window.matchMedia&&window.matchMedia('(prefers-reduced-motion:reduce)').matches){s.style.backgroundImage='url('+v.getAttribute('poster')+')';return;}
var loaded=false;function load(){if(loaded)return;loaded=true;v.src=v.getAttribute('data-src');v.load();}
if(!('IntersectionObserver' in window)){load();v.play().catch(function(){});return;}
new IntersectionObserver(function(e){e.forEach(function(x){if(x.isIntersecting){load();v.play().catch(function(){});}else if(loaded){v.pause();}});},{rootMargin:'300px'}).observe(s);})();
