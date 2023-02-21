FROM node:16-alpine

WORKDIR /code/house_website/

COPY package*.json /code/house_website/
RUN npm install

COPY . /code/house_website/

CMD ["npm", "start"]