<template>
    <Rutina></Rutina>

    <div class="mt-12">
        <div class="relative overflow-x-auto shadow-md sm:rounded-lg">
            <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
                <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                    <tr>
                        <th scope="col" class="p-4">
                            <div class="flex items-center">
                                <input id="checkbox-all-search" type="checkbox"
                                    class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
                                <label for="checkbox-all-search" class="sr-only">checkbox</label>
                            </div>
                        </th>
                        <th scope="col" class="px-6 py-3">
                            Nombre
                        </th>
                        <th scope="col" class="px-6 py-3">
                            Programa Saludable
                        </th>
                        <th scope="col" class="px-6 py-3">
                            Fecha Registro
                        </th>
                        <th scope="col" class="px-6 py-3">
                            Fecha Actualización
                        </th>
                        <th scope="col" class="px-6 py-3">
                            Tiempo Aproximado
                        </th>
                        <th scope="col" class="px-6 py-3">
                            Estatus
                        </th>
                        <th scope="col" class="px-6 py-3">
                            Resultados Esperados
                        </th>
                        <th scope="col" class="px-6 py-3">
                            Action
                        </th>
                    </tr>
                </thead>
                <tbody>
                    <tr
                        class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
                        <td class="w-4 p-4">
                            <div class="flex items-center">
                                <input id="checkbox-table-search-1" type="checkbox"
                                    class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
                                <label for="checkbox-table-search-1" class="sr-only">checkbox</label>
                            </div>
                        </td>
                        <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                            Mario
                        </th>
                        <td class="px-6 py-4">
                            Gutierrez
                        </td>
                        <td class="px-6 py-4">
                            Rosales
                        </td>
                        <td class="px-6 py-4">
                            Masculino
                        </td>
                        <td class="px-6 py-4">
                            O+
                        </td>
                        <td class="px-6 py-4">
                            18/10/03
                        </td>
                        <td class="px-6 py-4">
                            <img src="https://cdn-icons-png.flaticon.com/512/6073/6073873.png" width="25px">
                        </td>
                        <td class="flex items-center px-6 py-4">
                            <a href="#" class="font-medium text-blue-600 dark:text-blue-500 hover:underline">Editar</a>
                            <a href="#" class="font-medium text-red-600 dark:text-red-500 hover:underline ms-3">Eliminar</a>
                        </td>
                    </tr>
                    <tr
                        class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
                        <td class="w-4 p-4">
                            <div class="flex items-center">
                                <input id="checkbox-table-search-2" type="checkbox"
                                    class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
                                <label for="checkbox-table-search-2" class="sr-only">checkbox</label>
                            </div>
                        </td>
                        <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                            Sebastian
                        </th>
                        <td class="px-6 py-4">
                            Marquez
                        </td>
                        <td class="px-6 py-4">
                            Garcia
                        </td>
                        <td class="px-6 py-4">
                            Masculino
                        </td>
                        <td class="px-6 py-4">
                            O+
                        </td>
                        <td class="px-6 py-4">
                            11/06/24
                        </td>
                        <td class="px-6 py-4">
                            <img src="https://cdn-icons-png.flaticon.com/512/6073/6073873.png" width="25px">
                        </td>
                        <td class="flex items-center px-6 py-4">
                            <a href="#" class="font-medium text-blue-600 dark:text-blue-500 hover:underline">Editar</a>
                            <a href="#" class="font-medium text-red-600 dark:text-red-500 hover:underline ms-3">Eliminar</a>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>

    </div>
</template>

<script>
import Rutina from "./Rutina.vue";

export default {
    components: {
        Rutina,
    },
};
</script>