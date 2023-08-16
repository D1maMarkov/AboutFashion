(function () {
  var blocktext = document.querySelector('#second-block-text');
  var models = blocktext.querySelector('#designers');

  var observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (typeof getCurrentAnimationPreference === 'function' && !getCurrentAnimationPreference()) {
        return;
      }

      if (entry.isIntersecting) {
        models.classList.add('anim');
        return;
      }

      models.classList.remove('anim');
    });
  });

  observer.observe(blocktext);
})();