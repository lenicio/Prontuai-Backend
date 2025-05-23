document.addEventListener('DOMContentLoaded', function() {
    const cepInput = document.getElementById('id_cep');
    const ruaInput = document.getElementById('id_rua');
    const bairroInput = document.getElementById('id_bairro');
    const cidadeInput = document.getElementById('id_cidade');
    const estadoInput = document.getElementById('id_estado');

    // formata o cep
    cepInput.addEventListener('input', function() {
        let value = cepInput.value.replace(/\D/g, '');
        value = value.replace(/(\d{5})(\d)/, '$1-$2');
        cepInput.value = value;
    });

    cepInput.addEventListener('blur', function() {
        const cep = cepInput.value.replace(/\D/g, '');
        if (cep.length === 8) {
            fetch(`https://viacep.com.br/ws/${cep}/json/`)
                .then(response => response.json())
                .then(data => {
                    ruaInput.value = data.logradouro;
                    bairroInput.value = data.bairro;
                    cidadeInput.value = data.localidade;
                    estadoInput.value = data.uf;
                })
                .catch(error => {
                });
        }
    });
});
