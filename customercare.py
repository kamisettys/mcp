from mcp.server.fastmcp import FastMCP

from customers import CUSTOMERS
from orders import ORDERS
from restaurents import RESTAURANTS

mcp = FastMCP(name="swiggy_mcp", website_url="https://github.com/kamisettys/Generative-AI-phase1")


# tools
@mcp.tool()
def get_customer_summary(customer_id: str) -> dict | None:
    """
    Retrieve a customer's full information based on their customer ID.

    Parameters
    ----------
    customer_id : str
        Unique identifier of the customer to search for.

    Returns
    -------
    dict | None
        The customer record if found, otherwise None.
    """
    for customer in CUSTOMERS:
        if customer["customerId"] == customer_id:
            return customer
    return None


@mcp.tool()
def get_order_information(order_id: str) -> dict | None:
    """
    Retrieve detailed order information for a given order ID.

    Parameters
    ----------
    order_id : str
        Unique identifier of the order to search for.

    Returns
    -------
    dict | None
        The order record if found, otherwise None.
    """
    for order in ORDERS:
        if order["orderId"] == order_id:
            return order
    return None


@mcp.tool()
def get_restuarent_information(restaurant_id: str) -> dict | None:
    """
    Retrieve restaurant details based on the restaurant ID.

    Parameters
    ----------
    restaurant_id : str
        Unique identifier of the restaurant to search for.

    Returns
    -------
    dict | None
        The restaurant record if found, otherwise None.
    """
    for restaurant in RESTAURANTS:
        if restaurant["restaurantId"] == restaurant_id:
            return restaurant
    return None


# resources
@mcp.resource("policy://refund")
def get_refund_policy():
    """
    Load and return the refund policy text from the markdown file.

    Returns
    -------
    str
        The full contents of 'refundpolicy.md' as a single string.
    """
    lines = []
    with open('refundpolicy.md') as refund:
        lines = refund.readlines()
    return "\n".join(lines)


@mcp.resource("complaint://{ctype}")
def get_complain_resolution(ctype) -> str:
    """
    Load and return complaint resolution guidelines based on complaint type.

    Parameters
    ----------
    ctype : str
        The complaint category requested (e.g., 'late_delivery').

    Returns
    -------
    str
        The full contents of 'latetimedeliverypolicy.md' as a single string.
    """
    lines = []
    with open('latetimedeliverypolicy.md') as complain:
        lines = complain.readlines()
    return "\n".join(lines)


if __name__ == "__main__":
    mcp.run(transport="stdio")