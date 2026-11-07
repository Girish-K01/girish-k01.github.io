---
permalink: /
title: "About Me"
excerpt: "Researcher in non-invasive biosignal decoding (EEG and wrist EMG), federated learning and leakage-free evaluation."
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---
<link rel="stylesheet" href="{{ base_path }}/assets/css/about-style.css">

<div class="profile-header">
  <h1>Hi, I’m <span class="highlight-text">Girish Kulathumani</span></h1>
  <p class="lead-paragraph">
    I work on <span class="highlight-text">decoding non-invasive biosignals</span>, EEG and wrist surface EMG, so that models trained on some people work on new ones with little or no calibration.
    I’m also interested in personalising shared models with federated learning without pooling anyone’s data, and in evaluating them with subject-wise splits that rule out data leakage.
  </p>
</div>

## What I Focus On
- **Cross-subject biosignal decoding** — EEG and wrist surface EMG models that work on new people with little or no calibration. I’m currently an independent entrant in the NeurIPS 2026 EEG/EMG Foundation Challenge (Track 2, EEG decoding), with a covariance-based decoder (Riemannian tangent space with logistic regression) evaluated on held-out participants.
- **Federated learning** — personalising shared models without pooling each person’s data. At VIT Chennai I led HabitatFL, a federated framework for classifying wildlife audio and images, built with Flower and Docker on the university’s NVIDIA DGX; its edge models (under 2 MB) reached 87.65% accuracy on audio and 69.92% on images.
- **Leakage-free evaluation** — subject-wise splits that rule out data leakage.

## Recent Highlights
- Two peer-reviewed papers: [JIGS](/publication/2025-00-00-jigs-crypto) in *Engineering Research Express* (2025), a parallelised ECDH and AES-128 secure-messaging pipeline verified in ProVerif, and [Siren](/publication/2024-06-10-siren-cybersecurity) in Springer LNNS (2025), a deception-based cyber defence
- Application Engineer at Accenture (Oct 2025 – Oct 2026): built Salesforce Life Sciences Cloud features for a global pharmaceutical client, and evaluated GitHub Copilot on real user stories (over 80% average time savings), which fed into the licence decision
- Founder and writer of [GreyLattice](https://greylattice.substack.com) (since Feb 2025): around ten posts on brain–computer interfaces and computational neuroscience
- GPU-accelerated financial news sentiment with Kafka, FinBERT and RAPIDS cuDF: end-to-end latency cut from about 8 minutes to 10 seconds
- Talk: introduction to CUDA programming, VIT Chennai (50+ attendees)
- B.Tech. in Computer Science and Engineering, VIT Chennai (2021–2025), CGPA 8.69/10

## Open To
- Research collaborations in EEG/EMG decoding, federated learning, or computational neuroscience
- Internships with labs/companies advancing AI systems, BCI, or edge computing
- Projects at the boundary of **engineering and research**
