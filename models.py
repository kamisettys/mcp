

# this moduel has pydantic models
from pydantic import BaseModel, Field
from typing import Annotated, Literal



class Restaurant(BaseModel):
    """Represents the restaurant fulfilling the order.

    Attributes:
        name (str): Name of the restaurant.
        restaurantId (str): Unique identifier for the restaurant.
        location (str): Physical location of the restaurant.
        rating (float): Rating of the restaurant.
        deliveryTime (str): Estimated delivery time for the order.
    """

    name: Annotated[str, Field(description="Restaurant name")]
    restaurantId: Annotated[str, Field(description="Restaurant ID")]
    location: Annotated[str, Field(description="Restaurant location")]
    rating: Annotated[float, Field(description="Restaurant rating")]
    deliveryTime: Annotated[str, Field(description="Estimated delivery time")]


class OrderItem(BaseModel):
    """Represents an item included in the order.

    Attributes:
        name (str): Name of the item.
        quantity (int): Quantity ordered.
        price (float): Price of the item.
        customizations (list[str]): List of customizations applied to the item.
    """

    name: Annotated[str, Field(description="Item name")]
    quantity: Annotated[int, Field(description="Quantity ordered")]
    price: Annotated[float, Field(description="Price of the item")]
    customizations: Annotated[list[str], Field(description="Customizations applied")]


class Pricing(BaseModel):
    """Represents the pricing breakdown for the order.

    Attributes:
        itemTotal (float): Total cost of all items.
        deliveryFee (float): Delivery charges applied.
        platformFee (float): Platform service fee.
        gst (float): GST applied to the order.
        discount (float): Discount applied to the order.
        totalAmount (float): Final payable amount.
    """

    itemTotal: Annotated[float, Field(description="Total cost of items")]
    deliveryFee: Annotated[float, Field(description="Delivery charges")]
    platformFee: Annotated[float, Field(description="Platform service fee")]
    gst: Annotated[float, Field(description="GST applied")]
    discount: Annotated[float, Field(description="Discount applied")]
    totalAmount: Annotated[float, Field(description="Final payable amount")]


class Payment(BaseModel):
    """Represents payment information for the order.

    Attributes:
        method (str): Payment method used.
        transactionId (str): Unique identifier for the payment transaction.
        status (Literal): Payment status (paid or notpaid).
    """

    method: Annotated[str, Field(description="Payment method used")]
    transactionId: Annotated[str, Field(description="Transaction ID")]
    status: Annotated[Literal["paid", "notpaid"], Field(description="Payment status")]


class DeliveryAddress(BaseModel):
    """Represents the delivery address for the order.

    Attributes:
        label (str): Label for the address (e.g., Home, Office).
        address (str): Full delivery address.
        city (str): City where the order is delivered.
        pincode (str): Postal code of the delivery location.
    """

    label: Annotated[str, Field(description="Address label")]
    address: Annotated[str, Field(description="Full delivery address")]
    city: Annotated[str, Field(description="City of delivery")]
    pincode: Annotated[str, Field(description="Postal code")]


class DeliveryPartner(BaseModel):
    """Represents the delivery partner assigned to the order.

    Attributes:
        name (str): Name of the delivery partner.
        rating (float): Rating of the delivery partner.
        phone (str): Contact number of the delivery partner.
    """

    name: Annotated[str, Field(description="Delivery partner name")]
    rating: Annotated[float, Field(description="Delivery partner rating")]
    phone: Annotated[str, Field(description="Delivery partner phone number")]


class Timeline(BaseModel):
    """Represents the timeline of the order from placement to delivery.

    Attributes:
        orderPlaced (str): Timestamp when the order was placed.
        restaurantAccepted (str): Timestamp when the restaurant accepted the order.
        foodReady (str): Timestamp when the food was prepared.
        outForDelivery (str): Timestamp when the order was dispatched.
        delivered (str): Timestamp when the order was delivered.
    """

    orderPlaced: Annotated[str, Field(description="Order placed timestamp")]
    restaurantAccepted: Annotated[str, Field(description="Restaurant acceptance timestamp")]
    foodReady: Annotated[str, Field(description="Food ready timestamp")]
    outForDelivery: Annotated[str, Field(description="Out for delivery timestamp")]
    delivered: Annotated[str, Field(description="Delivered timestamp")]


class Ratings(BaseModel):
    """Represents customer ratings and review for the order.

    Attributes:
        food (float): Rating for the food quality.
        delivery (float): Rating for the delivery experience.
        review (str): Written review provided by the customer.
    """

    food: Annotated[float, Field(description="Food rating")]
    delivery: Annotated[float, Field(description="Delivery rating")]
    review: Annotated[str, Field(description="Customer review text")]


class Order(BaseModel):
    """Represents a complete customer order with all associated details.

    Attributes:
        orderId (str): Unique identifier for the order.
        customerId (str): Unique identifier for the customer.
        customerName (str): Name of the customer.
        orderDate (str): Timestamp when the order was placed.
        status (str): Current status of the order.
        restaurant (Restaurant): Restaurant fulfilling the order.
        items (list[OrderItem]): List of items included in the order.
        pricing (Pricing): Pricing breakdown for the order.
        payment (Payment): Payment details for the order.
        deliveryAddress (DeliveryAddress): Delivery address information.
        deliveryPartner (DeliveryPartner): Assigned delivery partner details.
        timeline (Timeline): Timeline events for the order.
        ratings (Ratings): Customer ratings and review.
    """

    orderId: Annotated[str, Field(description="Order ID")]
    customerId: Annotated[str, Field(description="Customer ID")]
    customerName: Annotated[str, Field(description="Customer name")]
    orderDate: Annotated[str, Field(description="Order timestamp")]
    status: Annotated[str, Field(description="Order status")]
    restaurant: Annotated[Restaurant, Field(description="Restaurant details")]
    items: Annotated[list[OrderItem], Field(description="List of ordered items")]
    pricing: Annotated[Pricing, Field(description="Pricing details")]
    payment: Annotated[Payment, Field(description="Payment details")]
    deliveryAddress: Annotated[DeliveryAddress, Field(description="Delivery address")]
    deliveryPartner: Annotated[DeliveryPartner, Field(description="Delivery partner details")]
    timeline: Annotated[Timeline, Field(description="Order timeline")]
    ratings: Annotated[Ratings, Field(description="Customer ratings and review")]

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