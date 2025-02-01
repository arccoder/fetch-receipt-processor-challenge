# Receipts for testing APIs
morning_200 = {
    "retailer": "Walgreens",
    "purchaseDate": "2022-01-02",
    "purchaseTime": "08:13",
    "total": "2.65",
    "items": [
        {"shortDescription": "Pepsi - 12-oz", "price": "1.25"},
        {"shortDescription": "Dasani", "price": "1.40"},
    ],
}
simple_retailer_400 = {
    "retailer": "Target$",
    "purchaseDate": "2022-01-02",
    "purchaseTime": "13:13",
    "total": "1.25",
    "items": [{"shortDescription": "Pepsi - 12-oz", "price": "1.25"}],
}
simple_purchaseDate_400 = {
    "retailer": "Target",
    "purchaseDate": "01/02/2022",
    "purchaseTime": "13:13",
    "total": "1.25",
    "items": [{"shortDescription": "Pepsi - 12-oz", "price": "1.25"}],
}
simple_purchaseTime_400 = {
    "retailer": "Target",
    "purchaseDate": "2022-01-02",
    "purchaseTime": "13.1300",
    "total": "1.25",
    "items": [{"shortDescription": "Pepsi - 12-oz", "price": "1.25"}],
}
simple_total_400 = {
    "retailer": "Target",
    "purchaseDate": "2022-01-02",
    "purchaseTime": "13:13",
    "total": "125",
    "items": [{"shortDescription": "Pepsi - 12-oz", "price": "1.25"}],
}
simple_item_desp_400 = {
    "retailer": "Target",
    "purchaseDate": "2022-01-02",
    "purchaseTime": "13:13",
    "total": "1.25",
    "items": [{"shortDescription": "Pepsi : 12-oz", "price": "125"}],
}
simple_item_price_400 = {
    "retailer": "Target",
    "purchaseDate": "2022-01-02",
    "purchaseTime": "13:13",
    "total": "1.25",
    "items": [{"shortDescription": "Pepsi - 12-oz", "price": "125"}],
}
simple_200 = {
    "retailer": "Target",
    "purchaseDate": "2022-01-02",
    "purchaseTime": "13:13",
    "total": "1.25",
    "items": [{"shortDescription": "Pepsi - 12-oz", "price": "1.25"}],
}
simple_200 = {
    "retailer": "Target",
    "purchaseDate": "2022-01-02",
    "purchaseTime": "13:13",
    "total": "1.25",
    "items": [{"shortDescription": "Pepsi - 12-oz", "price": "1.25"}],
}
simple_rules_retailer = {
    "retailer": "abc123&",
    "purchaseDate": "2022-02-02",
    "purchaseTime": "13:13",
    "total": "1.23",
    "items": [{"shortDescription": "Pepsi", "price": "10.00"}],
}
simple_rules_total00 = {
    "retailer": "-&-",
    "purchaseDate": "2022-02-02",
    "purchaseTime": "13:13",
    "total": "1.00",
    "items": [{"shortDescription": "Pepsi", "price": "10.00"}],
}
simple_rules_x25cents = {
    "retailer": "-&-",
    "purchaseDate": "2022-02-02",
    "purchaseTime": "13:13",
    "total": "1.50",
    "items": [{"shortDescription": "Pepsi", "price": "10.00"}],
}
simple_rules_items = {
    "retailer": "-&-",
    "purchaseDate": "2022-02-02",
    "purchaseTime": "13:13",
    "total": "1.23",
    "items": [
        {"shortDescription": "Pepsi", "price": "1.25"},
        {"shortDescription": "Dasani0", "price": "1.40"},
    ],
}
simple_rules_evendes = {
    "retailer": "-&-",
    "purchaseDate": "2022-02-02",
    "purchaseTime": "13:13",
    "total": "1.23",
    "items": [
        {"shortDescription": "Dasani", "price": "20.00"},
    ],
}
simple_rules_oddday = {
    "retailer": "-&-",
    "purchaseDate": "2022-02-01",
    "purchaseTime": "13:13",
    "total": "1.23",
    "items": [{"shortDescription": "Pepsi", "price": "10.00"}],
}
simple_rules_3pm = {
    "retailer": "-&-",
    "purchaseDate": "2022-02-02",
    "purchaseTime": "15:00",
    "total": "1.23",
    "items": [{"shortDescription": "Pepsi", "price": "10.00"}],
}
