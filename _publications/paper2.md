---
title: "JIGS: A Modular Parallel Encryption and Authentication Pipeline for Secure Messaging"
collection: publications
category: manuscripts
permalink: /publication/2025-00-00-jigs-crypto
excerpt: 'This study presents JIGS, a hybrid secure messaging architecture designed to balance security and efficiency.'
date: 2025-06-04
venue: 'Engineering Research Express 7(2), 025276'
authors: '<b>G. Kulathumani</b>, S. V. Madangarli, J. Ullas, I. Agarwal, et al.'
paperurl: 'https://iopscience.iop.org/article/10.1088/2631-8695/addd67/pdf'
codeurl: 'https://github.com/Girish-K01/jigs-crypto-code-repo'
doiurl: 'https://doi.org/10.1088/2631-8695/addd67'
bibtexurl: '/files/bib/kulathumani2025jigs.bib'
scholar:  # Google Scholar citation tags; metadata as recorded by Crossref
  title: 'JIGS: a modular parallel encryption and authentication pipeline for secure messaging'
  authors: ['Kulathumani, Girish', 'Madangarli, Smriti Vipin', 'Ullas, Jeshma', 'Agarwal, Ishita', 'L, Mary Shamala']
  journal: 'Engineering Research Express'
  volume: 7
  issue: 2
  firstpage: '025276'
  publisher: 'IOP Publishing'
  doi: '10.1088/2631-8695/addd67'
  pdf_url: 'https://iopscience.iop.org/article/10.1088/2631-8695/addd67/pdf'
citation: 'Kulathumani, G., Madangarli, S. V., Ullas, J., Agarwal, I., et al. (2025). &quot;JIGS: a modular parallel encryption and authentication pipeline for secure messaging.&quot; <i>Engineering Research Express</i>, 7(2), 025276. doi:10.1088/2631-8695/addd67'
---

JIGS integrates Elliptic Curve Diffie-Hellman (ECDH) key exchanges with nonce-based AES-128 encryption, providing forward secrecy and key authentication. Its modular design enables adaptation across diverse implementation scenarios, and Python-based prototyping facilitates rapid performance optimization.

Experimental results indicate a processing speed improvement of up to 96.67% through parallelization, particularly for handling larger data sizes. A security analysis further validates the architecture's resilience against common attack vectors while also acknowledging the inherent trade-offs between computational efficiency and cryptographic strength.

The implementation code is available in the [jigs-crypto-code-repo](https://github.com/Girish-K01/jigs-crypto-code-repo) GitHub repository, and the paper is [open on IOPscience](https://iopscience.iop.org/article/10.1088/2631-8695/addd67).