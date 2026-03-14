/**
 * Make entire cards clickable
 * Converts card containers into full clickable zones
 */
document.addEventListener('DOMContentLoaded', function() {
  var cardSelectors = [
    '.path-card',
    '.article-card',
    '.tool-card',
    '.guide-card',
    '.visa-card',
    '.visa-category-card',
    '.program-card',
    '.topic-card',
    '.checklist-card',
    '.related-card',
    '.sidebar-card'
  ];

  cardSelectors.forEach(function(selector) {
    document.querySelectorAll(selector).forEach(function(card) {
      // Find the CTA link within the card
      // First try __cta/__link pattern, then fall back to first link in card
      var cta = card.querySelector('[class*="__cta"], [class*="__link"]') || card.querySelector('a');
      if (!cta || !cta.href) return;

      var link = cta.href;
      var target = cta.target || '_self';
      var rel = cta.rel || '';

      card.style.cursor = 'pointer';

      card.addEventListener('click', function(e) {
        // Check if user clicked on an interactive element (link or button)
        var clickedInteractive = e.target.closest('a, button');

        // Only allow clicks that don't target interactive elements, OR target the main CTA
        if (clickedInteractive && clickedInteractive !== cta) {
          // Allow the default behavior for non-CTA links
          return;
        }

        // For the CTA or empty card areas, navigate
        e.preventDefault();
        if (target === '_blank') {
          window.open(link, '_blank', rel);
        } else {
          window.location.href = link;
        }
      });
    });
  });
});
