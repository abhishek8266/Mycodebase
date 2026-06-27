import argparse
from bot.client import BinanceClient
from bot.orders import OrderManager


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:

        client = BinanceClient()
        order_manager = OrderManager(client)

        response = order_manager.create_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price
        )

        print("\n==============================")
        print("ORDER RESPONSE")
        print("==============================\n")

        print(response)

        print("\n==============================")
        print("SUMMARY")
        print("==============================")

        print("Symbol:", args.symbol)
        print("Side:", args.side)
        print("Type:", args.type)
        print("Quantity:", args.quantity)

    except Exception as e:

        print("\nERROR:", str(e))


if __name__ == "__main__":
    main()