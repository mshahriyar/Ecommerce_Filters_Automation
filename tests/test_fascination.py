from components.fascination import FascinationCarousel



def test_fascination_flow(cars_page):
    fascination = FascinationCarousel(cars_page)

    make_labels = fascination.validate_visible()
    assert len(make_labels) > 0, "❌ No Make list shown"
    selected_make = fascination.click_first()
    cars_page.wait_for_timeout(3000)

    model_labels = fascination.validate_visible()
    assert len(model_labels) > 0, "❌ No model list shown after selecting a Make!"
    fascination.click_first()
    cars_page.wait_for_timeout(3000)
    

    year_labels = fascination.validate_visible()
    assert len(year_labels) > 0, "❌ No year list shown after selecting a Model!"
    fascination.click_first()
