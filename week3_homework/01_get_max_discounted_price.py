# Q. 다음과 같이 숫자로 이루어진 배열이 두 개가 있다.
# 하나는 상품의 가격을 담은 배열이고, 하나는 쿠폰을 담은 배열이다.
# 쿠폰의 할인율에 따라 상품의 가격을 할인 받을 수 있다. 이 때,
# 최대한 할인을 많이 받는다면 얼마를 내야 하는가?
# 단, 할인쿠폰은 한 제품에 한 번씩만 적용 가능하다.


# 할인을 많이받으려면 어떻게 해야할까 : 가장 비싼거에 할인율이 높은 쿠폰을 사용
# 정렬 사용 sort

# 비싼가격을 높은 할인율로 할인받아야한다.
# 내림차순
shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):
    prices.sort(reverse=True)  # sort를 이용한 내림차순 정렬
    coupons.sort(reverse=True)

    price_index = 0
    coupon_index = 0
    max_price = 0

    # prices 리스트와 , coupons의 리스트 개수가 다르기때문에 while문을통해 비교
    while price_index < len(prices) and coupon_index < len(coupons):  #len을 통해 각 리스트 길이만큼 반복
        max_price += prices[price_index] * (100 - coupons[coupon_index]) / 100 # 40 ,20프로 할인된 가격 저장
                                                    # 할인률 계산
        price_index += 1 # 계산이 끝날때 한칸씩 이동
        coupon_index += 1 # 한칸씩 이동

    while price_index < len(prices): #위에서는 0 , 1 까지 실행이 완료되고 2000원만남아있기때문에 계산
        max_price += prices[price_index] #할인할 쿠폰이없기때문에 그대로 대입
        price_index += 1  # 한칸씩 이동

    return max_price


print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.
