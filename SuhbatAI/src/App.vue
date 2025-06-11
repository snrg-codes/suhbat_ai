<template>
  <div class="container py-5 text-light cyber-bg">
    <h1 class="text-center mb-4 neon-text">Cyber AI Suhbat</h1>

    <form @submit.prevent="submit">
      <div class="row mb-3">
        <div class="col-md-4">
          <label class="form-label">Rol</label>
          <input v-model="rol" class="form-control cyber-input" placeholder="Masalan: Sistemniy administrator" />
        </div>
        <div class="col-md-4">
          <label class="form-label">Daraja</label>
          <input v-model="daraja" class="form-control cyber-input" placeholder="Masalan: junior" />
        </div>
        <div class="col-md-4">
          <label class="form-label">Ism</label>
          <input v-model="ism" class="form-control cyber-input" placeholder="Masalan: Pepe" />
        </div>
      </div>

      <div class="mb-3">
        <label class="form-label">Javobingizni yozing</label>
        <textarea v-model="javob" class="form-control cyber-input" rows="3"></textarea>
      </div>

      <button class="btn btn-outline-light neon-border" :disabled="loading">
        {{ loading ? 'Yuklanmoqda...' : 'Yuborish' }}
      </button>
    </form>

    <div v-if="response" class="mt-4 p-3 cyber-box">
      <h5 class="neon-text">AI javobi:</h5>
      <pre class="text-light">{{ response }}</pre>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { GoogleGenAI } from '@google/genai';

const rol = ref('');
const daraja = ref('');
const ism = ref('');
const javob = ref('');
const response = ref('');
const loading = ref(false);

const submit = async () => {
  loading.value = true;
  response.value = '';

  const ai = new GoogleGenAI({
    apiKey: import.meta.env.VITE_GEMINI_API_KEY,
  });

  const systemInstruction = `
Sen ${rol.value} mutaxassisi sifatida 10 yillik tajribaga egasan. 
Sen ${daraja.value} ${rol.value} lavozimiga ${ism.value} ismli mutaxassisni olish uchun suhbat jarayonidasan. 
Ketma-ket savollarni ber. Savollar soni 10 ta. Javoblar qoniqtirmasa, bu haqida yoz va davom et. 
Oxirida statistikani ber va 10 ballik tizimda bahola.
`;

  const res = await ai.models.generateContent({
    model: 'gemini-2.0-flash-lite',
    contents: [
      {
        role: 'user',
        parts: [{ text: javob.value }],
      },
    ],
    config: {
      responseMimeType: 'text/plain',
      systemInstruction: [{ text: systemInstruction }],
    },
  });

  response.value = res.response.text;
  loading.value = false;
};
</script>

<style>
.cyber-bg {
  background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
  min-height: 100vh;
}
.cyber-input {
  background-color: #1c1c2c;
  color: #0ff;
  border: 1px solid #0ff;
}
.cyber-input::placeholder {
  color: #77f;
}
.neon-text {
  color: #0ff;
  text-shadow: 0 0 5px #0ff, 0 0 10px #0ff;
}
.neon-border {
  border: 1px solid #0ff;
  box-shadow: 0 0 5px #0ff, 0 0 10px #0ff;
}
.cyber-box {
  background-color: #111122;
  border: 1px solid #0ff;
  border-radius: 8px;
  box-shadow: 0 0 8px #0ff;
}
</style>
