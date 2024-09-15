const packages = document.querySelectorAll(".package");

function checkVisibility() {
  packages.forEach((package) => {
    const packageTop = package.getBoundingClientRect().top;
    const windowHeight = window.innerHeight;

    if (packageTop < windowHeight * 0.8) {
      // Paket %80 görünür olduğunda
      package.classList.add("show");
    }
  });
}

window.addEventListener("scroll", checkVisibility);
checkVisibility();
