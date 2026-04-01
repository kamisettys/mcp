

# this moduel has pydantic models
from pydantic import BaseModel, Field
from typing import Annotated, Literal


class Item(BaseModel):
    """Represents an item included in a customer's order.

    Attributes:
        Item_id (int): Unique identifier for the item. Must be greater than 0.
        name (str): Name of the item.
        quantity (int): Quantity of the item ordered. Must be greater than 1.
    """

    Item_id: Annotated[int, Field(gt=0)]
    name: Annotated[str, Field(description="Item name")]
    quantity: Annotated[int, Field(gt=1)]


class Pricing(BaseModel):
    """Represents the pricing breakdown for an order.

    Attributes:
        itemTotal (float): Total cost of all items. Must be greater than 0.
        deliveryFee (float): Delivery charges applied to the order.
        gst (float): GST fee applied to the order.
        totalAmount (float): Final payable amount including all charges.
    """

    itemTotal: Annotated[float, Field(gt=0, description="Total price of the item")]
    deliveryFee: Annotated[float, Field(gt=0, description="delivery charges")]
    gst: Annotated[float, Field(gt=0, description="GST fee")]
    totalAmount: Annotated[float, Field(gt=0, description="Total amount of the order")]


class Restaurant(BaseModel):
    """Represents the restaurant fulfilling the order.

    Attributes:
        name (str): Name of the restaurant.
        restaurantId (str): Unique identifier for the restaurant.
        location (str): Physical location of the restaurant.
        rating (float): Rating of the restaurant. Must be greater than 0.
        deliveryTime (str): Estimated delivery time for the order.
    """

    name: Annotated[str, Field(description="Restaurant name")]
    restaurantId: Annotated[str, Field(description="Restaurant ID")]
    location: Annotated[str, Field(description="Restaurant location")]
    rating: Annotated[float, Field(gt=0, description="Restaurant rating")]
    deliveryTime: Annotated[str, Field(description="Estimated delivery time")]


class Payment(BaseModel):
    """Represents payment information for the order.

    Attributes:
        method (str): Payment method used (e.g., UPI, card, cash).
        transactionId (str): Unique identifier for the payment transaction.
        status (Literal): Payment status, either 'paid' or 'notpaid'.
    """

    method: Annotated[str, Field(description="Payment method used for the order")]
    transactionId: Annotated[str, Field(description="Unique identifier for the payment transaction")]
    status: Annotated[Literal["paid", "notpaid"], Field(description="Payment status")]


class Delivery_Address(BaseModel):
    """Represents the delivery address for the order.

    Attributes:
        label (Literal): Label for the address (Home or office).
        address (str): Full delivery address.
        city (str): City where the order is delivered.
        pincode (int): ZIP code for the delivery location.
    """

    label: Annotated[Literal["Home", "office"], Field(description="label for delivery")]
    address: Annotated[str, Field(description="address for delivery")]
    city: Annotated[str, Field(description="City for delivery")]
    pincode: Annotated[int, Field(description="ZIP code for delivery")]


class Delivery_Partner(BaseModel):
    """Represents the delivery partner assigned to the order.

    Attributes:
        name (str): Name of the delivery partner.
        rating (float): Rating of the delivery partner. Must be greater than 0.
        phone (str): Contact number of the delivery partner.
    """

    name: Annotated[str, Field(description="Name of the delivery partner")]
    rating: Annotated[float, Field(gt=0, description="Rating of the delivery partner")]
    phone: Annotated[str, Field(description="Contact number of the delivery partner")]


class TimeLine(BaseModel):
    """Represents the timeline of the order from placement to delivery.

    Attributes:
        orderPlaced (str): Timestamp when the order was placed.
        restaurantAccepted (str): Timestamp when the restaurant accepted the order.
        foodReady (str): Timestamp when the food was prepared.
        outForDelivery (str): Timestamp when the order was dispatched.
        delivered (str): Timestamp when the order was delivered.
    """

    orderPlaced: Annotated[str, Field(description="Timestamp when the order was placed")]
    restaurantAccepted: Annotated[str, Field(description="Timestamp when the restaurant accepted the order")]
    foodReady: Annotated[str, Field(description="Timestamp when the food is ready")]
    outForDelivery: Annotated[str, Field(description="Timestamp when the order is out for delivery")]
    delivered: Annotated[str, Field(description="Timestamp when the order is delivered")]


class Ratings(BaseModel):
    """Represents customer ratings and review for the order.

    Attributes:
        food (float): Rating for the food quality. Must be greater than 0.
        delivery (float): Rating for the delivery experience. Must be greater than 0.
        review (str): Written review provided by the customer.
    """

    food: Annotated[float, Field(gt=0, description="Rating for the food")]
    delivery: Annotated[float, Field(gt=0, description="Rating for the delivery")]
    review: Annotated[str, Field(description="Customer review for the order")]


class Order(BaseModel):
    """Represents a complete customer order with all associated details.

    Attributes:
        order_id (str): Unique identifier for the order.
        restaurant (list[Restaurant]): Restaurant fulfilling the order.
        status (Literal): Current status of the order.
        items (list[Item]): List of items included in the order.
        pricing (list[Pricing]): Pricing breakdown for the order.
        payment (list[Payment]): Payment details for the order.
        deliveryAddress (list[Delivery_Address]): Delivery address information.
        deliveryPartner (list[Delivery_Partner]): Assigned delivery partner details.
        timeline (list[TimeLine]): Timeline events for the order.
        ratings (list[Ratings]): Customer ratings and review.
    """

    order_id: Annotated[str, Field(description="Unique identifier for the order")]
    restaurant: Annotated[list[Restaurant], Field(description="Restaurant details")]
    status: Annotated[
        Literal["pending", "processing", "shipped", "delivered", "cancelled", "not_delivered"],
        Field(description="allowed statuses")
    ]
    items: Annotated[list[Item], Field(description="List of items in the order")]
    pricing: Annotated[list[Pricing], Field(description="Pricing details of the order")]
    payment: Annotated[list[Payment], Field(description="Payment details of the order")]
    deliveryAddress: Annotated[list[Delivery_Address], Field(description="Delivery address details of the order")]
    deliveryPartner: Annotated[list[Delivery_Partner], Field(description="Details of the delivery partner")]
    timeline: Annotated[list[TimeLine], Field(description="Timeline of the order")]
    ratings: Annotated[list[Ratings], Field(description="Customer ratings and review for the order")]

# customer informations
# from pydantic import BaseModel, Field
from typing import Annotated, Literal, List, Optional


class Profile(BaseModel):
    """Customer profile information."""

    name: Annotated[str, Field(description="Customer full name")]
    email: Annotated[str, Field(description="Customer email address")]
    phone: Annotated[str, Field(description="Customer phone number")]
    memberSince: Annotated[str, Field(description="Date when customer joined")]  # ISO date


class AccountStats(BaseModel):
    """Customer account statistics."""

    totalOrders: Annotated[int, Field(description="Total number of orders placed")]
    lifetimeValue: Annotated[float, Field(description="Total spend across all orders")]
    averageOrderValue: Annotated[float, Field(description="Average order value")]
    favoriteRestaurants: Annotated[List[str], Field(description="List of favorite restaurants")]
    preferredCuisines: Annotated[List[str], Field(description="Preferred cuisines")]
    savedAddresses: Annotated[int, Field(description="Number of saved addresses")]


class OrderItem(BaseModel):
    """Item inside a recent order."""

    name: Annotated[str, Field(description="Item name")]
    quantity: Annotated[int, Field(description="Quantity ordered")]
    price: Annotated[float, Field(description="Price of the item")]
    customizations: Annotated[List[str], Field(description="List of customizations applied")]


class Restaurant(BaseModel):
    """Restaurant details for an order."""

    name: Annotated[str, Field(description="Restaurant name")]
    restaurantId: Annotated[str, Field(description="Restaurant ID")]
    location: Annotated[str, Field(description="Restaurant location")]
    rating: Annotated[float, Field(description="Restaurant rating")]
    deliveryTime: Annotated[str, Field(description="Estimated delivery time")]


class Pricing(BaseModel):
    """Pricing breakdown for an order."""

    itemTotal: Annotated[float, Field(description="Total cost of items")]
    deliveryFee: Annotated[float, Field(description="Delivery charges")]
    platformFee: Annotated[float, Field(description="Platform service fee")]
    gst: Annotated[float, Field(description="GST applied")]
    discount: Annotated[float, Field(description="Discount applied")]
    totalAmount: Annotated[float, Field(description="Final payable amount")]


class Payment(BaseModel):
    """Payment details for an order."""

    method: Annotated[str, Field(description="Payment method used")]
    transactionId: Annotated[str, Field(description="Transaction ID")]
    status: Annotated[Literal["paid", "notpaid"], Field(description="Payment status")]


class DeliveryAddress(BaseModel):
    """Delivery address for an order."""

    label: Annotated[str, Field(description="Address label (Home/Office)")]
    address: Annotated[str, Field(description="Full delivery address")]
    city: Annotated[str, Field(description="City of delivery")]
    pincode: Annotated[str, Field(description="Postal code")]  # String in JSON


class DeliveryPartner(BaseModel):
    """Delivery partner assigned to the order."""

    name: Annotated[str, Field(description="Delivery partner name")]
    rating: Annotated[float, Field(description="Delivery partner rating")]
    phone: Annotated[str, Field(description="Delivery partner phone number")]


class Timeline(BaseModel):
    """Order timeline events."""

    orderPlaced: Annotated[str, Field(description="Order placed timestamp")]
    restaurantAccepted: Annotated[str, Field(description="Restaurant acceptance timestamp")]
    foodReady: Annotated[str, Field(description="Food ready timestamp")]
    outForDelivery: Annotated[str, Field(description="Out for delivery timestamp")]
    delivered: Annotated[str, Field(description="Delivered timestamp")]


class Ratings(BaseModel):
    """Customer ratings and review."""

    food: Annotated[float, Field(description="Food rating")]
    delivery: Annotated[float, Field(description="Delivery rating")]
    review: Annotated[str, Field(description="Customer review text")]


class RecentOrder(BaseModel):
    """Represents a single recent order."""

    orderId: Annotated[str, Field(description="Order ID")]
    orderDate: Annotated[str, Field(description="Order timestamp")]
    status: Annotated[str, Field(description="Order status")]
    restaurant: Annotated[Restaurant, Field(description="Restaurant details")]
    items: Annotated[List[OrderItem], Field(description="List of ordered items")]
    pricing: Annotated[Pricing, Field(description="Pricing details")]
    payment: Annotated[Payment, Field(description="Payment details")]
    deliveryAddress: Annotated[DeliveryAddress, Field(description="Delivery address")]
    deliveryPartner: Annotated[DeliveryPartner, Field(description="Delivery partner details")]
    timeline: Annotated[Timeline, Field(description="Order timeline")]
    ratings: Annotated[Ratings, Field(description="Customer ratings and review")]


class Preferences(BaseModel):
    """Customer food and ordering preferences."""

    dietaryRestrictions: Annotated[List[str], Field(description="Dietary restrictions")]
    favoriteItems: Annotated[List[str], Field(description="Favorite food items")]
    avoidIngredients: Annotated[List[str], Field(description="Ingredients to avoid")]
    spiceLevel: Annotated[str, Field(description="Preferred spice level")]


class Coupon(BaseModel):
    """Coupon available to the customer."""

    code: Annotated[str, Field(description="Coupon code")]
    description: Annotated[str, Field(description="Coupon description")]
    validUntil: Annotated[str, Field(description="Coupon expiry date")]


class LoyaltyRewards(BaseModel):
    """Customer loyalty reward details."""

    currentPoints: Annotated[int, Field(description="Current loyalty points")]
    pointsToNextReward: Annotated[int, Field(description="Points needed for next reward")]
    couponsAvailable: Annotated[List[Coupon], Field(description="Available coupons")]


class Customer(BaseModel):
    """Complete customer profile including orders, preferences, and rewards."""

    customerId: Annotated[str, Field(description="Customer ID")]
    profile: Annotated[Profile, Field(description="Customer profile details")]
    accountStats: Annotated[AccountStats, Field(description="Customer account statistics")]
    recentOrders: Annotated[List[RecentOrder], Field(description="List of recent orders")]
    preferences: Annotated[Preferences, Field(description="Customer preferences")]
    loyaltyRewards: Annotated[LoyaltyRewards, Field(description="Loyalty rewards information")]    