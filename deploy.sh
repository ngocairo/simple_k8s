docker build -t ngocairo/server:latest -t ngocairo/server:$VERSION .

docker push ngocairo/server:latest
docker push ngocairo/server:$VERSION

kubectl apply -f k8s_prod

kubectl set image deployment server-deployment server=ngocairo/server:$VERSION