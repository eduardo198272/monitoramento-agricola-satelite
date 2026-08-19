import ee
import plotly.graph_objects as go


def compute_time_series(
    collection: ee.ImageCollection,
    geometry: ee.Geometry,
    index_name: str,
    scale: int = 10
) -> list[dict]:
    if collection.size().getInfo() == 0:
        return []

    def reduce_image(img):
        img = ee.Image(img)
        stats = img.reduceRegion(
            reducer=ee.Reducer.mean(),
            geometry=geometry,
            scale=scale,
            maxPixels=1e9
        )
        value = stats.get(index_name)
        date_str = img.date().format("YYYY-MM-dd")
        return ee.Feature(None, {"date": date_str, "value": value})

    features = collection.map(reduce_image)
    features_list = features.toList(features.size())

    result = []
    size = features_list.size().getInfo()

    for i in range(size):
        feat = ee.Feature(features_list.get(i))
        props = feat.toDictionary().getInfo()
        val = props.get("value")
        if val is not None:
            result.append({
                "date": props["date"],
                "value": float(val)
            })

    result.sort(key=lambda x: x["date"])
    return result


def plot_time_series(data: list[dict], index_name: str) -> go.Figure | None:
    if not data:
        return None

    dates = [d["date"] for d in data]
    values = [d["value"] for d in data]

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=dates,
        y=values,
        mode="lines+markers",
        name=index_name,
        line=dict(color="#2E86AB", width=2),
        marker=dict(size=6)
    ))

    fig.update_layout(
        title=f"Evolução Temporal de {index_name}",
        xaxis_title="Data",
        yaxis_title=index_name,
        yaxis=dict(range=[-1, 1]),
        template="plotly_white",
        showlegend=False,
        hovermode="x unified"
    )

    return fig