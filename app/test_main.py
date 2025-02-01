import re
import pytest
from fastapi import status
from fastapi.testclient import TestClient

import models
import receipts2test
from main import app


@pytest.mark.parametrize(
    "item, status_code",
    [
        # Valid receipt
        (receipts2test.morning_200, 200),
        # Retailer name pattern check fails
        (receipts2test.simple_retailer_400, 400),
        # Purchase date pattern check fails
        (receipts2test.simple_purchaseDate_400, 400),
        # Purchase time pattern check fails
        (receipts2test.simple_purchaseTime_400, 400),
        # Total pattern check fails
        (receipts2test.simple_total_400, 400),
        # Item description pattern check fails
        (receipts2test.simple_item_desp_400, 400),
        # Item price pattern check fails
        (receipts2test.simple_item_price_400, 400),
    ],
)
def test_processReceipts(item: models.Receipt, status_code: int):
    """
    Test /receipts/process
    """
    with TestClient(app) as client:
        response = client.post("/receipts/process", json=item)
        data = response.json()

        assert response.status_code == status_code

        if response.status_code == status.HTTP_200_OK:
            assert "id" in data
            assert re.fullmatch(r"^[\w\s\&-]+$", data["id"])


@pytest.mark.parametrize(
    "item, points",
    [
        # Retailer name with 6 alphanumerics
        (receipts2test.simple_rules_retailer, 6),
        # Total w no cents, that makes it a multiple of a quarter
        # 50 + 25 = 75
        (receipts2test.simple_rules_total00, 75),
        # Total mutiple of quarter
        (receipts2test.simple_rules_x25cents, 25),
        # Two items in the receipt
        (receipts2test.simple_rules_items, 5),
        # Item desp even and price $20 * 0.2 = 4
        (receipts2test.simple_rules_evendes, 4),
        # Odd date in date, 6
        (receipts2test.simple_rules_oddday, 6),
        # Purchase time between 2 and 4 pm
        (receipts2test.simple_rules_3pm, 10),
    ],
)
def test_checkPoints(item: models.Receipt, points: int):
    """
    Test rules for points calculation
    """
    with TestClient(app) as client:
        response = client.post("/receipts/process", json=item)
        data = response.json()

        assert response.status_code == status.HTTP_200_OK

        assert "id" in data
        assert re.fullmatch(r"^[\w\s\&-]+$", data["id"])

        pointsId = client.get(f"/receipts/{data["id"]}/points").json()
        assert pointsId["points"] == points


def test_getPointById():
    """
    Test /receipts/{id}/points
    """
    with TestClient(app) as client:

        # Process a receipt
        response = client.post(f"/receipts/process", json=receipts2test.simple_200)
        created_id = response.json()["id"]

        # Check if the receipt id exists
        response = client.get(f"/receipts/{created_id}/points")
        assert response.status_code == status.HTTP_200_OK
        if response.status_code == status.HTTP_200_OK:
            # Check the receipts reatiler name
            data = response.json()
            assert isinstance(data["points"], int)

        # Check if this modified receipt id does not exists
        modified_id = created_id[:-2] + "az"
        response = client.get(f"/receipts/{modified_id}/points")
        assert response.status_code == status.HTTP_404_NOT_FOUND
