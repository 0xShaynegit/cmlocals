# Chaty Widget – Setup Guide

The Chaty widget is a floating contact menu for all your C:\ZZZWebsites projects. It's centralized and easy to configure per site.

## Installation

### 1. In Your HTML (before closing `</body>` tag):

```html
<!-- Configure Chaty for this site -->
<script>
  window.CHATY_CONFIG = {
    channels: [
      {
        name: "Facebook_Messenger",
        label: "Facebook Messenger",
        url: "https://m.me/YOUR_PAGE_NAME",
        svg: '<svg viewBox="0 0 39 39" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="19.4395" cy="19.4395" r="19.4395" fill="#0084FF"/><path d="M19.5 9.5C13.701 9.5 9 13.748 9 19.074c0 3.014 1.474 5.702 3.778 7.456V30l3.294-1.81c.878.244 1.81.376 2.778.376 5.799 0 10.5-4.248 10.5-9.574S25.299 9.5 19.5 9.5zm1.04 12.878l-2.674-2.852-5.22 2.852 5.74-6.096 2.74 2.852 5.154-2.852-5.74 6.096z" fill="white"/></svg>'
      },
      {
        name: "WhatsApp",
        label: "WhatsApp",
        url: "https://wa.me/YOUR_PHONE_NUMBER",
        svg: '<svg viewBox="0 0 39 39" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="19.4395" cy="19.4395" r="19.4395" fill="#25D366"/><path d="M19.5 9.5C14.253 9.5 10 13.753 10 19c0 1.67.436 3.285 1.265 4.717L10 29l5.418-1.234A9.454 9.454 0 0019.5 28.5c5.247 0 9.5-4.253 9.5-9.5s-4.253-9.5-9.5-9.5zm5.508 13.142c-.232.652-1.345 1.247-1.853 1.29-.508.043-.982.228-3.306-.688-2.806-1.107-4.573-3.974-4.71-4.16-.137-.186-1.12-1.49-1.12-2.843 0-1.352.71-2.018.96-2.293.25-.275.546-.344.728-.344.183 0 .365.002.525.01.168.007.394-.064.617.47.232.556.786 1.92.855 2.06.069.138.115.3.023.485-.093.186-.139.3-.275.462-.137.162-.288.362-.412.486-.137.137-.28.286-.12.56.16.275.71 1.173 1.525 1.9 1.047.933 1.93 1.222 2.205 1.36.275.137.435.115.595-.069.16-.185.686-.8.869-1.075.183-.275.365-.228.617-.137.25.092 1.595.752 1.868.889.275.137.457.206.526.32.068.115.068.663-.164 1.315z" fill="white"/></svg>'
      }
    ],
    triggerColor: "#9F7AEA",  // Optional: customize button color
    bottomOffset: 50,         // Optional: distance from bottom (px)
    leftOffset: 20            // Optional: distance from left (px)
  };
</script>

<!-- Load the widget -->
<script src="../shared/chaty-widget/scripts/chaty-widget.js"></script>
```

## Configuration

All options are optional. The widget has sensible defaults.

```javascript
window.CHATY_CONFIG = {
  // Override the default channels
  channels: [
    {
      name: "Facebook_Messenger",
      label: "Facebook Messenger",
      url: "https://m.me/YOUR_PAGE",
      svg: "..."  // SVG icon string
    },
    {
      name: "WhatsApp",
      label: "WhatsApp",
      url: "https://wa.me/YOUR_NUMBER",
      svg: "..."
    }
  ],

  // Button color (default: "#9F7AEA")
  triggerColor: "#9F7AEA",

  // Position from bottom of screen in pixels (default: 50)
  bottomOffset: 50,

  // Position from left of screen in pixels (default: 20)
  leftOffset: 20
};
```

## Behavior

- **"Contact Us"** tooltip appears when mouse moves to bottom-left 30% of screen
- **Channel tooltips** appear when hovering over their icons
- Hover over trigger button to open the widget
- Widget auto-closes after 30 seconds
- Click trigger button to close anytime
- Responsive: 40px icons on mobile (≤480px), 54px on desktop

## Examples

### CMLocals
```javascript
window.CHATY_CONFIG = {
  channels: [
    {
      name: "Facebook_Messenger",
      label: "Facebook Messenger",
      url: "https://m.me/cmlocals",
      svg: '<svg>...</svg>'
    },
    {
      name: "WhatsApp",
      label: "WhatsApp",
      url: "https://wa.me/66801202074",
      svg: '<svg>...</svg>'
    }
  ]
};
```

### Ken Brown FC
```javascript
window.CHATY_CONFIG = {
  channels: [
    {
      name: "Facebook_Messenger",
      label: "Facebook Messenger",
      url: "https://m.me/kenbrownfc",
      svg: '<svg>...</svg>'
    },
    {
      name: "WhatsApp",
      label: "WhatsApp",
      url: "https://wa.me/66910571270",
      svg: '<svg>...</svg>'
    },
    {
      name: "Phone",
      label: "Phone: +66 91 057 1270",
      url: "tel:+66910571270",
      svg: '<svg>...</svg>'
    },
    {
      name: "LinkedIn",
      label: "LinkedIn",
      url: "https://www.linkedin.com/in/ken-brown-59438192/",
      svg: '<svg>...</svg>'
    }
  ],
  triggerColor: "#000000"
};
```

## Path Reference

From any C:\ZZZWebsites\{sitename}\ directory:
```
../shared/chaty-widget/scripts/chaty-widget.js
```

Adjust `../` based on your site's folder depth.
