/**
 * Extraccion de metodo
 * problema: Fragmento de codigo agrupable
 * Solucion: Mover codigo a nuevo metodo y llamarlo
 * Causa: Reducir longitud, preparar terreno a refactorizacion.
 * Beneficios: Codigo legible, menos duplicados, asislar codigo independiente.
 */

//ejemplo 1

function imprimirInforme(data){
    console.log("Fecha inicio:",data.fechaInicio)
    console.log("Fecha fin:",data.fechaFin)
    console.log("Autor:",data.autor)
    console.log("Titulo",data.titulo)
    console.log("-----------------------------------")
}

informe={
    fechaInicio:"12/05/2021",
    fechaFin:"15/05/2021",
    autor: "Juan Lopez",
    titulo: "Primer informe"
}

imprimirInforme(informe)

// refactorizando

function imprimirInformeRef(data){
    imprimirCabecera(data)
    console.log("Titulo",data.titulo)
}
function imprimirCabecera(data){
    console.log("Fecha inicio:",data.fechaInicio)
    console.log("Fecha fin:",data.fechaFin)
    console.log("Autor:",data.autor)
}

imprimirInformeRef(informe)

/**
 * se aplica para tratar los siguientes code smells
 * 1. Comentarios
 * 2. codigo duplicado
 * 3. clase de datos
 * 4. Metodo grande
 * 5. Senticas switch
 * 6. Envidia de caracteristica
 * 7. Cadenas de mensajes.
 */

