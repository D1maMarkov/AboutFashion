(function () {
  var models = document.querySelectorAll('.mainhr');

  var observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (typeof getCurrentAnimationPreference === 'function' && !getCurrentAnimationPreference()) {
        return;
      }

      if (entry.isIntersecting) {
        models.forEach( model => {
            model.classList.add('mainhrhr')
        });
        return;
      }

      models.forEach( model => {
            model.classList.remove('mainhrhr')
      });

    });
  });
  models.forEach( model => {
    observer.observe(model);
  });
})();