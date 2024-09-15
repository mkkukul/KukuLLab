const packages = document.querySelectorAll(".package");

packages.forEach((package) => {
  package.addEventListener("click", () => {
    packages.forEach((pkg) => pkg.classList.remove("active"));
    package.classList.toggle("active");
  });
});
