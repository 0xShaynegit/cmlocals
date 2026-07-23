/**
 * Visa Expiry Calendar Tool
 * Handles visa expiry date input and generates .ics calendar file
 */

document.addEventListener('DOMContentLoaded', function() {
  const visaDateForm = document.getElementById('visa-date-form');
  const visaExpiryInput = document.getElementById('visa-expiry-input');
  const proTipModal = document.getElementById('pro-tip-modal');
  const proTipButton = document.getElementById('pro-tip-bubble-btn');

  if (!visaDateForm || !visaExpiryInput) return;

  // Open modal when button clicked
  if (proTipButton) {
    proTipButton.addEventListener('click', function(e) {
      e.preventDefault();
      proTipModal.classList.add('active');
      visaExpiryInput.focus();
    });
  }

  // Auto-format input as user types (DD/MM/YYYY)
  visaExpiryInput.addEventListener('input', function(e) {
    let value = e.target.value.replace(/\D/g, '');
    if (value.length > 8) value = value.slice(0, 8);

    if (value.length >= 2) {
      value = value.slice(0, 2) + '/' + value.slice(2);
    }
    if (value.length >= 5) {
      value = value.slice(0, 5) + '/' + value.slice(5);
    }
    e.target.value = value;
  });

  // Parse DD/MM/YYYY and validate
  function parseDate(dateString) {
    const parts = dateString.trim().split('/');
    if (parts.length !== 3) return null;

    const day = parseInt(parts[0], 10);
    const month = parseInt(parts[1], 10);
    const year = parseInt(parts[2], 10);

    // Validate ranges
    if (day < 1 || day > 31 || month < 1 || month > 12 || year < 2000 || year > 2100) {
      return null;
    }

    // Check for valid day in month
    const daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

    // Handle leap years
    const isLeapYear = (year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0);
    if (isLeapYear) daysInMonth[1] = 29;

    if (day > daysInMonth[month - 1]) {
      return null;
    }

    return new Date(year, month - 1, day);
  }

  // Generate ICS file content
  function generateICS(expiryDate) {
    const now = new Date();
    const dateCreated = now.toISOString().replace(/[-:]/g, '').split('.')[0] + 'Z';

    // Format expiry date for .ics (YYYYMMDD)
    const expiryYear = expiryDate.getFullYear();
    const expiryMonth = String(expiryDate.getMonth() + 1).padStart(2, '0');
    const expiryDay = String(expiryDate.getDate()).padStart(2, '0');
    const expiryDateFormatted = `${expiryYear}${expiryMonth}${expiryDay}`;

    // Reminders: 7 days and 1 day before expiry
    const sevenDaysBefore = new Date(expiryDate);
    sevenDaysBefore.setDate(sevenDaysBefore.getDate() - 7);
    const sevenDaysBeforeFormatted = sevenDaysBefore.toISOString().replace(/[-:]/g, '').split('.')[0] + 'Z';

    const oneDayBefore = new Date(expiryDate);
    oneDayBefore.setDate(oneDayBefore.getDate() - 1);
    const oneDayBeforeFormatted = oneDayBefore.toISOString().replace(/[-:]/g, '').split('.')[0] + 'Z';

    const icsContent = `BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//CMLocals//Visa Expiry Tracker//EN
CALSCALE:GREGORIAN
METHOD:PUBLISH
X-WR-CALNAME:CMLocals Visa Calendar
X-WR-TIMEZONE:UTC
BEGIN:VEVENT
UID:cmlocals-visa-expiry-${expiryYear}-${expiryMonth}-${expiryDay}@cmlocals.com
DTSTAMP:${dateCreated}
CREATED:${dateCreated}
LAST-MODIFIED:${dateCreated}
DTSTART:${expiryDateFormatted}
DTEND:${expiryDateFormatted}
SUMMARY:Thai Visa Expires
DESCRIPTION:Your Thai visa expires on ${expiryDay}/${expiryMonth}/${expiryYear}. Ensure you arrange your extension or renewal before this date.
LOCATION:Thailand
STATUS:CONFIRMED
TRANSP:OPAQUE
BEGIN:VALARM
TRIGGER:-P7D
ACTION:DISPLAY
DESCRIPTION:Your Thai visa expires in 7 days
END:VALARM
BEGIN:VALARM
TRIGGER:-P1D
ACTION:DISPLAY
DESCRIPTION:Your Thai visa expires tomorrow
END:VALARM
END:VEVENT
END:VCALENDAR`;

    return icsContent;
  }

  // Handle form submission
  visaDateForm.addEventListener('submit', function(e) {
    e.preventDefault();

    const dateString = visaExpiryInput.value.trim();
    const expiryDate = parseDate(dateString);

    if (!expiryDate) {
      visaExpiryInput.style.borderColor = '#DC2626';
      visaExpiryInput.setAttribute('aria-invalid', 'true');
      setTimeout(() => {
        visaExpiryInput.style.borderColor = 'rgba(255,255,255,.5)';
        visaExpiryInput.setAttribute('aria-invalid', 'false');
      }, 2000);
      return;
    }

    // Generate .ics content
    const icsContent = generateICS(expiryDate);

    // Create blob and download
    const blob = new Blob([icsContent], { type: 'text/calendar' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = `cmlocals-visa-expiry-${expiryDate.getFullYear()}-${String(expiryDate.getMonth() + 1).padStart(2, '0')}-${String(expiryDate.getDate()).padStart(2, '0')}.ics`;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(url);

    // Clear form and show success
    visaExpiryInput.value = '';
    visaExpiryInput.style.borderColor = '#22c55e';
    setTimeout(() => {
      visaExpiryInput.style.borderColor = 'rgba(255,255,255,.5)';
      proTipModal.classList.remove('active');
    }, 1500);
  });

  // Close modal on × button
  const closeButton = proTipModal.querySelector('.pro-tip-modal-close');
  if (closeButton) {
    closeButton.addEventListener('click', function() {
      proTipModal.classList.remove('active');
    });
  }

  // Close modal on outside click
  proTipModal.addEventListener('click', function(e) {
    if (e.target === proTipModal) {
      proTipModal.classList.remove('active');
    }
  });
});
