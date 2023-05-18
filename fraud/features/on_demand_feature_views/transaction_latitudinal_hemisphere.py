from tecton import RequestSource, on_demand_feature_view
from tecton.types import String, Field, Float64

request_schema = [Field("merchant_latitude", String)]
location_request = RequestSource(schema=request_schema)
output_schema = [Field("transaction_latitudinal_hemisphere", String)]


@on_demand_feature_view(
    sources=[location_request],
    mode="python",
    schema=output_schema,
    description="Given a merchant latitude, find the latitudinal hemisphere of the transaction",
)

def transaction_hemisphere(location_request):
    location_request["merchant_latitude"] = float(location_request["merchant_latitude"])
    if location_request["merchant_latitude"] > 0:
        hemisphere = "North"
    else:
        hemisphere = "South"
    
    return {"transaction_latitudinal_hemisphere": hemisphere}