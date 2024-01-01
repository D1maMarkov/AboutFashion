(function () {
  const texts = document.querySelectorAll('.text__left');

  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
    
      if (entry.isIntersecting) {
        entry.target.classList.add('anim__text__left');
        setTimeout(() => entry.target.classList.remove('anim__text__left'), 1000);
      }

    });
  });

  texts.forEach(text => {
    observer.observe(text);
  })
})();

(function () {
  const texts = document.querySelectorAll('.text__right');

  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
    
      if (entry.isIntersecting) {
        entry.target.classList.add('anim__text__right');
        setTimeout(() => entry.target.classList.remove('anim__text__right'), 1000);
      }

    });
  });

  texts.forEach(text => {
    observer.observe(text);
  })
})();
