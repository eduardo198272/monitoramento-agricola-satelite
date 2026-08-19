import ee
from datetime import datetime


def filter_by_date(collection: ee.ImageCollection, start_date: str, end_date: str) -> ee.ImageCollection:
    _validate_date_format(start_date)
    _validate_date_format(end_date)
    if start_date > end_date:
        raise ValueError("start_date deve ser menor ou igual a end_date")
    return collection.filter(ee.Filter.date(start_date, end_date))


def filter_by_area(collection: ee.ImageCollection, geometry: ee.Geometry) -> ee.ImageCollection:
    if geometry is None:
        raise ValueError("geometry não pode ser None")
    return collection.filter(ee.Filter.bounds(geometry))


def get_image_collection(
    geometry: ee.Geometry,
    start_date: str,
    end_date: str,
    cloud_cover_max: int = 20
) -> ee.ImageCollection:
    if geometry is None:
        raise ValueError("geometry não pode ser None")
    if not isinstance(cloud_cover_max, int) or cloud_cover_max < 0 or cloud_cover_max > 100:
        raise ValueError("cloud_cover_max deve ser inteiro entre 0 e 100")

    collection = ee.ImageCollection("COPERNICUS/S2_SR_HARMONIZED")
    collection = filter_by_area(collection, geometry)
    collection = filter_by_date(collection, start_date, end_date)
    collection = collection.filter(ee.Filter.lt("CLOUD_COVERAGE_ASSESSMENT", cloud_cover_max))
    collection = collection.select(["B2", "B3", "B4", "B8", "QA60"])
    return collection


def mask_clouds(image: ee.Image) -> ee.Image:
    qa60 = image.select("QA60")
    cloud_mask = qa60.bitwiseAnd(1 << 10).eq(0)
    cirrus_mask = qa60.bitwiseAnd(1 << 11).eq(0)
    mask = cloud_mask.And(cirrus_mask)
    return image.updateMask(mask)


def _validate_date_format(date_str: str) -> None:
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError(f"Data inválida: {date_str}. Use formato YYYY-MM-DD")


def calculate_ndvi(image: ee.Image) -> ee.Image:
    ndvi = image.normalizedDifference(["B8", "B4"])
    return ndvi.rename("NDVI")


def calculate_ndwi(image: ee.Image) -> ee.Image:
    ndwi = image.normalizedDifference(["B8", "B11"])
    return ndwi.rename("NDWI")


def calculate_ndmi(image: ee.Image) -> ee.Image:
    ndmi = image.normalizedDifference(["B8A", "B11"])
    return ndmi.rename("NDMI")