document.addEventListener('DOMContentLoaded', () => {
  const toggleButton = document.querySelector('.menu-toggle');
  const nav = document.querySelector('.main-nav');

  if (toggleButton && nav) {
    toggleButton.addEventListener('click', () => {
      const isOpen = nav.classList.toggle('open');
      toggleButton.setAttribute('aria-expanded', String(isOpen));
    });
  }

  const revealItems = document.querySelectorAll('.reveal');
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
      }
    });
  }, { threshold: 0.15 });

  revealItems.forEach((item) => observer.observe(item));

  const galleryItems = document.querySelectorAll('.gallery-item');
  galleryItems.forEach((item) => {
    item.addEventListener('click', () => {
      const img = item.querySelector('img');
      if (!img) return;
      const modal = document.createElement('div');
      modal.style.position = 'fixed';
      modal.style.inset = '0';
      modal.style.background = 'rgba(30, 20, 18, 0.82)';
      modal.style.display = 'flex';
      modal.style.alignItems = 'center';
      modal.style.justifyContent = 'center';
      modal.style.zIndex = '999';
      modal.style.padding = '24px';

      const image = document.createElement('img');
      image.src = img.src;
      image.alt = img.alt;
      image.style.maxWidth = '90vw';
      image.style.maxHeight = '80vh';
      image.style.borderRadius = '18px';
      image.style.boxShadow = '0 20px 40px rgba(0,0,0,0.32)';

      modal.appendChild(image);
      document.body.appendChild(modal);
      modal.addEventListener('click', () => modal.remove());
    });
  });

  document.querySelectorAll('.video-sound-toggle').forEach((button) => {
    const video = button.parentElement.querySelector('video');
    if (!video) return;

    button.addEventListener('click', () => {
      video.muted = !video.muted;
      video.volume = 1;
      video.play().catch(() => {});
      const soundOn = !video.muted;
      button.textContent = soundOn ? 'Desativar som' : 'Ativar som';
      button.setAttribute('aria-pressed', String(soundOn));
    });
  });

  document.querySelectorAll('.eyebrow-image-rotator').forEach((rotator) => {
    const images = Array.from(rotator.querySelectorAll('.service-card-image'));
    if (images.length < 2) return;

    let activeIndex = images.findIndex((image) => image.classList.contains('is-active'));
    let rotation;
    if (activeIndex < 0) activeIndex = 0;

    const showImage = (index) => {
      images.forEach((image, imageIndex) => image.classList.toggle('is-active', imageIndex === index));
    };

    rotator.addEventListener('mouseenter', () => {
      rotation = window.setInterval(() => {
        activeIndex = (activeIndex + 1) % images.length;
        showImage(activeIndex);
      }, 1600);
    });

    rotator.addEventListener('mouseleave', () => {
      window.clearInterval(rotation);
      activeIndex = 0;
      showImage(activeIndex);
    });
  });
});
