# Etapa 1: Construcción (Build)
FROM node:20-alpine AS build-stage

WORKDIR /app

# Copiar archivos de dependencias
COPY package*.json ./

# Instalar dependencias
RUN npm install

ARG VITE_API_URL
ENV VITE_API_URL=$VITE_API_URL

# Copiar el resto del código
COPY . .

# Construir la aplicación para producción
RUN npm run build

# Etapa 2: Servir con Nginx
FROM nginx:alpine AS production-stage

# Copiar los archivos construidos desde la etapa anterior
# Vite por defecto genera la salida en la carpeta 'dist'
COPY --from=build-stage /app/dist /usr/share/nginx/html

# Exponer el puerto 80
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]