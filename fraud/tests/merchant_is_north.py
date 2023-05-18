### tests/transaction_amount_is_high.py ###
from fraud.features.on_demand_feature_views.transaction_latitudinal_hemisphere import transaction_hemisphere
import pytest

@pytest.fixture
def location_request():
    return {"merchant_latitude":"47.603230"}

def test_if_merchant_is_north(location_request):
    actual = transaction_hemisphere.test_run(location_request=location_request)
    print(actual)
    assert actual == {"transaction_latitudinal_hemisphere": "North"}
