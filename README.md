# drip-search
Information Retireval system for clothing products.

# set-up

To run frontend:<br/>
yarn install; yarn serve<br/>
To run backend:<br/>
yarn install; node server.js<br/>

The appication needs Carrot2 clustering engine running on port 8880, to setup refer to [their documentation](https://carrot2.github.io/release/latest).<br/>
Once correctly installed: /dcs --port 8880


To scrape all the sites:<br/>
scrapy crawl supreme -O ../results/supreme.json<br/>
scrapy crawl bape -O ../results/bape.json<br/>
scrapy crawl farfetch -O ../results/farfetch.json<br/>
