const generateBtn = document.getElementById("generate-password");
const passwordNumberInp = document.getElementById("password-number");
const passwordList = document.getElementById("passwords-list");
const passwordTemplate = document.getElementById("password");
const addAnotherPasswordBtn = document.getElementById("add_another_password");


const addPasswordElement = (password, delay) => {
  const clone = passwordTemplate.content.firstElementChild.cloneNode(true);

  const passwordText = clone.querySelector(".password_text");
  passwordText.value = password;

  const copyPassword = clone.querySelector(".copy_password");
  copyPassword.addEventListener("click", () => {
    passwordText.select();
    passwordText.setSelectionRange(0, 99999); // for mobile devices

    navigator.clipboard.writeText(passwordText.value);
  });

  const deletePassword = clone.querySelector(".delete_password");
  deletePassword.addEventListener("click", (evt) => {
    clone.classList.add("animate__fadeOut");
    clone.style.setProperty("-webkit-animation-duration", "0.3s");
    clone.style.setProperty("-webkit-animation-delay", "0s");

    setTimeout(() => {
      evt.target.parentNode.remove();
    }, 190);
  });

  clone.style.setProperty("-webkit-animation-delay", delay / 15 + "s");

  passwordList.appendChild(clone);
};

const addPassword = async (complexity, count = 1) => {
  const res = await fetch(
    `/api/passwords?count=${count}&complexity=${complexity}`
  );
  const data = await res.json();

  data.forEach((password, i) => addPasswordElement(password, i));
};

generateBtn.addEventListener("click", () => {
  passwordList.innerHTML = "";

  const count = passwordNumberInp.value ? passwordNumberInp.value : 1;
  const complexity = document.querySelector(
    "input[name=password-difficulty]:checked"
  ).value;

  addPassword(complexity, count);
});

addAnotherPasswordBtn.addEventListener("click", () => {
  const complexity = document.querySelector(
    "input[name=password-difficulty]:checked"
  ).value;

  addPassword(complexity);
});

function download (data){
    const blob = new Blob([data], { type: 'text/csv' });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.setAttribute('href', url);
    a.setAttribute('download', 'download.csv');
    a.click();
}
  
function convertToCSV (data) {
    return 'Passwords \n' + data.join('\n');
}
  
const get_CSV = function() {
    var inputs = $('.password_text');
    var passwords = inputs.map((_, element) => element.value);
    var CSV_data = []
    for (i = 0; i < passwords.length; i++) {
      CSV_data.push(passwords[i]);
    }
    console.log(CSV_data);
    download_data = convertToCSV(CSV_data);
    download(download_data);
}


  $(document).ready(function(){
      $("#myModal").modal('show');
    });
  
  const exportToCSVBtn = document.getElementById('export-to-csv');
  exportToCSVBtn.addEventListener("click", get_CSV);

