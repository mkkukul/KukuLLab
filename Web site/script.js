// function scrollToSection(id) {
//   document.getElementById(id).scrollIntoView({ behavior: "smooth" });
// }
const packages = document.querySelectorAll(".package");

packages.forEach((package) => {
  package.addEventListener("click", () => {
    packages.forEach((pkg) => pkg.classList.remove("active")); // Diğer paketleri kapat
    package.classList.toggle("active"); // Tıklanan paketi aç/kapat
  });
});
