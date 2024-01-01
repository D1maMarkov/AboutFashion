(function () {
  const hrs = document.querySelectorAll('.hr__wrapper hr');

  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('hr__anim')
        return;
      }
      else{

      entry.target.classList.remove('hr__anim');
      }
    });
  });

  hrs.forEach(hr => {
    observer.observe(hr);
  });
})();