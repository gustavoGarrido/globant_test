FROM python:3.8.10

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt



CMD ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]


# RUN rm -rf node_modules 

# RUN npm install
# RUN npm install -g nodemon
# RUN npm install pm2 -g
# RUN npm install -g typescript
# RUN tsc

# CMD pm2-runtime start config_pm2.json --env production
# CMD pm2 start config_pm2.json --env production
# CMD npm run dev

# EXPOSE 3000

# RUN apt update

# RUN apt-get install curl
# RUN curl -sL https://deb.nodesource.com/setup_16.x -o nodesource_setup.sh
# RUN bash nodesource_setup.sh
# RUN apt-get install -y nodejs
# # RUN apt install -y npm
# RUN npm install -g @angular/cli
# RUN npm install

# RUN ng build
# RUN cp -r ./dist/crm-gg-frontend/* /usr/local/apache2/htdocs/

# VOLUME /usr/local/apache2/htdocs/


# EXPOSE 4200
