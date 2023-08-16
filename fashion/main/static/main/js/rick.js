(function () {
  var blocktext = document.querySelector('#lamyy');
  var models = blocktext.querySelector('#textaboutlamy');

  var observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (typeof getCurrentAnimationPreference === 'function' && !getCurrentAnimationPreference()) {
        return;
      }

      if (entry.isIntersecting) {
        models.classList.add('animLamy');
        return;
      }

      models.classList.remove('animLamy');
    });
  });

  observer.observe(blocktext);
})();