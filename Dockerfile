FROM python:3.9-buster

RUN mkdir -p /opt/petclinic-selenium

WORKDIR /opt/petclinic-selenium


RUN apt-get update && apt-get install -y \
	apt-transport-https \
	ca-certificates \
	curl \
	gnupg \
    zip \
	--no-install-recommends \
	&& curl -sSL https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
	&& echo "deb https://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
	&& apt-get update && apt-get install -y \
	google-chrome-stable \
	fontconfig \
	fonts-ipafont-gothic \
	fonts-wqy-zenhei \
	fonts-thai-tlwg \
	fonts-kacst \
	fonts-symbola \
	fonts-noto \
	fonts-freefont-ttf \
	--no-install-recommends \
    && curl -sO http://chromedriver.storage.googleapis.com/91.0.4472.19/chromedriver_linux64.zip \
    && unzip chromedriver_linux64.zip \
    && mv chromedriver /usr/bin \
	&& apt-get purge --auto-remove -y curl gnupg zip \
	&& rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install -r requirements.txt


ENTRYPOINT [ "python" ]
CMD [ "main.py"]
#ENTRYPOINT ["tail", "-f", "/dev/null"]
