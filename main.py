from pydantic import BaseModel
from typing import Dict, List
from src.models import Parameters
from src.manager import Manager
import json

if __name__ == '__main__':
    parameters = Parameters()
    manager = Manager(parameters)

    for apartment in manager.apartments.values():
        print(f"Kod mieszkania: {apartment.key}, Nazwa mieszkania: {apartment.name}, Lokalizacja mieszkania: {apartment.location}, Powierzchnia mieszkania: {apartment.area_m2}\n")
        for room in apartment.rooms.values():
            print(f"Nazwa pokoju: {room.name}, Powierzchnia pokoju: {room.area_m2}\n")
        
        for bill in manager.bills:
            if bill.apartment == apartment.key:
                print(f"Kwota rachunku: {bill.amount_pln}, Deadline rachunku: {bill.date_due}, Rok rozliczenia: {bill.settlement_year}, Miesiąc rozliczenia: {bill.settlement_month}, Rodzaj rachunku: {bill.type}\n")

    for tenant in manager.tenants.values():
        print(f"Nazwa najemncy: {tenant.name}, Mieszkanie najemncy: {tenant.apartment}, Pokoj najemncy: {tenant.room}, Kwota czynszy[PLN]: {tenant.rent_pln}, Kwota zaliczki[PLN]: {tenant.deposit_pln}, Poczatek umowy: {tenant.date_agreement_from}, Koniec umowy: {tenant.date_agreement_to}\n")
        for transfer in manager.transfers:
            if transfer.tenant == tenant.name:
                print(f"Kwota przelewu[PLN]:  {transfer.amount_pln}, Data przelewu: {transfer.date}, Rok przelewu: {transfer.settlement_year}, Miesiac przelewu: {transfer.settlement_month}")