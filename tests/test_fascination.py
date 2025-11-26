from components.fascination import FascinationCarousel



def test_fascination_flow(cars_page):
    fascination = FascinationCarousel(cars_page)


    print("\n--- Level 1: Validate Makes ---")
    make_labels = fascination.validate_visible()
    assert len(make_labels) > 0, "❌ No Make list shown"
    selected_make = fascination.click_first()

    print("\n--- Level 2: Validate Models ---")
    model_labels = fascination.validate_visible()

    assert len(model_labels) > 0, "❌ No model list shown after selecting a Make!"

    selected_model = fascination.click_first()

    # ---------------------------
    # LEVEL 3 → YEAR SELECTION
    # ---------------------------
    print("\n--- Level 3: Validate Years ---")
    year_labels = fascination.validate_visible()

    assert len(year_labels) > 0, "❌ No year list shown after selecting a Model!"

    selected_year = fascination.click_first()

    print("\n🎉 Fascination flow completed successfully!")
    print(f"Selected Make → {selected_make}")
    print(f"Selected Model → {selected_model}")
    print(f"Selected Year → {selected_year}")
