def analyze_product(product):
    margin = product.price - product.cost
    score = 0

    # Margen
    if margin > 50:
        score += 30
    elif margin > 20:
        score += 20
    else:
        score += 10

    # Competencia
    if product.competition == "low":
        score += 25
    elif product.competition == "medium":
        score += 15
    else:
        score += 5

    # Demanda
    if product.demand == "high":
        score += 25
    elif product.demand == "medium":
        score += 15
    else:
        score += 5

    # Envío
    if product.shipping_days <= 7:
        score += 20
    else:
        score += 10

    if score > 70:
        risk = "low"
    elif score > 40:
        risk = "medium"
    else:
        risk = "high"

    return {
        "name": product.name,
        "margin": margin,
        "score": score,
        "risk": risk
    }
