"""
Reservation System Module with Traceability.

This module provides functionalities for managing hotels, customers, and
reservations, while ensuring data persistence through JSON files with backups.
"""

import json
import os
import unittest
import shutil
from datetime import datetime


# File management utility
def read_file(filename):
    """Reads JSON data from a file.
    Returns an empty list if the file doesn't exist."""
    if not os.path.exists(filename):
        return []
    with open(filename, 'r', encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def write_file(filename, data):
    """Writes data to a JSON file, replacing the existing content."""
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def append_file(filename, entry):
    """Appends an entry to the JSON file, ensuring traceability."""
    data = read_file(filename)
    data.append(entry)
    write_file(filename, data)


# Ensure JSON files exist before running any logic
for json_data_file in ['hotels.json', 'customers.json', 'reservations.json']:
    if not os.path.exists(json_data_file):
        write_file(json_data_file, [])  # Initialize if missing


class Hotel:
    """Represents a hotel entity with persistent storage."""

    FILE = 'hotels.json'

    def __init__(self, name, location):
        """Initializes a hotel with a name and location."""
        self.name = name
        self.location = location

    def save(self):
        """Saves the hotel to a persistent JSON file."""
        append_file(self.FILE, {'name': self.name, 'location': self.location})

    @staticmethod
    def delete(name):
        """Deletes a hotel by name from the persistent file."""
        hotels = read_file(Hotel.FILE)
        hotels = [hotel for hotel in hotels if hotel['name'] != name]
        write_file(Hotel.FILE, hotels)

    @staticmethod
    def list_hotels():
        """Returns a list of all stored hotels."""
        return read_file(Hotel.FILE)


class Customer:
    """Represents a customer entity with persistent storage."""

    FILE = 'customers.json'

    def __init__(self, name, email):
        """Initializes a customer with a name and email."""
        self.name = name
        self.email = email

    def save(self):
        """Saves the customer to a persistent JSON file."""
        append_file(self.FILE, {'name': self.name, 'email': self.email})

    @staticmethod
    def delete(name):
        """Deletes a customer by name from the persistent file."""
        customers = read_file(Customer.FILE)
        customers = [cust for cust in customers if cust['name'] != name]
        write_file(Customer.FILE, customers)

    @staticmethod
    def list_customers():
        """Returns a list of all stored customers."""
        return read_file(Customer.FILE)


class Reservation:
    """Represents a reservation entity with persistent storage."""

    FILE = 'reservations.json'

    def __init__(self, customer, hotel):
        """Initializes a reservation with a customer and hotel."""
        self.customer = customer
        self.hotel = hotel

    def save(self):
        """Saves the reservation to a persistent JSON file."""
        append_file(self.FILE, {'customer': self.customer,
                                'hotel': self.hotel})

    @staticmethod
    def cancel(customer):
        """Cancels a reservation by customer name."""
        reservations = read_file(Reservation.FILE)
        reservations = [res for res in reservations
                        if res['customer'] != customer]
        write_file(Reservation.FILE, reservations)

    @staticmethod
    def list_reservations():
        """Returns a list of all stored reservations."""
        return read_file(Reservation.FILE)


class TestReservationSystem(unittest.TestCase):
    """Unit tests for the Reservation System with file traceability."""

    def setUp(self):
        """Backs up JSON files before modifying them
        and ensures a clean state."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        for backup_file in ['hotels.json', 'customers.json',
                            'reservations.json']:
            if os.path.exists(backup_file):
                shutil.copy(backup_file, f"{backup_file}_{timestamp}.bak")

        # Ensure a clean test environment before each test
        write_file('hotels.json', [])
        write_file('customers.json', [])
        write_file('reservations.json', [])

    def test_hotel_creation_and_deletion(self):
        """Tests the creation and deletion of hotels."""
        hotel = Hotel("Grand Hotel", "NYC")
        hotel.save()

        hotels = Hotel.list_hotels()
        self.assertEqual(len(hotels), 1)

        Hotel.delete("Grand Hotel")
        hotels = Hotel.list_hotels()
        self.assertEqual(len(hotels), 0)

    def test_customer_creation_and_deletion(self):
        """Tests the creation and deletion of customers."""
        customer = Customer("John Doe", "john@example.com")
        customer.save()

        customers = Customer.list_customers()
        self.assertEqual(len(customers), 1)

        Customer.delete("John Doe")
        customers = Customer.list_customers()
        self.assertEqual(len(customers), 0)

    def test_reservation_persistence(self):
        """Tests that reservations persist
        across different test runs."""
        reservation = Reservation("John Doe", "Grand Hotel")
        reservation.save()

        reservations = Reservation.list_reservations()
        self.assertEqual(len(reservations), 1)

    def test_reservation_cancellation(self):
        """Tests that reservation cancellation
        removes only the specified entry."""
        Reservation("John Doe", "Grand Hotel").save()
        Reservation("Jane Smith", "Beach Resort").save()

        Reservation.cancel("John Doe")
        reservations = Reservation.list_reservations()

        self.assertEqual(len(reservations), 1)
        self.assertEqual(reservations[0]['customer'], "Jane Smith")

    def test_multiple_reservations_creation(self):
        """Tests creating multiple reservations
        and verifies correct storage."""
        Reservation("Alice Brown", "Sunset Hotel").save()
        Reservation("Bob White", "Ocean View Resort").save()

        reservations = Reservation.list_reservations()
        self.assertEqual(len(reservations), 2)


if __name__ == "__main__":
    unittest.main()
