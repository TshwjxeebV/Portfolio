// Scroll reveal: elements with .reveal fade up once as they enter the screen.
(function () {
  var els = document.querySelectorAll('.reveal');
  if (!('IntersectionObserver' in window)) {
    els.forEach(function (el) { el.classList.add('is-visible'); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          e.target.classList.add('is-visible');
          io.unobserve(e.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    els.forEach(function (el) { io.observe(el); });
  }

  // Mobile menu
  var btn = document.querySelector('.menu-btn');
  var links = document.querySelector('.nav-links');
  if (btn && links) {
    btn.addEventListener('click', function () {
      var open = links.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    links.addEventListener('click', function (e) {
      if (e.target.tagName === 'A') { links.classList.remove('open'); btn.setAttribute('aria-expanded', 'false'); }
    });
  }

  // Contact form: opens the visitor's email app with the message filled in.
  var form = document.querySelector('#contact-form');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var f = new FormData(form);
      var to = form.getAttribute('data-email');
      var subject = 'Portfolio inquiry from ' + (f.get('first') || '') + ' ' + (f.get('last') || '');
      var body = (f.get('message') || '') + '\n\n' + (f.get('first') || '') + ' ' + (f.get('last') || '') + '\n' + (f.get('email') || '');
      window.location.href = 'mailto:' + to + '?subject=' + encodeURIComponent(subject.trim()) + '&body=' + encodeURIComponent(body);
    });
  }

  var y = document.querySelector('#year');
  if (y) y.textContent = new Date().getFullYear();
})();
