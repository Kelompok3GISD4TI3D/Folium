import folium

m = folium.Map(
    location=[-5.148298,  119.435022],
    zoom_start=10,
    )
folium.Marker(
    location=[-5.147432,  119.417544],
    popup='Mangkura',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-5.138860,  119.417977],
    popup='Lajangiru',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-5.124052,  119.411914],
    popup='Butung',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-5.114419,  119.417688],
    popup='Totaka',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-5.109530,  119.430102],
    popup='Kaluku Bodoa',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-5.1011766,  119.446269],
    popup='Tallo',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-5.103348,  119.453343],
    popup='Parang Loe',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-5.127628,  119.460599],
    popup='Mamajang',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-5.113708, 119.413535],
    popup='Tamalaba',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
folium.Marker(
    location=[-5.136272, 119.417255],
    popup='pisang utara',
    icon=folium.Icon(icon='info-sign')
).add_to(m)
m.save('index.html')
.
