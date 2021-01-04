#
# Build stage
#

# Use node:alpine to build static files
FROM node:alpine as build-site

# Create app directory
WORKDIR /usr/src/app

# Install other dependencies via apk
RUN apk update && apk add python g++ make && rm -rf /var/cache/apk/*

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY package*.json ./

RUN npm install

# Bundle app source
COPY . .

# Build static files
RUN npm run build

#
# Package stage
#

# Use nginx alpine for minimal image size
FROM nginx:alpine as build-server

# Copy static files from build-side to build-server
COPY --from=build-site /usr/src/app/dist /usr/share/nginx/html
RUN rm /etc/nginx/conf.d/default.conf
#COPY nginx/nginx.conf /etc/nginx/conf.d
COPY nginx/nginx.conf.template /etc/nginx/templates/
EXPOSE 80
#CMD ["nginx", "-g", "daemon off;"]
CMD ["/bin/sh" , "-c" , "envsubst '${API_HOST} ${API_PORT}' < /etc/nginx/templates/nginx.conf.template > /etc/nginx/conf.d/nginx.conf && exec nginx -g 'daemon off;'"]