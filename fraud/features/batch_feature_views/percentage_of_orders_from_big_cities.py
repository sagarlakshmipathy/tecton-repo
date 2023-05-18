from tecton import batch_feature_view, FilteredSource, Aggregation, materialization_context
from datetime import datetime, timedelta
from fraud.data_sources.transactions import transactions_batch
from fraud.data_sources.fraud_users import fraud_users_batch
from fraud.entities import merchant

users_batch = fraud_users_batch
merchant_entity = merchant

# @batch_feature_view(
#     sources=[transactions_batch, fraud_users_batch],
#     entities=[merchant],
#     mode='spark_sql',
#     ttl=timedelta(days=2),
#     online=True,
#     offline=True,
#     feature_start_time=datetime(2022, 8, 1),
#     batch_schedule=timedelta(days=1),
#     # incremental_backfills=True,
#     owner='18vidhyasagar@gmail.com',
#     description='Finding the percentage of orders from big cities in the last rolling week, updated daily.'
# )

# def percentage_of_orders_from_big_cities(transactions_batch, users_batch, context=materialization_context()):
#     return f'''
#     SELECT 
#         DATE_TRUNC('hour', txn.timestamp) AS aggregated_hour,
#         --TO_TIMESTAMP("{context.end_time}") - INTERVAL 1 HOUR as TIMESTAMP,
#         --DATE_TRUNC('hour', TO_TIMESTAMP("{context.end_time}")) as TIMESTAMP,
#         ROUND(COUNT (DISTINCT txn.transaction_id) FILTER(WHERE usr.city_pop > 10000)::FLOAT * 100.0 / COUNT(DISTINCT txn.transaction_id), 2) as percentage_of_orders_from_big_cities,
#         txn.merchant
#     FROM {transactions_batch} as txn
#     JOIN {users_batch} as usr
#     ON txn.user_id = usr.user_id
#     WHERE TIMESTAMP >= TO_TIMESTAMP("{context.start_time}") - INTERVAL 6 DAYS
#     AND TIMESTAMP < TO_TIMESTAMP("{context.end_time}")
#     GROUP BY aggregated_hour, txn.merchant
#     '''


from tecton import batch_feature_view, materialization_context

@batch_feature_view(
    sources=[transactions_batch, users_batch],
    entities=[merchant_entity],
    mode='spark_sql',
    ttl=timedelta(days=2),
    online=True,
    offline=True,
    feature_start_time=datetime(2022, 8, 1),
    batch_schedule=timedelta(days=1),
    # incremental_backfills=True,
    owner='18vidhyasagar@gmail.com',
    description='Finding the percentage of orders from big cities in the last rolling week, updated daily.'
)
def percentage_of_orders_from_big_cities(transactions_batch, users_batch, context=materialization_context()):
    return f'''
    SELECT 
        DATE_TRUNC('hour', txn.timestamp) AS aggregated_hour,
        --TO_TIMESTAMP("{context.end_time}") - INTERVAL 1 HOUR as TIMESTAMP,
        --DATE_TRUNC('hour', TO_TIMESTAMP("{context.end_time}")) as TIMESTAMP,
        ROUND(COUNT (DISTINCT txn.transaction_id) FILTER(WHERE usr.city_pop > 10000)::FLOAT * 100.0 / COUNT(DISTINCT txn.transaction_id), 2) as percentage_of_orders_from_big_cities,
        txn.merchant
    FROM {transactions_batch} as txn
    JOIN {users_batch} as usr
    ON txn.user_id = usr.user_id
    WHERE TIMESTAMP >= TO_TIMESTAMP("{context.start_time}") - INTERVAL 6 DAYS
    AND TIMESTAMP < TO_TIMESTAMP("{context.end_time}")
    GROUP BY aggregated_hour, txn.merchant
    '''