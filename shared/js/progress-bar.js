/* ============================================================
   READING PROGRESS BAR
   Tracks scroll position and updates progress indicator
   ============================================================ */

(function() {
  const progressBar = document.getElementById('progress-bar');

  if (!progressBar) return;

  function updateProgress() {
    const windowHeight = window.innerHeight;
    const documentHeight = document.documentElement.scrollHeight - windowHeight;
    const scrolled = window.scrollY;
    const progress = documentHeight > 0 ? (scrolled / documentHeight) * 100 : 0;

    progressBar.style.width = progress + '%';
    progressBar.setAttribute('aria-valuenow', Math.round(progress));
  }

  // Update on scroll
  window.addEventListener('scroll', updateProgress, { passive: true });

  // Initial call
  updateProgress();
})();
