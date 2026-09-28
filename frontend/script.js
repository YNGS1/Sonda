function validateForm() {
  var x = document.forms["search-form"]["firstName","lastName","email","username","phone","location"].value;
  if (x == "") {
    alert("Name must be filled out");
    return false;
  }
}