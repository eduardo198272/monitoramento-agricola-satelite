from streamlit.testing.v1 import AppTest


def test_app_renders_initial_form():
    app = AppTest.from_file("src/app/main.py").run()

    assert not app.exception
    assert app.title[0].value == "Sistema de Monitoramento Agricola"
    assert app.text_input[0].label == "Nome da área de análise"
    assert app.text_input[1].label == "Período da análise"


def test_app_shows_entered_area_and_period():
    app = AppTest.from_file("src/app/main.py").run()
    app.text_input[0].input("Talhão Norte")
    app.text_input[1].input("2026-01-01 a 2026-01-31")
    app.run()

    written_values = [element.value for element in app.markdown]
    assert "Área: Talhão Norte" in written_values
    assert "Período: 2026-01-01 a 2026-01-31" in written_values
