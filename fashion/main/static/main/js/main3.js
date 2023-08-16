(function () {
  var blocktext = document.querySelector('#third-block-text');
  var models = blocktext.querySelector('#models');

  var observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (typeof getCurrentAnimationPreference === 'function' && !getCurrentAnimationPreference()) {
        return;
      }

      if (entry.isIntersecting) {
        models.classList.add('anim2');
        return;
      }

      models.classList.remove('anim2');
    });
  });

  observer.observe(blocktext);
})();