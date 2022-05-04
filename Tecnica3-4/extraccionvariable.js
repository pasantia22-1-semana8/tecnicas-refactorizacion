/*
Problema: expresion demasiado complicado de entender
Solucion: extraer fragmentos en variables bien nombrados
Causa: hacer compresible una expresion compleja
Beneficios: codigo mas legible
Inconveniencia: sin evalucion perezosa
*/

function fidelizarCliente(pedido){
    if(pedido.getLines().getLength()>5 
    && pedido.getImporteTotal()>1000 && 
    !pedido.getClient().isHabitual()){
        // ....
        console.log("logica de la aplicacion")
    }
}


//codigo refactorizado

function fielizarClienteRef(pedido){
    let esLargo = pedido.getLines().getLength() > 5;
    let importeAlto = pedido.getImporteTotal()> 1000;
    let clienteHabital = !pedido.getClient().isHabitual();

    let ofrecerDescuento = esLargo && importeAlto && clienteHabital;
    if(ofrecerDescuento){
        // codigo .....
    }
}


/*
code smells aplica
1. comentarios

es similar extraccion de metodo.
*/