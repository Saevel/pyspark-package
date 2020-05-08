spark-submit \
 --jars jvm-libs/spark-redis_2.12-2.4.2.jar \
 --jars jvm-libs/jedis-3.2.0.jar \
 --py-files "conf/$2.json" \
 --py-files libs.zip \
 --master $1 src/main.py \
 --env $2