# ED Visa 90-Day Reporting Modal Template

## Files to Update
1. muay-thai-ed-visa-chiang-mai.html (already has button, needs modal)
2. emergency-self-defence-ed-visa-chiang-mai.html (add button + modal)
3. hand-to-hand-combat-ed-visa-chiang-mai.html (add button + modal)
4. thai-language-ed-visa-chiang-mai.html (add button + modal)
5. volunteer-non-o-visa-chiang-mai.html (add button + modal)
6. ed-visa-comparison-chiang-mai.html (add button + modal)
7. index.html (add button + modal)

---

## PART 1: INLINE BUTTON (to add next to "90-day reporting" text)

```html
<button id="open90DayReminder" style="background: #4F46E5; color: white; padding: 0.35em 0.8em; border: none; border-radius: 6px; font-weight: 600; cursor: pointer; font-size: 0.85rem; transition: background 0.2s;">Set Deadline Reminder</button>
```

**Important:** Button ID should be:
- `open90DayReminder` for pages with single 90-day mention
- If page has multiple 90-day sections, use unique IDs (e.g., `open90DayReminder1`, `open90DayReminder2`)

**Placement:** Immediately after the "90-day reporting" text in the context where it's most relevant:
```html
<li><strong>90-day reporting:</strong> Required every 90 days. File form TM.47... <button id="open90DayReminder" style="...">Set Deadline Reminder</button></li>
```

---

## PART 2: CSS (add to <style> section in <head>)

```css
/* ============================================================
   PRO TIP MODAL (90-Day Reporting)
   ============================================================ */
.pro-tip-modal {
  display: none;
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.5);
  z-index: 1000;
  align-items: center;
  justify-content: center;
  backdrop-filter: blur(4px);
  -webkit-backdrop-filter: blur(4px);
  animation: fadeInModal 0.3s ease-out;
}

.pro-tip-modal.active {
  display: flex;
}

.pro-tip-modal-content {
  background: white;
  border-radius: 12px;
  padding: 2rem;
  max-width: 500px;
  width: 90%;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
}

.pro-tip-modal-title {
  margin: 0 0 1rem 0;
  font-size: 1.3rem;
  font-weight: 700;
  color: var(--c-body);
  font-family: var(--font-body);
}

.pro-tip-modal-text {
  margin: 0 0 1.5rem 0;
  font-size: 0.95rem;
  line-height: 1.6;
  color: var(--c-muted);
}

.pro-tip-date-input-group {
  margin: 1.5rem 0;
  display: flex;
  gap: 0.8rem;
  align-items: center;
  flex-wrap: wrap;
}

.pro-tip-date-input {
  padding: 0.6rem 0.8rem;
  border: 1px solid rgba(99, 102, 241, 0.3);
  border-radius: 6px;
  font-size: 0.9rem;
  font-family: var(--font-body);
  width: 120px;
  transition: border-color 0.3s ease;
}

.pro-tip-date-input:focus {
  outline: none;
  border-color: #6366F1;
}

.pro-tip-modal-buttons {
  display: flex;
  gap: 0.8rem;
  flex-direction: column;
  margin-top: 1.5rem;
}

.pro-tip-modal-buttons button {
  padding: 0.8rem 1.2rem;
  border: none;
  border-radius: 6px;
  font-size: 0.95rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  font-family: var(--font-body);
}

.pro-tip-modal-buttons .btn-primary {
  background: linear-gradient(135deg, #6366F1 0%, #7C3AED 100%);
  color: white;
}

.pro-tip-modal-buttons .btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(99, 102, 241, 0.3);
}

.pro-tip-modal-buttons .btn-secondary {
  background: white;
  color: var(--c-body);
  border: 1px solid rgba(99, 102, 241, 0.3);
}

.pro-tip-modal-buttons .btn-secondary:hover {
  background: rgba(99, 102, 241, 0.05);
}

.pro-tip-modal-buttons .btn-cancel {
  background: transparent;
  color: var(--c-muted);
  border: none;
}

.pro-tip-modal-buttons .btn-cancel:hover {
  color: var(--c-body);
}

@keyframes fadeInModal {
  from {
    opacity: 0;
    transform: scale(0.95);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}
```

---

## PART 3: MODAL HTML (add before closing </article> tag)

```html
<!-- 90-Day Reporting Reminder Modal -->
<div id="proTipCalendarModal" class="pro-tip-modal">
  <div class="pro-tip-modal-content">
    <h3 class="pro-tip-modal-title">Add 90-Day Deadline to Calendar</h3>
    <p class="pro-tip-modal-text">File between 14 days BEFORE your 90-day deadline and 7 days AFTER to avoid a 2,000 THB fine.</p>
    <div class="pro-tip-date-input-group">
      <input type="text" id="proTipDateInput" placeholder="DD/MM/YYYY" class="pro-tip-date-input">
      <span style="font-size: 0.85rem; color: var(--c-muted);">Your entry date</span>
    </div>
    <div class="pro-tip-modal-buttons">
      <button class="btn-primary" id="proTipGoogleCalendar">Add to Google Calendar</button>
      <button class="btn-secondary" id="proTipDownloadIcs">Download .ics File</button>
      <button class="btn-cancel" id="proTipCancel">Cancel</button>
    </div>
  </div>
</div>
```

---

## PART 4: JAVASCRIPT (add as <script> block before </body>)

```javascript
<!-- 90-Day Reporting Deadline Reminder -->
<script>
document.addEventListener('DOMContentLoaded', function() {
  // Support multiple modals on same page (if needed)
  const buttonSelectors = ['#open90DayReminder', '#open90DayReminder1', '#open90DayReminder2'];
  let button = null;

  for (let selector of buttonSelectors) {
    let el = document.querySelector(selector);
    if (el) {
      button = el;
      break;
    }
  }

  const dateInput = document.getElementById('proTipDateInput');
  const submitBtn = button;
  const modal = document.getElementById('proTipCalendarModal');
  const googleCalendarBtn = document.getElementById('proTipGoogleCalendar');
  const downloadIcsBtn = document.getElementById('proTipDownloadIcs');
  const cancelBtn = document.getElementById('proTipCancel');

  let calculatedDate = null;

  if (submitBtn) {
    submitBtn.addEventListener('click', function() {
      const dateValue = dateInput.value.trim();

      // Validate DD/MM/YYYY format
      const dateRegex = /^(\d{2})\/(\d{2})\/(\d{4})$/;
      const match = dateValue.match(dateRegex);

      if (!match) {
        alert('Please enter date in DD/MM/YYYY format');
        return;
      }

      const [, day, month, year] = match;
      const entryDate = new Date(year, parseInt(month) - 1, parseInt(day));

      // Check if date is valid
      if (isNaN(entryDate.getTime())) {
        alert('Please enter a valid date');
        return;
      }

      // Check if date is in the future
      if (entryDate > new Date()) {
        alert('Please enter a past date (your entry date)');
        return;
      }

      // Calculate 90-day deadline
      const deadlineDate = new Date(entryDate);
      deadlineDate.setDate(deadlineDate.getDate() + 90);

      // Calculate filing window start (14 days before)
      const filingStart = new Date(deadlineDate);
      filingStart.setDate(filingStart.getDate() - 14);

      calculatedDate = { entry: entryDate, deadline: deadlineDate, filingStart: filingStart };

      // Show calendar selection modal
      modal.classList.add('active');
    });
  }

  googleCalendarBtn.addEventListener('click', function() {
    if (calculatedDate) {
      const filingStartStr = calculatedDate.filingStart.toISOString().split('T')[0].replace(/-/g, '');
      const deadlineStr = calculatedDate.deadline.toISOString().split('T')[0].replace(/-/g, '');

      const title = '90-Day Reporting Deadline - File Now';
      const description = 'Your 90-day reporting deadline is ' +
        calculatedDate.deadline.toLocaleDateString('en-GB') +
        '. File between now and 14 days before this date at Chiang Mai Immigration Office.\\n\\n' +
        'Location: 71 Moo 3 Airport Rd, Suthep, Chiang Mai\\n' +
        'Hours: Mon–Fri 8:30 AM–4:30 PM';

      const url = 'https://calendar.google.com/calendar/r/eventedit?' +
        'text=' + encodeURIComponent(title) +
        '&dates=' + filingStartStr + '/' + deadlineStr +
        '&details=' + encodeURIComponent(description) +
        '&location=' + encodeURIComponent('Chiang Mai Immigration Office');

      window.open(url, '_blank');
      modal.classList.remove('active');
      dateInput.value = '';
    }
  });

  downloadIcsBtn.addEventListener('click', function() {
    if (calculatedDate) {
      const icsContent = generateICS(calculatedDate);
      downloadICS(icsContent);
      modal.classList.remove('active');
      dateInput.value = '';
    }
  });

  cancelBtn.addEventListener('click', function() {
    modal.classList.remove('active');
  });

  modal.addEventListener('click', function(e) {
    if (e.target === modal) {
      modal.classList.remove('active');
    }
  });

  function generateICS(dateObj) {
    const uid = 'ninety-day-deadline-' + dateObj.deadline.getTime() + '@cmlocals.com';
    const startDate = formatDateForICS(dateObj.filingStart);
    const endDate = formatDateForICS(new Date(dateObj.deadline.getTime() + 86400000));

    return `BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//CMLocals//Thai Visa Calendar//EN
CALSCALE:GREGORIAN
METHOD:PUBLISH
BEGIN:VEVENT
 UID:${uid}
DTSTAMP:${formatDateForICS(new Date())}
DTSTART:${startDate}
DTEND:${endDate}
SUMMARY:90-Day Reporting Deadline - File Now
DESCRIPTION:Your 90-day reporting deadline is ${dateObj.deadline.toLocaleDateString('en-GB')}. You can file from now until 14 days before this date at Chiang Mai Immigration Office.\\n\\nLocation: 71 Moo 3 Airport Rd\\, Suthep\\, Chiang Mai\\nHours: Mon–Fri 8:30 AM–4:30 PM\\n\\nWhat you need: Original passport\\, TM.47 form (if filing in person)\\, proof of address (optional).
LOCATION:Chiang Mai Immigration Office
SEQUENCE:0
STATUS:CONFIRMED
TRANSP:OPAQUE
BEGIN:VALARM
TRIGGER:-P7D
ACTION:DISPLAY
DESCRIPTION:90-Day Report Due in 7 Days
END:VALARM
BEGIN:VALARM
TRIGGER:-P1D
ACTION:DISPLAY
DESCRIPTION:90-Day Report Due Tomorrow
END:VALARM
END:VEVENT
END:VCALENDAR`;
  }

  function formatDateForICS(date) {
    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, '0');
    const day = String(date.getDate()).padStart(2, '0');
    const hours = String(date.getHours()).padStart(2, '0');
    const minutes = String(date.getMinutes()).padStart(2, '0');
    const seconds = String(date.getSeconds()).padStart(2, '0');
    return `${year}${month}${day}T${hours}${minutes}${seconds}`;
  }

  function downloadICS(icsContent) {
    const blob = new Blob([icsContent], { type: 'text/calendar' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = '90-day-reporting-deadline.ics';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  }
});
</script>
```

---

## Implementation Notes

### Button Placement by File:

**✅ 1. muay-thai-ed-visa-chiang-mai.html** – ADD MODAL
- Line ~1291: Already has button with id="openReportingReminder"
- Change button ID to `id="open90DayReminder"` for consistency
- Add CSS + modal HTML + JavaScript

**❌ 2. emergency-self-defence-ed-visa-chiang-mai.html** – SKIP
- Line ~846: "90-day reporting handled by the school (not you)."
- No button needed (school files TM.47 on behalf of student)
- User does NOT file 90-day reporting

**❌ 3. hand-to-hand-combat-ed-visa-chiang-mai.html** – SKIP
- Line ~1239: "90-day reporting handled by the school (not you)."
- No button needed (school files TM.47 on behalf of student)
- User does NOT file 90-day reporting

**❌ 4. thai-language-ed-visa-chiang-mai.html** – SKIP
- Line ~1247: "90-day reporting handled by the school (not you)."
- No button needed (school files TM.47 on behalf of student)
- User does NOT file 90-day reporting

**❌ 5. volunteer-non-o-visa-chiang-mai.html** – SKIP
- No mention of 90-day reporting in content
- Volunteer visa structure (annual renewal vs 90-day cycles) is different
- 90-day reporting not user-facing requirement

**❌ 6. ed-visa-comparison-chiang-mai.html** – SKIP
- References "90-day renewals (at immigration)" for Thai Language ED visa
- These are visa renewal cycles (structure), NOT TM.47 filing requirements
- No explicit "you must file 90-day reporting" statement
- Not appropriate for modal

**❌ 7. index.html** – SKIP
- Line ~1207: Mentions 90-day reporting only in context of guide links
- No dedicated section explaining 90-day filing requirement
- Card labeled "Compliance & Reporting" links out to immigration guide
- Not appropriate for inline modal

### Key Rules:

1. **Only add modal to files with user-facing 90-day filing requirement** (user must file, not school)
2. **CSS must be added to <style> section** in <head> (before closing </head>)
3. **Modal HTML goes before </article>** closing tag
4. **JavaScript goes before </body>** closing tag
5. **Button ID must match JavaScript selector** (default: `open90DayReminder`)
6. **All three components (CSS, HTML, JS) must be present** or modal won't function
7. **Use consistent styling** with rest of page (indigo gradient buttons, white modal)

### Testing Checklist (for muay-thai-ed-visa-chiang-mai.html):

- [ ] Button appears inline with 90-day reporting text
- [ ] Button clickable and opens modal
- [ ] Modal displays with backdrop blur
- [ ] Modal allows DD/MM/YYYY date input (e.g., 15/03/2025)
- [ ] Submit button validates date format (rejects invalid formats with alert)
- [ ] Submit button validates past dates (rejects future dates with alert)
- [ ] Google Calendar button opens Google Calendar with:
  - Event title: "90-Day Reporting Deadline - File Now"
  - Start date: 14 days before 90-day deadline
  - End date: 7 days after 90-day deadline
  - Location: "Chiang Mai Immigration Office"
  - Description includes filing window info
- [ ] .ics button downloads file named "90-day-reporting-deadline.ics"
- [ ] .ics file includes:
  - VEVENT with correct DTSTART/DTEND dates
  - Two VALARM entries (7-day and 1-day reminders)
  - SUMMARY, LOCATION, DESCRIPTION fields populated
- [ ] Cancel button closes modal without action
- [ ] Clicking modal backdrop closes modal without action
- [ ] Date input clears after successful calendar action
- [ ] Modal styling matches site design (white box, gradient buttons, blur backdrop)
- [ ] CSS animations smooth (fadeInModal transition)
- [ ] Responsive on mobile (modal max-width 90% with 500px max)

---

## File Structure Summary

**Files that need modal added:**
- `/c/ZZZWebsites/cmlocals/pages/ed-visas/muay-thai-ed-visa-chiang-mai.html` (1 file)

**Files that should be skipped:**
- emergency-self-defence-ed-visa-chiang-mai.html
- hand-to-hand-combat-ed-visa-chiang-mai.html
- thai-language-ed-visa-chiang-mai.html
- volunteer-non-o-visa-chiang-mai.html
- ed-visa-comparison-chiang-mai.html
- index.html
