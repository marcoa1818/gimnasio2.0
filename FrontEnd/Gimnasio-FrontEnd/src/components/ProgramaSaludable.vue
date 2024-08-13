<template>
  <div>
    <h1 class="text-2xl xl:text-3xl font-extrabold mb-6">Programas Saludables</h1>
    
    <!-- Formulario para añadir un nuevo programa -->
    <form @submit.prevent="addProgram">
      <input
        v-model="newProgram.name"
        class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5"
        type="text" placeholder="Nombre del Programa Saludable" required
      />
      <input
        v-model="newProgram.status"
        class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5"
        type="text" placeholder="Estatus" required
      />
      <input
        v-model="newProgram.duration"
        class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5"
        type="text" placeholder="Duración" required
      />
      <input
        v-model="newProgram.progress"
        class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5"
        type="number" placeholder="Porcentaje de Avance" required
      />
      <button
        class="mt-5 tracking-wide font-semibold bg-red-700 text-red-100 w-full py-4 rounded-lg hover:bg-red-900 transition-all duration-300 ease-in-out flex items-center justify-center focus:shadow-outline focus:outline-none col-span-2"
        type="submit"
      >
        Registrar
      </button>
    </form>

    <!-- Listado de programas -->
    <h2 class="text-xl font-bold mt-10">Lista de Programas Saludables</h2>
    <table class="min-w-full bg-white mt-5">
      <thead>
        <tr>
          <th class="py-2">ID</th>
          <th class="py-2">Nombre</th>
          <th class="py-2">Estatus</th>
          <th class="py-2">Duración</th>
          <th class="py-2">Porcentaje de Avance</th>
          <th class="py-2">Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="program in programs" :key="program.id">
          <td class="border px-4 py-2">{{ program.id }}</td>
          <td class="border px-4 py-2">{{ program.name }}</td>
          <td class="border px-4 py-2">{{ program.status }}</td>
          <td class="border px-4 py-2">{{ program.duration }}</td>
          <td class="border px-4 py-2">{{ program.progress }}%</td>
          <td class="border px-4 py-2">
            <button @click="editProgram(program.id)" class="bg-yellow-500 text-white px-4 py-2 rounded">
              Editar
            </button>
            <button @click="deleteProgram(program.id)" class="bg-red-500 text-white px-4 py-2 rounded ml-2">
              Eliminar
            </button>
          </td>
        </tr>
      </tbody>
    </table>

    <!-- Formulario para editar un programa -->
    <div v-if="editingProgram">
      <h2 class="text-xl font-bold mt-10">Editar Programa</h2>
      <form @submit.prevent="updateProgram">
        <input
          v-model="currentProgram.name"
          class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5"
          type="text" placeholder="Nombre del Programa Saludable" required
        />
        <input
          v-model="currentProgram.status"
          class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5"
          type="text" placeholder="Estatus" required
        />
        <input
          v-model="currentProgram.duration"
          class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5"
          type="text" placeholder="Duración" required
        />
        <input
          v-model="currentProgram.progress"
          class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5"
          type="number" placeholder="Porcentaje de Avance" required
        />
        <button
          class="mt-5 tracking-wide font-semibold bg-blue-700 text-gray-100 w-full py-4 rounded-lg hover:bg-blue-900 transition-all duration-300 ease-in-out flex items-center justify-center focus:shadow-outline focus:outline-none col-span-2"
          type="submit"
        >
          Actualizar
        </button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      programs: [
        { id: 1, name: "Programa de Nutrición", status: "Activo", duration: "3 meses", progress: 75 },
        { id: 2, name: "Entrenamiento Funcional", status: "Inactivo", duration: "6 meses", progress: 40 },
        { id: 3, name: "Yoga Avanzado", status: "Activo", duration: "1 mes", progress: 100 }
      ],
      newProgram: {
        name: "",
        status: "",
        duration: "",
        progress: 0
      },
      currentProgram: null,
      editingProgram: false
    };
  },
  methods: {
    addProgram() {
      if (this.newProgram.name && this.newProgram.status && this.newProgram.duration && this.newProgram.progress) {
        const newId = this.programs.length + 1;
        this.programs.push({ ...this.newProgram, id: newId });
        this.newProgram = { name: "", status: "", duration: "", progress: 0 };
      }
    },
    editProgram(id) {
      this.currentProgram = { ...this.programs.find(p => p.id === id) };
      this.editingProgram = true;
    },
    updateProgram() {
      const index = this.programs.findIndex(p => p.id === this.currentProgram.id);
      if (index !== -1) {
        this.programs.splice(index, 1, this.currentProgram);
      }
      this.currentProgram = null;
      this.editingProgram = false;
    },
    deleteProgram(id) {
      this.programs = this.programs.filter(p => p.id !== id);
    }
  }
};
</script>

<style scoped>
table {
  width: 100%;
  border-collapse: collapse;
}
th, td {
  border: 1px solid #ddd;
  text-align: left;
  padding: 8px;
}
</style>
