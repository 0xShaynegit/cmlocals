# Chaty Widget – Shared Installation

A configurable floating contact widget for all C:\ZZZWebsites projects.

## Features

- ✨ Floating chat/contact button in bottom-left corner
- 🎯 Smart tooltips: "Contact Us" in bottom-left 30% of screen, channel labels on hover
- 📱 Responsive: 40px on mobile, 54px on desktop
- ⚡ Lightweight, vanilla JavaScript (no dependencies)
- 🎨 Fully customizable: channels, colors, positioning

## Quick Start

### 1. Add to your HTML (before `</body>`):

```html
<!-- Chaty Widget Configuration -->
<script>
  window.CHATY_CONFIG = {
    channels: [
      {
        name: "Facebook_Messenger",
        label: "Facebook Messenger",
        url: "https://m.me/YOUR_PAGE",
        svg: '<svg>...</svg>'  // Copy from SETUP.md
      },
      {
        name: "WhatsApp",
        label: "WhatsApp",
        url: "https://wa.me/YOUR_NUMBER",
        svg: '<svg>...</svg>'
      }
    ],
    triggerColor: "#9F7AEA"  // Optional
  };
</script>

<!-- Load widget from shared location -->
<script src="../shared/chaty-widget/scripts/chaty-widget.js"></script>
```

### 2. Update paths based on your site's depth:

- Direct child: `../shared/chaty-widget/scripts/chaty-widget.js`
- Nested site: `../../shared/chaty-widget/scripts/chaty-widget.js`

## Configuration

See [SETUP.md](./SETUP.md) for complete configuration options and examples.

## Current Installations

- ✅ CMLocals – https://cmlocals.com
- Ken Brown FC (ready to integrate)

## File Structure

```
C:\ZZZWebsites\
├── shared\
│   └── chaty-widget\
│       ├── scripts\
│       │   └── chaty-widget.js    (shared widget code)
│       ├── README.md              (this file)
│       └── SETUP.md               (detailed setup guide)
├── cmlocals\
│   ├── index.html                 (uses shared widget)
│   └── scripts\
│       └── (local scripts)
└── kenbrownfc\
    └── index.html                 (ready to add widget)
```

## Support

All sites reference the same `chaty-widget.js`, so updates apply to all sites automatically. Each site controls its own configuration via `window.CHATY_CONFIG`.
