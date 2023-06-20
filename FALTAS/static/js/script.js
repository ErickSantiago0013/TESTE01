// Script para adicionar comportamento interativo à tabela em cadastros.html
window.addEventListener('DOMContentLoaded', () => {
    const table = document.querySelector('table');
    table.addEventListener('click', (event) => {
      const targetRow = event.target.closest('tr');
      if (targetRow) {
        targetRow.classList.toggle('highlight');
      }
    });
  });
  
// MENU***************************************************************************************
  // Seleciona todos os itens do menu com submenu
const menuItems = document.querySelectorAll('.navbar li');

// Adiciona evento de clique a cada item
menuItems.forEach(item => {
  // Verifica se o item possui submenu
  if (item.querySelector('.submenu')) {
    // Adiciona evento de clique para abrir/fechar o submenu
    item.addEventListener('click', () => {
      item.querySelector('.submenu').classList.toggle('show');
    });
  }
});


// BUSCA DO EMPREGADO NA EXCLUSÃO **********************************************************************
function buscarEmpregado() {
  var codigo = document.getElementById('codigo').value;

  // Faz uma requisição AJAX para buscar os dados do empregado com base no código fornecido
  var xhr = new XMLHttpRequest();
  xhr.open('GET', '/buscar_empregado?codigo=' + codigo, true);
  xhr.onreadystatechange = function() {
    if (xhr.readyState === XMLHttpRequest.DONE) {
      if (xhr.status === 200) {
        var dadosEmpregado = JSON.parse(xhr.responseText);
        if (dadosEmpregado) {
          document.getElementById('codigoEmpregado').innerText = dadosEmpregado.codigo;
          document.getElementById('nomeEmpregado').innerText = dadosEmpregado.nome;
          document.getElementById('cargoEmpregado').innerText = dadosEmpregado.cargo;
          document.getElementById('lojaEmpregado').innerText = dadosEmpregado.loja;
          document.getElementById('salarioEmpregado').innerText = dadosEmpregado.salario;

          document.getElementById('dadosEmpregado').style.display = 'block';
        } else {
          alert('Empregado não encontrado.');
        }
      } else {
        alert('Erro ao buscar empregado. Status: ' + xhr.status);
      }
    }
  };
  xhr.send();
}

//FUNÇÃO DE EXCLUIR *******************************************************************************
function excluirEmpregado() {
  var confirmacao = confirm('Tem certeza que deseja excluir o empregado?');

  if (confirmacao) {
    var codigo = document.getElementById('codigo').value;

    // Faça uma requisição AJAX para excluir o empregado no servidor
    // Exemplo simplificado:
    // Substitua esse código pela lógica adequada para excluir o empregado no servidor
    fetch('/excluir', {
      method: 'POST',
      body: JSON.stringify({ codigo: codigo }),
      headers: {
        'Content-Type': 'application/json'
      }
    })
      .then(response => response.text())
      .then(message => {
        // Exiba uma caixa de mensagem informando que a exclusão foi realizada com sucesso
        alert(message);

        // Redirecione para a página inicial ou realize qualquer ação desejada após a exclusão
        window.location.href = '/';
      })
      .catch(error => {
        console.error('Erro ao excluir o empregado:', error);
      });
  }
}

document.addEventListener('DOMContentLoaded', function() {
  var codigoInput = document.getElementById('codigo');
  
  codigoInput.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
      event.preventDefault(); // Evita o envio do formulário

      buscarEmpregado();
    }
  });
});