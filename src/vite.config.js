import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import Components from 'unplugin-vue-components/vite'
import {BootstrapVueNextResolver} from 'bootstrap-vue-next'

export default defineConfig({
    plugins: [
      vue(),
      Components({
        resolvers: [BootstrapVueNextResolver()],
      }), ],
    server: {
      proxy: {
        '/api': {
          target: 'http://localhost:5000',  // Flask backend URL
          changeOrigin: true,
          rewrite: (path) => path.replace(/^\/api/, ''),  // Optional path rewrite
        },
      },
    },
  });