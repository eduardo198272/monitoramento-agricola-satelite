import pandas as pd


def test_http_response_fixture_is_configurable_and_local(mock_http_response):
    response = mock_http_response({'ok': True}, status_code=201)

    assert response.status_code == 201
    assert response.json() == {'ok': True}
    response.raise_for_status()
    response.raise_for_status.assert_called_once_with()


def test_ee_geometry_fixture_exposes_analysis_values(mock_ee_geometry):
    geometry = mock_ee_geometry(coordinates=(-52.4, -28.3), area_m2=2500000)

    assert geometry.centroid().coordinates().getInfo() == [-52.4, -28.3]
    assert geometry.area().divide().getInfo() == 250.0


def test_ee_collection_fixture_is_configurable(mock_ee_collection):
    collection = mock_ee_collection(size=5)

    assert collection.size().getInfo() == 5
    assert collection.map() is collection
    assert collection.median() is not None


def test_time_series_fixture_has_stable_order_and_values(sample_time_series):
    assert [item['date'] for item in sample_time_series] == [
        '2026-01-01', '2026-02-01', '2026-03-01'
    ]
    assert [item['value'] for item in sample_time_series] == [0.5, 0.6, 0.7]


def test_dataframe_fixture_has_expected_schema(sample_dataframe):
    assert isinstance(sample_dataframe, pd.DataFrame)
    assert list(sample_dataframe.columns) == [
        'date', 'precipitation', 'temperature'
    ]
    assert len(sample_dataframe) == 3


def test_shared_fixtures_return_independent_objects(mock_http_response):
    first = mock_http_response({'id': 1})
    second = mock_http_response({'id': 2})

    first.json.return_value['id'] = 99

    assert second.json() == {'id': 2}
