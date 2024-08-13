<template>
    <div>
      <form @submit.prevent="registrarPrograma">
        <h1 class="text-2xl xl:text-3xl font-extrabold">Programas Saludables</h1>
  
        <input
          v-model="nuevoPrograma.id"
          class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5"
          type="text" placeholder="ID del Programa"
        /> 
        <input
          v-model="nuevoPrograma.nombre"
          class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5 col-span-2"
          type="text" placeholder="Nombre del Programa Saludable"
        />
        <input
          v-model="nuevoPrograma.estatus"
          class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5"
          type="text" placeholder="Estatus"
        />
        <input
          v-model="nuevoPrograma.duracion"
          class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5"
          type="text" placeholder="Duración"
        />
        <input
          v-model="nuevoPrograma.avance"
          class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5"
          type="text" placeholder="Porcentaje de Avance"
        />
        <button
          type="submit"
          class="mt-5 tracking-wide font-semibold bg-red-700 text-gray-100 w-full py-4 rounded-lg hover:bg-red-900 transition-all duration-300 ease-in-out flex items-center justify-center focus:shadow-outline focus:outline-none col-span-2"
        >
          Registrar
        </button>
      </form>
  
      <div class="mt-10">
        <h2 class="text-xl font-bold">Programas Registrados</h2>
        <ul>
          <li v-for="programa in programas" :key="programa.id">
            {{ programa.nombre }} - {{ programa.estatus }} - {{ programa.duracion }} - {{ programa.avance }}%
          </li>
        </ul>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        nuevoPrograma: {
          id: '',
          nombre: '',
          estatus: '',
          duracion: '',
          avance: ''
        },
        programas: []  // Aquí almacenarás los programas registrados
      };
    },
    methods: {
      async registrarPrograma() {
        // Aquí debes hacer la llamada a tu API o backend para registrar el programa
        try {
          // Ejemplo de llamada a API usando fetch (puedes usar Axios si prefieres)
          let response = await fetch('https://tu-api.com/programas', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify(this.nuevoPrograma)
          });
  
          if (response.ok) {
            let programaGuardado = await response.json();
            this.programas.push(programaGuardado);  // Agrega el nuevo programa a la lista
            this.limpiarFormulario();  // Limpia el formulario después de guardar
          } else {
            console.error('Error al guardar el programa');
          }
        } catch (error) {
          console.error('Error en la petición', error);
        }
      },
      limpiarFormulario() {
        this.nuevoPrograma = {
          id: '',
          nombre: '',
          estatus: '',
          duracion: '',
          avance: ''
        };
      }
    },
    mounted() {
      // Puedes cargar los programas existentes desde el backend cuando se monta el componente
      this.cargarProgramas();
    },
    methods: {
      async cargarProgramas() {
        try {
          let response = await fetch('https://tu-api.com/programas');
          this.programas = await response.json();
        } catch (error) {
          console.error('Error al cargar los programas', error);
        }
      }
    }
  };
  </script>
  