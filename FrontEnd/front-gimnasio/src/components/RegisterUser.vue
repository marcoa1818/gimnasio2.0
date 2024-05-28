<template>
    <div class="flex items-center justify-center p-12">
        <!-- Author: FormBold Team -->
        <div class="mx-auto w-full max-w-[550px] bg-white">
            <h1 class="text-2xl xl:text-3xl font-extrabold">
                Registrar Usuarios
            </h1>
            <br>
            <form>
                <div class="mb-5">
                    <label for="name" class="mb-3 block text-base font-medium text-[#07074D]">
                        Nombre
                    </label>
                    <input type="text" name="name" id="name" placeholder="Nombre"
                        class="w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md" />
                </div>
                <div class="mb-5">
                    <label for="primerapellido" class="mb-3 block text-base font-medium text-[#07074D]">
                        Apellido Paterno
                    </label>
                    <input type="text" name="patapellido" id="patapellido" placeholder="Ingresa tu Apellido Paterno"
                        class="w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md" />
                </div>
                <div class="mb-5">
                    <label for="matapellido" class="mb-3 block text-base font-medium text-[#07074D]">
                        Apellido Materno
                    </label>
                    <input type="text" name="matapellido" id="matapellido" placeholder="Ingresa tu Apellido Materno"
                        class="w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md" />
                </div>

                <div class="-mx-3 flex flex-wrap">
                    <div class="w-full px-3 sm:w-1/2">
                        <div class="mb-5">
                            <label for="time" class="mb-3 block text-base font-medium text-[#07074D]">
                                Titulo de Cortesia
                            </label>
                            <input type="text" name="titulocortesia" id="titulocort" placeholder="Tit."
                                class="w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md" />
                        </div>
                    </div>

                    <div class="w-full px-3 sm:w-1/2">
                        <div class="mb-5">
                            <label for="date" class="mb-3 block text-base font-medium text-[#07074D]">
                                Fecha de Nacimiento
                            </label>
                            <input type="date" name="date" id="date"
                                class="w-full rounded-md border border-[#e0e0e0] bg-white py-3 px-6 text-base font-medium text-[#6B7280] outline-none focus:border-[#6A64F1] focus:shadow-md" />
                        </div>
                    </div>
                </div>

                <div class="mb-4">
                    <label for="genero" class="mb-3 block text-base font-medium text-[#07074D]">Genero</label>
                    <select id="genero" name="genero"
                        class="border border-gray-400 p-2 w-full rounded-lg focus:outline-none focus:border-blue-400"
                        required>
                        <option value="">Selecciona tú genero</option>
                        <option value="masculino">Masculino</option>
                        <option value="femenino">Femenino</option>
                        <option value="otro">Otro</option>
                    </select>
                </div>

                <div class="mb-4">
                    <label for="sangre" class="mb-3 block text-base font-medium text-[#07074D]">Tipo de Sangre</label>
                    <select id="sangre" name="sangre"
                        class="border border-gray-400 p-2 w-full rounded-lg focus:outline-none focus:border-blue-400"
                        required>
                        <option value="">Selecciona tu tipo de Sangre</option>
                        <option value="">A+</option>
                        <option value="">A-</option>
                        <option value="">B+</option>
                        <option value="">B-</option>
                        <option value="">O+</option>
                        <option value="">O-</option>
                        <option value="">AB+</option>
                        <option value="">AB-</option>
                    </select>
                </div>

                <div>
                    <button
                        class="hover:shadow-form w-full rounded-md bg-[#6A64F1] py-3 px-8 text-center text-base font-semibold text-white outline-none">
                        Registrar
                    </button>
                </div>
            </form>
        </div>
    </div>
</template>
