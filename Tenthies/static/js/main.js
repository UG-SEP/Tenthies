const menuBtn = document.querySelector(".menu-icon span");
const cancelBtn = document.querySelector(".cancel-icon");
const items = document.querySelector(".nav-items");

menuBtn.onclick = ()=>{
  document.body.style.margin='0'
  document.body.style.height='100%'
  document.body.style.overflow='hidden'
  items.classList.add("active");
  menuBtn.classList.add("hide");
  cancelBtn.classList.add("show");
}
cancelBtn.onclick = ()=>{
    document.body.style.margin='0'
    document.body.style.height='100%'
    document.body.style.overflow='visible'
  items.classList.remove("active");
  menuBtn.classList.remove("hide");
  cancelBtn.classList.remove("show");
  cancelBtn.style.color = "#ff3d00";
}