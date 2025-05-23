#チケット一枚あたりの価格
price = 500

#所持金
money = 3000

#チケットを購入するための関数を定義
def buyTicket(ticket_count, price, money):
    total_price = 0
    if ticket_count > 0:
        total_price = price * ticket_count
        if total_price <= money:
            return f"{total_price}円で{ticket_count}枚のチケットを購入しました！"
        else:
            return "所持金が不足しています！"
    else:
        return "購入するチケットの数量を入力してください！"

#購入するチケットの数量を入力する
ticket_count = int(input(f"いらっしゃいませ！\n購入するチケットの数量を入力してください（１枚{price}円）："))
print(buyTicket(ticket_count, price, money))