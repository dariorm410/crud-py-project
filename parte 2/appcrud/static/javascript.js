(function(win, doc){
    'use strict';   

    
    if(doc.querySelector('.btnDel')){ // Verifica se existem botões de exclusão no documento
        let btnDel = doc.querySelectorAll('.btnDel'); // Seleciona todos os botões de exclusão
        for(let i = 0; i < btnDel.length; i++){ // Itera sobre cada botão de exclusão
            
            btnDel[i].addEventListener('click', function(event){ // Adiciona um evento de clique a cada botão
                if(confirm('Deseja mesmo apagar este dado?')){ // Exibe uma caixa de diálogo de confirmação para excluir o dado
                    return true; // Se o usuário confirmar, retorna true, permitindo a exclusão

                }else{  // Se o usuário cancelar, evita a exclusão
                    event.preventDefault(); 
                }
            });
        }
    }


})(window, document);
