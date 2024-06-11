let menu = document.querySelector(".menu")
let menu_child = document.querySelector(".menu-child")

function myFunction(){
    menu_child.classList.toggle('show')
}


menu.addEventListener("click", myFunction)