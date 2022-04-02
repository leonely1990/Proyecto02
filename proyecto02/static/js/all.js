let botonCrearEquipo = document.getElementById('crearEquipo');
let botonCrear = document.getElementById('crear');
let botonSalir = document.getElementById('salir');
let formulario = document.getElementById('contenedorFormulario');
let tabla = document.getElementById('tabla');

function mostrarForm() {
    formulario.style.display = 'flex';
    tabla.style.display = 'none';
    botonCrearEquipo.style.display = 'none';
    botonCrear.onsubmit();
}

function salirForm() {
    formulario.style.display = 'none';
    tabla.style.display = 'table';
    botonCrearEquipo.style.display = 'block';
}

function crearEquipo(params) {
    document.forms.submit
}

botonCrearEquipo.addEventListener('click', mostrarForm);
botonSalir.addEventListener('click', salirForm);
botonCrear.addEventListener('submit', crearEquipo);