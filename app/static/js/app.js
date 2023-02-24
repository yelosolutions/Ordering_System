const step1 = document.getElementById("step1");
const step2 = document.getElementById("step2");
const step3 = document.getElementById("step3");
const previewOrderBtn = document.getElementById("previewOrderBtn");

previewOrderBtn.addEventListener("click", function() {
  // Get order information
const contactNumber = document.getElementById("contactNumber").value;
const numPages = document.getElementById("numPages").value;
const deadline = document.getElementById("deadline").value;
const topic = document.getElementById("topic").value;

// Show order information in Step 2
step1.style.display = "none";
step2.style.display = "block";
});

// Add event listener to the checkbox for Paypal payment
const paypalCheckbox = document.querySelector('input[name="paypal"]');
paypalCheckbox.addEventListener('change', function() {
    if (this.checked) {
        alert('You will be redirected to Paypal for payment.');
    }
});