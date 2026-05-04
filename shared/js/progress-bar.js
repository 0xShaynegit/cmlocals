/* ============================================================
   READING PROGRESS BAR
   Tracks scroll position and updates progress indicator
   ============================================================ */

(function() {
  const progressBar = document.getElementById('progress-bar');

  if (!progressBar) return;

  let windowHeight = window.innerHeight;
  let documentHeight = document.documentElement.scrollHeight - windowHeight;

  function updateProgress() {
    const scrolled = window.scrollY;
    const progress = documentHeight > 0 ? (scrolled / documentHeight) * 100 : 0;
    progressBar.style.width = progress + '%';
    progressBar.setAttribute('aria-valuenow', Math.round(progress));
  }

  function updateDimensions() {
    windowHeight = window.innerHeight;
    documentHeight = document.documentElement.scrollHeight - windowHeight;
  }

  window.addEventListener('scroll', updateProgress, { passive: true });
  window.addEventListener('resize', updateDimensions, { passive: true });

  updateDimensions();
  updateProgress();
})();
