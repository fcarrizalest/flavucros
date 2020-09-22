FROM node:14.11
WORKDIR /code
COPY package.json package.json
COPY webpack.mix.js webpack.mix.js
RUN npm install
CMD ["npm", "run","watch"]