function myFunction() {
  document.getElementById("myDropdown3").classList.remove("show3");
  document.getElementById("myDropdown2").classList.remove("show2");
  document.getElementById("myDropdown").classList.toggle("show");


// Close the dropdown menu if the user clicks outside of it
window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }

    }

  }
}
}


function myFunction2() {
  document.getElementById("myDropdown3").classList.remove("show3");
  document.getElementById("myDropdown").classList.remove("show");
  document.getElementById("myDropdown2").classList.toggle("show2");


// Close the dropdown menu if the user clicks outside of it
window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {
    var dropdowns2 = document.getElementsByClassName("dropdown-content2");
    var j;
    for (j = 0; j < dropdowns2.length; j++) {
      var openDropdown2 = dropdowns2[j];
      if (openDropdown2.classList.contains('show2')) {
        openDropdown2.classList.remove('show2');
      }
    }
  }
}
}

function myFunction3() {
  document.getElementById("myDropdown").classList.remove("show");
  document.getElementById("myDropdown2").classList.remove("show2");
  document.getElementById("myDropdown3").classList.toggle("show3");


window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {
    var dropdowns = document.getElementsByClassName("dropdown-content3");
    var k;
    for (k = 0; k < dropdowns.length; k++) {
      var openDropdown = dropdowns[k];
      if (openDropdown.classList.contains('show3')) {
        openDropdown.classList.remove('show3');
      }
    }
  }
}
}
