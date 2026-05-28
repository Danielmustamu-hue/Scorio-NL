/* ============================================================
   SCORIO RAPPORT JS
   ============================================================ */

(function () {
  'use strict';

  /* ----------------------------------------------------------
     THEME TOGGLE
  ---------------------------------------------------------- */
  var themeBtn = document.getElementById('theme-toggle');
  var stored = localStorage.getItem('rapport_theme') || 'dark';

  function applyTheme(theme) {
    if (theme === 'light') {
      document.body.classList.add('light-mode');
      if (themeBtn) themeBtn.textContent = '🌙 Donker';
    } else {
      document.body.classList.remove('light-mode');
      if (themeBtn) themeBtn.textContent = '☀ Licht';
    }
  }

  applyTheme(stored);

  if (themeBtn) {
    themeBtn.addEventListener('click', function () {
      var current = document.body.classList.contains('light-mode') ? 'light' : 'dark';
      var next = current === 'light' ? 'dark' : 'light';
      localStorage.setItem('rapport_theme', next);
      applyTheme(next);
    });
  }

  /* ----------------------------------------------------------
     EMAIL GATE & DOWNLOAD
  ---------------------------------------------------------- */
  var downloadBtn = document.getElementById('download-btn');
  var modal = document.getElementById('email-modal');
  var modalClose = document.getElementById('modal-close');
  var modalSubmit = document.getElementById('modal-submit');
  var modalEmail = document.getElementById('modal-email');
  var modalNewsletter = document.getElementById('modal-newsletter');

  function openModal() {
    if (modal) modal.classList.add('active');
    if (modalEmail) setTimeout(function () { modalEmail.focus(); }, 100);
  }

  function closeModal() {
    if (modal) modal.classList.remove('active');
  }

  function triggerPrint() {
    window.print();
  }

  if (downloadBtn) {
    downloadBtn.addEventListener('click', function () {
      var email = localStorage.getItem('scorio_email');
      if (email) {
        triggerPrint();
      } else {
        openModal();
      }
    });
  }

  if (modalClose) {
    modalClose.addEventListener('click', closeModal);
  }

  if (modal) {
    modal.addEventListener('click', function (e) {
      if (e.target === modal) closeModal();
    });
  }

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') closeModal();
  });

  if (modalSubmit) {
    modalSubmit.addEventListener('click', function () {
      var email = modalEmail ? modalEmail.value.trim() : '';
      if (!email || !email.includes('@') || !email.includes('.')) {
        if (modalEmail) {
          modalEmail.classList.add('error');
          modalEmail.focus();
          setTimeout(function () { modalEmail.classList.remove('error'); }, 2000);
        }
        return;
      }
      localStorage.setItem('scorio_email', email);
      if (modalNewsletter && modalNewsletter.checked) {
        localStorage.setItem('scorio_newsletter', '1');
      }
      closeModal();
      setTimeout(triggerPrint, 300);
    });
  }

  if (modalEmail) {
    modalEmail.addEventListener('keydown', function (e) {
      if (e.key === 'Enter') {
        if (modalSubmit) modalSubmit.click();
      }
    });
  }

  /* ----------------------------------------------------------
     SCORE RING ANIMATION
  ---------------------------------------------------------- */
  var CIRCUMFERENCE = 2 * Math.PI * 54; // radius 54 → ≈339.3

  function getScoreColor(score) {
    if (score >= 75) return 'var(--accent)';
    if (score >= 50) return 'var(--orange)';
    return 'var(--red)';
  }

  function animateRing(ringEl, score) {
    var offset = CIRCUMFERENCE * (1 - score / 100);
    ringEl.style.strokeDasharray = CIRCUMFERENCE;
    ringEl.style.strokeDashoffset = CIRCUMFERENCE; // start at 0%
    ringEl.style.stroke = getScoreColor(score);
    requestAnimationFrame(function () {
      requestAnimationFrame(function () {
        ringEl.style.strokeDashoffset = offset;
      });
    });
  }

  function animateScoreNumbers() {
    var els = document.querySelectorAll('.score-number[data-score]');
    els.forEach(function (el) {
      var target = parseInt(el.getAttribute('data-score'), 10);
      var current = 0;
      var step = Math.max(1, Math.ceil(target / 50));
      el.textContent = '0';
      var timer = setInterval(function () {
        current = Math.min(current + step, target);
        el.textContent = current;
        if (current >= target) clearInterval(timer);
      }, 20);
    });
  }

  function animateProgressBars() {
    var bars = document.querySelectorAll('.metric-bar-fill[data-width]');
    bars.forEach(function (bar) {
      var width = bar.getAttribute('data-width');
      requestAnimationFrame(function () {
        requestAnimationFrame(function () {
          bar.style.width = width + '%';
        });
      });
    });
  }

  /* ----------------------------------------------------------
     INTERSECTION OBSERVER — trigger animations when visible
  ---------------------------------------------------------- */
  var animated = false;

  function runAnimations() {
    if (animated) return;
    animated = true;

    // Score rings
    var rings = document.querySelectorAll('.ring-fill[data-score]');
    rings.forEach(function (ring) {
      var score = parseInt(ring.getAttribute('data-score'), 10);
      animateRing(ring, score);
    });

    // Score counter numbers
    animateScoreNumbers();

    // Progress bars
    animateProgressBars();
  }

  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        runAnimations();
        observer.disconnect();
      }
    });
  }, { threshold: 0.1 });

  var scoreSection = document.getElementById('score-overview');
  if (scoreSection) {
    observer.observe(scoreSection);
  } else {
    window.addEventListener('load', runAnimations);
  }

  /* ----------------------------------------------------------
     SCORE COLOR LABELS (set dynamically from data-score)
  ---------------------------------------------------------- */
  window.addEventListener('DOMContentLoaded', function () {
    // Color sub-score numbers
    var subScores = document.querySelectorAll('.sub-score-number[data-score]');
    subScores.forEach(function (el) {
      var score = parseInt(el.getAttribute('data-score'), 10);
      if (score >= 75) el.classList.add('score-green');
      else if (score >= 50) el.classList.add('score-orange');
      else el.classList.add('score-red');
    });

    // Set verdict badges on sub-scores
    var verdicts = document.querySelectorAll('.sub-score-verdict[data-score]');
    verdicts.forEach(function (el) {
      var score = parseInt(el.getAttribute('data-score'), 10);
      if (score >= 75) el.classList.add('badge-green');
      else if (score >= 50) el.classList.add('badge-orange');
      else el.classList.add('badge-red');
    });
  });
}());
