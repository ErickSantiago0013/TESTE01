function buscarFuncionario() {
    var codigo = document.getElementById('codigo').value;
  
    // Realizar a requisição AJAX para buscar o funcionário
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/buscar_funcionario?codigo=' + codigo, true);
    xhr.onload = function() {
      if (xhr.status === 200) {
        var funcionario = JSON.parse(xhr.responseText);
        if (funcionario) {
          exibirCamposEdicao(funcionario);
        } else {
          alert('Funcionário não encontrado');
        }
      } else {
        alert('Erro ao buscar funcionário. Tente novamente.');
      }
    };
    xhr.onerror = function() {
      alert('Erro ao buscar funcionário. Tente novamente.');
    };
    xhr.send();
  }
  
  function exibirCamposEdicao(funcionario) {
    document.getElementById('funcionarioId').value = funcionario.id;
    document.getElementById('nome').value = funcionario.nome;
    document.getElementById('cargo').value = funcionario.cargo;
    document.getElementById('loja').value = funcionario.loja;
    document.getElementById('salario').value = funcionario.salario;
    document.getElementById('dadosFuncionario').style.display = 'block';
  }
  