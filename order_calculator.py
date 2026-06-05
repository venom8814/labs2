def calculate_order(price: float, quantity: int,
                    discount: float, delivery_type: str) -> float:

    if price < 0:
        raise ValueError("Цена не может быть отрицательной (price < 0)")
    if quantity < 0:
        raise ValueError("Количество не может быть отрицательным (quantity < 0)")
    if not (0 <= discount <= 100):
        raise ValueError("Скидка должна быть в диапазоне от 0 до 100")

    base_cost           = price * quantity
    discount_amount     = base_cost * (discount / 100)
    cost_after_discount = base_cost - discount_amount

    if cost_after_discount > 10_000:
        delivery_cost = 0
    else:
        if delivery_type == "standard":
            delivery_cost = 300
        elif delivery_type == "express":
            delivery_cost = 600
        else:
            raise ValueError(f"Неизвестный тип доставки: '{delivery_type}'")

    return cost_after_discount + delivery_cost
