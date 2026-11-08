(() => {
  const video = document.querySelector('.video-hero-media');
  const hero = video.closest('.video-hero');
  const reducedMotion = matchMedia('(prefers-reduced-motion: reduce)');
  let inView = false;
  let pending = false;
  let blocked = false;

  function updatePlayback() {
    if (!inView || document.hidden || reducedMotion.matches) {
      video.pause();
      return;
    }
    if (pending || blocked || !video.paused) return;

    if (!video.firstElementChild) {
      const files = matchMedia('(max-width: 768px)').matches
        ? [['hero-villa-mobile.mp4', 'video/mp4']]
        : [['hero-villa.webm', 'video/webm'], ['hero-villa.mp4', 'video/mp4']];

      for (const [file, type] of files) {
        const source = document.createElement('source');
        source.src = 'assets/video/' + file;
        source.type = type;
        video.append(source);
      }
      video.muted = true;
    }

    pending = true;
    video.play().then(() => {
      if (!video.paused) video.classList.add('is-playing');
    }).catch(error => {
      if (error.name !== 'AbortError') {
        blocked = true;
        video.classList.remove('is-playing');
      }
    }).finally(() => {
      pending = false;
      if (!blocked && video.paused && inView && !document.hidden && !reducedMotion.matches) {
        updatePlayback();
      }
    });
  }

  new IntersectionObserver(([entry]) => {
    inView = entry.isIntersecting;
    updatePlayback();
  }).observe(hero);

  reducedMotion.addEventListener('change', updatePlayback);
  document.addEventListener('visibilitychange', updatePlayback);
})();
