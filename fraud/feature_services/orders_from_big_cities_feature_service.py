from tecton import FeatureService
from fraud.features.batch_feature_views.percentage_of_orders_from_big_cities import percentage_of_orders_from_big_cities


big_city_orders = FeatureService(
    name="orders_from_big_cities_feature_service",
    prevent_destroy=False,  
    online_serving_enabled=True,
    features=[
        percentage_of_orders_from_big_cities
    ]
)