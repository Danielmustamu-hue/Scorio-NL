/* ============================================================
   Scorio.nl — Main JavaScript
   ============================================================ */

(function () {
  'use strict';

  /* ----------------------------------------------------------
     Sticky Header
  ---------------------------------------------------------- */
  const header = document.querySelector('.site-header');
  if (header) {
    const onScroll = () => {
      header.classList.toggle('scrolled', window.scrollY > 40);
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  /* ----------------------------------------------------------
     Mobile Menu
  ---------------------------------------------------------- */
  const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
  const closeBtn = document.querySelector('.mobile-close-btn');

  if (mobileMenuBtn) {
    mobileMenuBtn.addEventListener('click', () => {
      document.body.classList.add('mobile-nav-open');
    });
  }

  if (closeBtn) {
    closeBtn.addEventListener('click', () => {
      document.body.classList.remove('mobile-nav-open');
    });
  }

  // Close on nav link click
  document.querySelectorAll('.nav-links a').forEach(link => {
    link.addEventListener('click', () => {
      document.body.classList.remove('mobile-nav-open');
    });
  });

  /* ----------------------------------------------------------
     FAQ Accordion
  ---------------------------------------------------------- */
  document.querySelectorAll('.faq-item').forEach(item => {
    const question = item.querySelector('.faq-question');
    const answer = item.querySelector('.faq-answer');

    if (!question || !answer) return;

    question.addEventListener('click', () => {
      const isActive = item.classList.contains('active');

      // Close all
      document.querySelectorAll('.faq-item').forEach(other => {
        other.classList.remove('active');
        const otherAnswer = other.querySelector('.faq-answer');
        if (otherAnswer) otherAnswer.style.maxHeight = null;
      });

      // Open clicked
      if (!isActive) {
        item.classList.add('active');
        answer.style.maxHeight = answer.scrollHeight + 'px';
      }
    });
  });

  /* ----------------------------------------------------------
     Pricing Toggle
  ---------------------------------------------------------- */
  const pricingToggle = document.querySelector('#pricing-toggle');
  const monthlyLabel = document.querySelector('.toggle-monthly');
  const yearlyLabel = document.querySelector('.toggle-yearly');

  const prices = {
    free:    { monthly: '0',  yearly: '0'  },
    starter: { monthly: '9',  yearly: '7'  },
    pro:     { monthly: '29', yearly: '24' },
    agency:  { monthly: '79', yearly: '66' },
  };

  const yearlyNotes = {
    free:    '',
    starter: 'Bespaar €24/jaar',
    pro:     'Bespaar €60/jaar',
    agency:  'Bespaar €156/jaar',
  };

  function updatePricing(isYearly) {
    if (monthlyLabel) monthlyLabel.classList.toggle('active', !isYearly);
    if (yearlyLabel) yearlyLabel.classList.toggle('active', isYearly);

    Object.keys(prices).forEach(plan => {
      const amountEl = document.querySelector(`[data-plan="${plan}"] .price-amount`);
      const noteEl = document.querySelector(`[data-plan="${plan}"] .price-yearly`);

      if (amountEl) {
        amountEl.textContent = '€' + (isYearly ? prices[plan].yearly : prices[plan].monthly);
      }
      if (noteEl) {
        noteEl.textContent = isYearly ? yearlyNotes[plan] : '';
      }
    });
  }

  if (pricingToggle) {
    pricingToggle.addEventListener('change', () => {
      updatePricing(pricingToggle.checked);
    });
    updatePricing(false);
  }

  /* ----------------------------------------------------------
     Score Ring Animation
  ---------------------------------------------------------- */
  function animateScore() {
    const ring = document.querySelector('.ring-progress');
    const scoreNumber = document.querySelector('.score-number');
    const metricFills = document.querySelectorAll('.metric-fill');

    if (ring) {
      setTimeout(() => {
        ring.classList.add('animated');
      }, 300);
    }

    if (scoreNumber) {
      const target = parseInt(scoreNumber.dataset.target || '74', 10);
      let current = 0;
      const duration = 1800;
      const start = performance.now();

      const tick = (now) => {
        const elapsed = now - start;
        const progress = Math.min(elapsed / duration, 1);
        const ease = 1 - Math.pow(1 - progress, 3);
        current = Math.round(ease * target);
        scoreNumber.textContent = current;
        if (progress < 1) requestAnimationFrame(tick);
      };

      setTimeout(() => requestAnimationFrame(tick), 300);
    }

    metricFills.forEach(fill => {
      setTimeout(() => fill.classList.add('animated'), 500);
    });
  }

  animateScore();

  /* ----------------------------------------------------------
     IntersectionObserver — Fade-up animations
  ---------------------------------------------------------- */
  const fadeEls = document.querySelectorAll('.fade-up');

  if ('IntersectionObserver' in window && fadeEls.length) {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.15, rootMargin: '0px 0px -40px 0px' }
    );

    fadeEls.forEach(el => observer.observe(el));
  } else {
    // Fallback: show all
    fadeEls.forEach(el => el.classList.add('visible'));
  }

  /* ----------------------------------------------------------
     URL Scanner — hero & CTA forms
  ---------------------------------------------------------- */
  const scanForms = document.querySelectorAll('.scan-form');
  const modal = document.querySelector('.scan-modal-overlay');
  const progressFill = document.querySelector('.scan-progress-fill');
  const scanUrl = document.querySelector('.scan-modal-url');

  function validateUrl(value) {
    if (!value) return false;
    try {
      const url = new URL(value.startsWith('http') ? value : 'https://' + value);
      return url.hostname.includes('.');
    } catch {
      return false;
    }
  }

  function openScanModal(url) {
    if (!modal) return;
    if (scanUrl) scanUrl.textContent = url;
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';

    let progress = 0;
    const interval = setInterval(() => {
      progress += Math.random() * 12 + 3;
      if (progress >= 95) {
        progress = 95;
        clearInterval(interval);
      }
      if (progressFill) progressFill.style.width = progress + '%';
    }, 220);

    // Simulate completion after 3.5s
    setTimeout(() => {
      clearInterval(interval);
      if (progressFill) progressFill.style.width = '100%';
      setTimeout(() => {
        if (modal) modal.classList.remove('active');
        document.body.style.overflow = '';
        if (progressFill) progressFill.style.width = '0%';
      }, 600);
    }, 3500);
  }

  if (modal) {
    modal.addEventListener('click', (e) => {
      if (e.target === modal) {
        modal.classList.remove('active');
        document.body.style.overflow = '';
      }
    });
  }

  scanForms.forEach(form => {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const input = form.querySelector('.hero-input');
      if (!input) return;

      const rawValue = input.value.trim();
      if (!validateUrl(rawValue)) {
        input.style.borderColor = '#ef4444';
        input.style.boxShadow = '0 0 0 3px rgba(239, 68, 68, 0.15)';
        input.focus();
        setTimeout(() => {
          input.style.borderColor = '';
          input.style.boxShadow = '';
        }, 2000);
        return;
      }

      const cleanUrl = rawValue.startsWith('http') ? rawValue : 'https://' + rawValue;
      openScanModal(cleanUrl);
    });
  });

  /* ----------------------------------------------------------
     Smooth Scroll for anchor links
  ---------------------------------------------------------- */
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', (e) => {
      const id = anchor.getAttribute('href').slice(1);
      const target = document.getElementById(id);
      if (target) {
        e.preventDefault();
        const headerH = header ? header.offsetHeight : 0;
        const top = target.getBoundingClientRect().top + window.scrollY - headerH - 24;
        window.scrollTo({ top, behavior: 'smooth' });
      }
    });
  });

  /* ----------------------------------------------------------
     Stat counters — "Waarom SEO" sectie
  ---------------------------------------------------------- */
  function animateCounter(el) {
    const target = parseInt(el.dataset.target, 10);
    const suffix = el.dataset.suffix || '';
    const duration = 1600;
    const startTime = performance.now();

    const tick = (now) => {
      const elapsed = now - startTime;
      const progress = Math.min(elapsed / duration, 1);
      const ease = 1 - Math.pow(1 - progress, 3);
      el.textContent = Math.round(ease * target) + suffix;
      if (progress < 1) requestAnimationFrame(tick);
    };

    requestAnimationFrame(tick);
  }

  const counterEls = document.querySelectorAll('.why-stat-number[data-target]');
  if (counterEls.length && 'IntersectionObserver' in window) {
    const counterObserver = new IntersectionObserver(
      (entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            animateCounter(entry.target);
            counterObserver.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.6 }
    );
    counterEls.forEach(el => counterObserver.observe(el));
  } else {
    counterEls.forEach(el => {
      el.textContent = el.dataset.target + (el.dataset.suffix || '');
    });
  }

  /* ----------------------------------------------------------
     Active nav highlighting
  ---------------------------------------------------------- */
  const navLinks = document.querySelectorAll('.nav-links a[href]');
  const currentPath = window.location.pathname;

  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    if (href === currentPath || (currentPath === '/' && href === 'index.html')) {
      link.classList.add('active');
    }
  });

  /* ----------------------------------------------------------
     Popular Questions Accordion (blog index)
  ---------------------------------------------------------- */
  document.querySelectorAll('.pq-accordion-item').forEach(item => {
    const question = item.querySelector('.pq-accordion-question');
    const answer = item.querySelector('.pq-accordion-answer');

    if (!question || !answer) return;

    question.addEventListener('click', () => {
      const isActive = item.classList.contains('active');

      document.querySelectorAll('.pq-accordion-item').forEach(other => {
        other.classList.remove('active');
        const otherAnswer = other.querySelector('.pq-accordion-answer');
        if (otherAnswer) otherAnswer.style.maxHeight = null;
        const otherBtn = other.querySelector('.pq-accordion-question');
        if (otherBtn) otherBtn.setAttribute('aria-expanded', 'false');
      });

      if (!isActive) {
        item.classList.add('active');
        answer.style.maxHeight = answer.scrollHeight + 'px';
        question.setAttribute('aria-expanded', 'true');
      }
    });
  });

  /* ----------------------------------------------------------
     Blog Category Filter
  ---------------------------------------------------------- */
  const catFilterBtns = document.querySelectorAll('.cat-filter-btn');
  const catBlogCards = document.querySelectorAll('.blog-card[data-category]');

  if (catFilterBtns.length) {
    catFilterBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        const filter = btn.dataset.filter;

        catFilterBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');

        catBlogCards.forEach(card => {
          if (filter === 'all' || card.dataset.category === filter) {
            card.style.display = '';
          } else {
            card.style.display = 'none';
          }
        });
      });
    });
  }

})();
