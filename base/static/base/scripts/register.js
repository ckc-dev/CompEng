const isBusinessCheckbox = document.querySelector("#id_is_business");
const cpfInput = document.querySelector("#id_cpf");
const cpfLabel = document.querySelector("label[for='id_cpf']");
const cpfGroup = [cpfInput, cpfLabel];

const cnpjInput = document.querySelector("#id_cnpj");
const cnpjLabel = document.querySelector("label[for='id_cnpj']");
const cnpjGroup = [cnpjInput, cnpjLabel];

function toggleDocumentInputs() {
  if (isBusinessCheckbox.checked) {
    cnpjGroup.forEach((e) => (e.style.display = ""));
    cpfGroup.forEach((e) => (e.style.display = "none"));
  } else {
    cnpjGroup.forEach((e) => (e.style.display = "none"));
    cpfGroup.forEach((e) => (e.style.display = ""));
  }
}

toggleDocumentInputs();
isBusinessCheckbox.onchange = () => toggleDocumentInputs();
