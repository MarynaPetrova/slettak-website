(() => {
  const hero = document.querySelector('.video-hero');
  if (!hero) return;
  const assetRoot = new URL('assets/video/', document.currentScript.src);
  const video = hero.querySelector('video');
  const sound = hero.querySelector('.video-hero-sound');
  const enableLabel = sound.getAttribute('aria-label');
  const reducedMotion = matchMedia('(prefers-reduced-motion: reduce)');
  const interaction = new AbortController();
  let revealTimer;
  let startupTimer;
  let awaitingReveal = !reducedMotion.matches;
  let inView = false;
  let starting = false;
  let blocked = false;
  let wantsSound = false;
  let fade;
  let context;
  let gain;

  function reveal(animate = false) {
    if (!awaitingReveal) return;
    awaitingReveal = false;
    clearTimeout(revealTimer);
    clearTimeout(startupTimer);
    interaction.abort();
    if (animate) hero.classList.add('reveal-animated');
    hero.classList.remove('awaiting-reveal');
  }

  if (awaitingReveal) {
    hero.classList.add('awaiting-reveal');
    const options = { signal: interaction.signal, passive: true };
    for (const event of ['scroll', 'keydown', 'focusin']) {
      window.addEventListener(event, () => reveal(), options);
    }
    for (const event of ['mousemove', 'touchstart']) {
      hero.addEventListener(event, () => reveal(), options);
    }
    startupTimer = setTimeout(reveal, 1500);
    revealTimer = setTimeout(() => reveal(true), 3000);
  }

  function resetSound() {
    cancelAnimationFrame(fade);
    wantsSound = false;
    video.muted = true;
    if (gain) gain.gain.value = 0;
    sound.setAttribute('aria-pressed', 'false');
    sound.setAttribute('aria-label', enableLabel);
  }

  video.volume = 0.35;
  const supportsVolume = video.volume === 0.35;
  video.volume = 0;
  sound.hidden = !supportsVolume && !(window.AudioContext || window.webkitAudioContext);

  sound.addEventListener('click', () => {
    reveal();
    if (reducedMotion.matches || blocked) return;
    cancelAnimationFrame(fade);
    wantsSound = !wantsSound;
    sound.setAttribute('aria-pressed', String(wantsSound));
    sound.setAttribute('aria-label', wantsSound ? sound.dataset.soundOff : enableLabel);

    if (!supportsVolume && !gain) {
      try {
        const Audio = window.AudioContext || window.webkitAudioContext;
        context = new Audio();
        gain = context.createGain();
        gain.gain.value = 0;
        context.createMediaElementSource(video).connect(gain).connect(context.destination);
      } catch {
        resetSound();
        return;
      }
    }

    if (wantsSound) {
      if (context) context.resume().catch(resetSound);
      video.muted = false;
      if (video.paused) updatePlayback();
    }
    const start = gain ? gain.gain.value : video.volume;
    const end = wantsSound ? 0.35 : 0;
    const duration = wantsSound ? 1500 : 600;
    const started = performance.now();

    function step(now) {
      const progress = Math.min(1, (now - started) / duration);
      const level = start + (end - start) * progress;
      if (gain) gain.gain.value = level;
      else video.volume = level;
      if (progress < 1) fade = requestAnimationFrame(step);
      else if (!wantsSound) video.muted = true;
    }

    fade = requestAnimationFrame(step);
  });

  video.addEventListener('playing', () => {
    clearTimeout(startupTimer);
    video.classList.add('is-playing');
  });

  function updatePlayback() {
    if (!inView || document.hidden || reducedMotion.matches) {
      video.pause();
      return;
    }
    if (starting || blocked || !video.paused) return;

    if (!video.firstElementChild) {
      const files = matchMedia('(max-width: 768px)').matches
        ? [['hero-villa-mobile-sound.mp4', 'video/mp4']]
        : [['hero-villa-sound.webm', 'video/webm'], ['hero-villa-sound.mp4', 'video/mp4']];

      for (const [file, type] of files) {
        const source = document.createElement('source');
        source.src = new URL(file, assetRoot);
        source.type = type;
        video.append(source);
      }
    }

    starting = true;
    video.play().catch(error => {
      if (error.name === 'AbortError') return;
      if (wantsSound) {
        resetSound();
        return;
      }
      blocked = true;
      sound.hidden = true;
      video.classList.remove('is-playing');
      reveal();
    }).finally(() => {
      starting = false;
    });
  }

  new IntersectionObserver(([entry]) => {
    inView = entry.isIntersecting;
    updatePlayback();
  }).observe(hero);

  reducedMotion.addEventListener('change', () => {
    if (reducedMotion.matches) {
      reveal();
      resetSound();
    }
    updatePlayback();
  });
  document.addEventListener('visibilitychange', updatePlayback);
})();
