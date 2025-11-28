from components.sorting import Sorting

def test_sorting(cars_page):
    sort = Sorting(cars_page)

    print("\n--- Apply Sorting: Price Low to High ---")
    sort.apply("Price: Low to High")
    prices = sort.get_price_sort_by()
    assert prices == sorted(prices), "❌ Prices are not sorted Low to High after applying filters!"
    print("sorted by low to high after applying filters:", prices)

    print("\n--- Apply Sorting: Price High to Low ---")
    sort.apply("Price: High to Low")
    prices = sort.get_price_sort_by()
    assert prices == sorted(prices, reverse=True), "❌ Prices are not sorted High to Low after applying filters!"

    print("sorted by high to low after applying filters:", prices)

    print("\n--- Apply Sorting: Kilometer Low to High ---")
    sort.apply("Kilometers: Low to High")
    sorted_kms = sort.get_km_sort_by()
    assert sorted_kms == sorted(sorted_kms), "❌ Kilometers are not sorted Low to High!"
    print("sorted by low to high kms after applying filters:", sorted_kms)

    print("\n--- Apply Sorting: Kilometer High to Low ---")
    sort.apply("Kilometers: High to Low")
    sorted_kms = sort.get_km_sort_by()
    assert sorted_kms == sorted(sorted_kms, reverse=True), "❌ Kilometers are not sorted High to Low after applying filters!"
    print("sorted by high to low kms after applying filters:", sorted_kms)

    print("\n--- Apply Sorting: Year Low to High ---")
    sort.apply("Year: Low to High")
    sorted_years = sort.get_year_sort_by()
    assert sorted_years == sorted(sorted_years), "❌ Years are not sorted by Low to High!"
    print("sorted by low to high Years:", sorted_years)

    print("\n--- Apply Sorting: Years High to low ---")
    sort.apply("Year: High to Low")
    sorted_years = sort.get_year_sort_by()
    assert sorted_years == sorted(sorted_years, reverse=True), "❌ Years are not sorted by High to Low!"
    print("sorted by high to low Years:", sorted_years)

    print("\n🎉 Sorting flow completed successfully!")

