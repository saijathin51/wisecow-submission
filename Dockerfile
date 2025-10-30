FROM ubuntu:24.04 

WORKDIR /wisecow
#installing pre requesties
RUN apt update && apt install fortune-mod cowsay netcat-openbsd -y
# Setting Env 
ENV PATH="$PATH:/usr/games"

COPY wisecow.sh .

RUN chmod +x wisecow.sh
# Exposing the post
EXPOSE 4499

CMD ["./wisecow.sh"]
