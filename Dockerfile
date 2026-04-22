FROM nginx:alpine

COPY . /usr/share/nginx/html

# Cloud Run sends traffic to port 8080 (--port=8080). Default nginx image listens on 80.
RUN sed -i 's/listen 80;/listen 8080;/g' /etc/nginx/conf.d/default.conf && \
    sed -i 's/listen       80;/listen 8080;/g' /etc/nginx/conf.d/default.conf && \
    sed -i -E 's/listen[[:space:]]+80 default_server/listen 8080 default_server/g' /etc/nginx/conf.d/default.conf

EXPOSE 8080

CMD ["nginx", "-g", "daemon off;"]
