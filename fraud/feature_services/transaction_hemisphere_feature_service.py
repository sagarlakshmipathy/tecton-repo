from tecton import FeatureService
from fraud.features.on_demand_feature_views.transaction_latitudinal_hemisphere import transaction_hemisphere


transaction_hemisphere_feature_service = FeatureService(
    name="transaction_hemisphere_feature_service",
    prevent_destroy=False,  
    online_serving_enabled=True,
    features=[
        transaction_hemisphere
    ]
)