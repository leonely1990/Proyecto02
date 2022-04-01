let CrearEquipo = document.getElementById('botonCrear');
let BotonCerrar = document.getElementById('botonCerrar');

function mostrar() {
    document.getElementById('formulario').style.display = 'flex';
    document.getElementsByName('body').style.BackgroudColor = "#d3e9fc00";
}

function cerrar(){
    document.getElementById('formulario').style.display = 'none';
}

CrearEquipo.addEventListener('click', mostrar);
BotonCerrar.addEventListener('click', cerrar);