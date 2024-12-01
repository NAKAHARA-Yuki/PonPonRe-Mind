FROM node:14-alpine

WORKDIR /app

COPY package.json ./

# 開発環境として設定
ENV NODE_ENV=development

# すべての依存関係をインストール
RUN npm install

COPY . .

EXPOSE 8080

CMD [ "npm", "run", "serve" ]
