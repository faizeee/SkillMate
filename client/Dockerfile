# Stage 1: Build React app
FROM node:20-alpine AS builder

WORKDIR /app

ENV NODE_ENV=development

COPY client/package*.json ./

RUN npm install

COPY client .

RUN npm run build

# Stage 2: Serve with NGINX
FROM nginx:alpine

COPY --from=builder /app/dist /usr/share/nginx/html

EXPOSE 80

CMD [ "nginx","-g","daemon off;"]