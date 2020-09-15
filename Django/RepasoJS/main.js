//alertas aler()

//variables
var nombre = "lodo";
var altura = 190;
/*
//concatenacion
var concatenacion = nombre + " " + altura;

//document.write(nombre)
//document.write(altura);

var datos = document.getElementById("datos");
//datos.innerHTML = concatenacion;

datos.innerHTML = `
    <h1>Soy un bloque</h1>
    `;
*/

function MuestaMiNombre(nombre, altura){
    var datos = document.getElementById("datos");
    datos.innerHTML = `
    <h1>Soy un bloque ${nombre}, de ${altura}</h1>
    `;
}

MuestaMiNombre('Lodo', 222)