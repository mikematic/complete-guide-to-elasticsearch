curl -H "Content-Type: application/json" -XPOST "http://localhost:9200/ecommerce/product/_bulk?pretty" --data-binary "@products-bulk.json" 
