/*
variable temporal en linea
Problema: variable local, expresion simple
Solucion: reemplazar referencias por expresion
Beneficios: pocos por si misma.
*/
// ejemplo

function procesarPedido(pedido){
    let numLineas = pedido.getLineas().getLength()
    if (numLineas > 5){
        /// linea de codigo ....
    }
    for (var i = 0; i < numLineas; i++){
        // linea de codigo....
    }
}

// opcion dos
function procesarPedido2(pedido){
    if (pedido.getLineas().getlength() > 5){
        /// linea de codigo ....
    }
    for (var i = 0; i < pedido.getLineas.getLength(); i++){
        // linea de codigo....
    }
}