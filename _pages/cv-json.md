---
layout: archive
title: ""
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
  - /cv
---

{% include base_path %}

<!-- Load required CSS -->
<link rel="stylesheet" href="{{ base_path }}/assets/css/cv-style.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">

<div class="cv-download-links">
  <a href="{{ base_path }}/files/cv.pdf" class="cv-download-btn">
    <i class="fas fa-download"></i> Download Resume (PDF)
  </a>
</div>


<!-- CV Content -->
{% include cv-template.html %}