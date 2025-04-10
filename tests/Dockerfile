FROM python:3.10-slim

# Установим зависимости
RUN apt-get update && apt-get install -y \
    wget curl unzip gnupg ca-certificates \
    libglib2.0-0 libnss3 libgconf-2-4 libxss1 libappindicator1 \
    libasound2 libatk-bridge2.0-0 libcups2 libxkbcommon0 libxcomposite1 \
    libxi6 libxtst6 fonts-liberation xdg-utils libgbm1 \
    firefox-esr chromium-driver chromium \
    && rm -rf /var/lib/apt/lists/*

# Установим geckodriver (для Firefox)
RUN GECKO_VERSION=$(curl -s https://api.github.com/repos/mozilla/geckodriver/releases/latest | grep tag_name | cut -d '"' -f 4) && \
    wget https://github.com/mozilla/geckodriver/releases/download/$GECKO_VERSION/geckodriver-$GECKO_VERSION-linux64.tar.gz && \
    tar -xvzf geckodriver-$GECKO_VERSION-linux64.tar.gz && \
    mv geckodriver /usr/local/bin/ && chmod +x /usr/local/bin/geckodriver && \
    rm geckodriver-$GECKO_VERSION-linux64.tar.gz

# Копируем зависимости
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Копируем весь проект
COPY . /tests
WORKDIR /tests