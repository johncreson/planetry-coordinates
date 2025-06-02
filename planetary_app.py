import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timezone
import requests
import json
from typing import Dict, List, Tuple
import time

# Configure page
st.set_page_config(
    page_title="Planetary Positioning Coordinates",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/johncreson/planetary-coordinates',
        'Report a bug': 'https://github.com/johncreson/planetary-coordinates/issues',
        'About': "Planetary positioning coordinates in multiple coordinate systems"
    }
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 48px;
        text-align: center;
        color: #1f4e79;
        margin-bottom: 32px;
    }
    .coord-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 16px;
        border-radius: 10px;
        margin: 16px 0;
        color: white;
    }
    .planet-header {
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 8px;
    }
    .coord-value {
        font-family: 'Courier New', monospace;
        font-size: 18px;
        background: rgba(255,255,255,0.1);
        padding: 5px;
        border-radius: 5px;
        margin: 3px 0;
    }
    .timestamp {
        text-align: center;
        font-style: italic;
        color: #666;
        margin: 16px 0;
    }
</style>
""", unsafe_allow_html=True)

class PlanetaryCoordinates:
    """Calculate planetary coordinates using astronomical algorithms"""
    
    def __init__(self):
        self.planets = {
            'Mercury': 1, 'Venus': 2, 'Earth': 3, 'Mars': 4,
            'Jupiter': 5, 'Saturn': 6, 'Uranus': 7, 'Neptune': 8
        }
        
    def get_jpl_horizons_data(self, planet_id: int, start_time: str) -> Dict:
        """Get data from JPL HORIZONS API"""
        try:
            base_url = "https://ssd.jpl.nasa.gov/api/horizons.api"
            params = {
                'format': 'json',
                'COMMAND': str(planet_id),
                'OBJ_DATA': 'YES',
                'MAKE_EPHEM': 'YES',
                'EPHEM_TYPE': 'OBSERVER',
                'CENTER': '500@399',  # Earth center
                'START_TIME': start_time,
                'STOP_TIME': start_time,
                'STEP_SIZE': '1d',
                'QUANTITIES': '1,2,3,4,9,20,23,24'  # RA, DEC, distance, etc.
            }
            
            response = requests.get(base_url, params=params, timeout=10)
            if response.status_code == 200:
                return response.json()
            else:
                return None
        except Exception as e:
            st.error(f"Error fetching JPL data: {e}")
            return None
    
    def calculate_approximate_positions(self, jd: float) -> Dict:
        """Calculate approximate planetary positions using simplified algorithms"""
        # Simplified orbital elements for demonstration
        # In practice, you'd use more precise ephemeris data
        
        positions = {}
        
        # Sample approximate calculations (these are simplified)
        planets_data = {
            'Mercury': {
                # Geocentric coordinates (Earth-centered)
                'ra': 15.5 + 0.1 * (jd - 2459000), 
                'dec': -23.2 + 0.05 * (jd - 2459000),
                'distance': 0.72 + 0.1 * np.sin((jd - 2459000) * 0.01),
                # Heliocentric coordinates (Sun-centered)
                'helio_lon': 45.2 + 4.09 * (jd - 2459000) / 365.25,  # Fast orbital motion
                'helio_lat': 2.1 * np.sin((jd - 2459000) * 0.02),
                'helio_dist': 0.387 + 0.08 * np.sin((jd - 2459000) * 0.012)
            },
            'Venus': {
                'ra': 22.8 + 0.08 * (jd - 2459000),
                'dec': -15.6 + 0.03 * (jd - 2459000),
                'distance': 1.02 + 0.05 * np.sin((jd - 2459000) * 0.008),
                'helio_lon': 178.3 + 1.6 * (jd - 2459000) / 365.25,
                'helio_lat': 1.8 * np.sin((jd - 2459000) * 0.015),
                'helio_dist': 0.723 + 0.007 * np.sin((jd - 2459000) * 0.009)
            },
            'Mars': {
                'ra': 8.2 + 0.05 * (jd - 2459000),
                'dec': 18.5 + 0.02 * (jd - 2459000),
                'distance': 1.85 + 0.3 * np.sin((jd - 2459000) * 0.005),
                'helio_lon': 289.7 + 0.524 * (jd - 2459000) / 365.25,
                'helio_lat': 1.2 * np.sin((jd - 2459000) * 0.008),
                'helio_dist': 1.524 + 0.14 * np.sin((jd - 2459000) * 0.006)
            },
            'Jupiter': {
                'ra': 5.8 + 0.02 * (jd - 2459000),
                'dec': 23.1 + 0.01 * (jd - 2459000),
                'distance': 5.95 + 0.1 * np.sin((jd - 2459000) * 0.002),
                'helio_lon': 67.8 + 0.083 * (jd - 2459000) / 365.25,
                'helio_lat': 0.8 * np.sin((jd - 2459000) * 0.003),
                'helio_dist': 5.203 + 0.25 * np.sin((jd - 2459000) * 0.004)
            },
            'Saturn': {
                'ra': 14.2 + 0.015 * (jd - 2459000),
                'dec': -8.5 + 0.008 * (jd - 2459000),
                'distance': 9.8 + 0.2 * np.sin((jd - 2459000) * 0.001),
                'helio_lon': 156.4 + 0.034 * (jd - 2459000) / 365.25,
                'helio_lat': 0.6 * np.sin((jd - 2459000) * 0.002),
                'helio_dist': 9.537 + 0.54 * np.sin((jd - 2459000) * 0.003)
            },
            'Uranus': {
                'ra': 3.1 + 0.01 * (jd - 2459000),
                'dec': 17.8 + 0.005 * (jd - 2459000),
                'distance': 19.2 + 0.1 * np.sin((jd - 2459000) * 0.0008),
                'helio_lon': 45.9 + 0.012 * (jd - 2459000) / 365.25,
                'helio_lat': 0.4 * np.sin((jd - 2459000) * 0.001),
                'helio_dist': 19.19 + 1.35 * np.sin((jd - 2459000) * 0.002)
            },
            'Neptune': {
                'ra': 23.9 + 0.008 * (jd - 2459000),
                'dec': -2.1 + 0.003 * (jd - 2459000),
                'distance': 30.1 + 0.05 * np.sin((jd - 2459000) * 0.0006),
                'helio_lon': 324.1 + 0.006 * (jd - 2459000) / 365.25,
                'helio_lat': 0.3 * np.sin((jd - 2459000) * 0.0008),
                'helio_dist': 30.07 + 0.82 * np.sin((jd - 2459000) * 0.001)
            }
        }
        
        for planet, data in planets_data.items():
            # Geocentric coordinates (Earth-centered)
            ra = data['ra'] % 24
            dec = max(-90, min(90, data['dec']))
            
            # Heliocentric coordinates (Sun-centered)
            helio_lon = data['helio_lon'] % 360
            helio_lat = max(-90, min(90, data['helio_lat']))
            helio_dist = abs(data['helio_dist'])
            
            positions[planet] = {
                # Geocentric (Earth-centered) coordinates
                'ra_hours': ra,
                'ra_degrees': ra * 15.0,
                'dec_degrees': dec,
                'distance_au': abs(data['distance']),
                'magnitude': self.calculate_magnitude(planet, data['distance']),
                
                # Heliocentric (Sun-centered) coordinates
                'helio_longitude': helio_lon,
                'helio_latitude': helio_lat,
                'helio_distance': helio_dist,
                
                # Cartesian heliocentric coordinates
                'helio_x': helio_dist * np.cos(np.radians(helio_lat)) * np.cos(np.radians(helio_lon)),
                'helio_y': helio_dist * np.cos(np.radians(helio_lat)) * np.sin(np.radians(helio_lon)),
                'helio_z': helio_dist * np.sin(np.radians(helio_lat))
            }
            
        return positions
    
    def calculate_magnitude(self, planet: str, distance: float) -> float:
        """Calculate approximate visual magnitude"""
        base_mags = {
            'Mercury': -0.4, 'Venus': -4.4, 'Mars': -2.9, 'Jupiter': -2.9,
            'Saturn': 0.4, 'Uranus': 5.7, 'Neptune': 7.8
        }
        base = base_mags.get(planet, 0)
        # Simple distance-based magnitude adjustment
        return base + 5 * np.log10(distance / 1.0)
    
    def julian_date(self, dt: datetime) -> float:
        """Convert datetime to Julian Date"""
        a = (14 - dt.month) // 12
        y = dt.year + 4800 - a
        m = dt.month + 12 * a - 3
        return dt.day + (153 * m + 2) // 5 + 365 * y + y // 4 - y // 100 + y // 400 - 32045 + (dt.hour + dt.minute/60 + dt.second/3600) / 24

def format_ra_hms(ra_hours: float) -> str:
    """Format RA in hours, minutes, seconds"""
    h = int(ra_hours)
    m = int((ra_hours - h) * 60)
    s = ((ra_hours - h) * 60 - m) * 60
    return f"{h:02d}h {m:02d}m {s:05.2f}s"

def format_dec_dms(dec_degrees: float) -> str:
    """Format declination in degrees, minutes, seconds"""
    sign = "+" if dec_degrees >= 0 else "-"
    dec_abs = abs(dec_degrees)
    d = int(dec_abs)
    m = int((dec_abs - d) * 60)
    s = ((dec_abs - d) * 60 - m) * 60
    return f"{sign}{d:02d}° {m:02d}' {s:05.2f}\""

def main():
    # Header
    st.markdown('<h1 class="main-header">🪐 Planetary Positioning Coordinates</h1>', unsafe_allow_html=True)
    
    # Sidebar controls
    st.sidebar.header("⚙️ Settings")
    
    # Time selection
    use_current_time = st.sidebar.checkbox("Use Current Time", value=True)
    
    if use_current_time:
        current_time = datetime.now(timezone.utc)
        selected_time = current_time
    else:
        date_col, time_col = st.sidebar.columns(2)
        with date_col:
            selected_date = st.date_input("Date", value=datetime.now().date())
        with time_col:
            selected_time_input = st.time_input("Time (UTC)", value=datetime.now().time())
        selected_time = datetime.combine(selected_date, selected_time_input).replace(tzinfo=timezone.utc)
    
    # Coordinate system selection
    coord_systems = st.sidebar.multiselect(
        "Coordinate Systems",
        ["Geocentric (RA/Dec)", "Heliocentric (Lon/Lat)", "Cartesian Heliocentric", "Distance & Magnitude"],
        default=["Geocentric (RA/Dec)", "Heliocentric (Lon/Lat)"]
    )
    
    # Planet selection
    all_planets = ['Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    selected_planets = st.sidebar.multiselect(
        "Select Planets",
        all_planets,
        default=all_planets
    )
    
    # Auto-refresh option
    auto_refresh = st.sidebar.checkbox("Auto-refresh (30s)", value=False)
    if auto_refresh:
        time.sleep(1)
        st.rerun()
    
    # Display current time
    st.markdown(f'<div class="timestamp">📅 Calculated for: {selected_time.strftime("%Y-%m-%d %H:%M:%S UTC")}</div>', unsafe_allow_html=True)
    
    # Initialize calculator
    calc = PlanetaryCoordinates()
    
    # Calculate positions
    with st.spinner("Calculating planetary positions..."):
        jd = calc.julian_date(selected_time)
        positions = calc.calculate_approximate_positions(jd)
    
    # Display results
    if selected_planets:
        # Create tabs for different views
        tab1, tab2, tab3 = st.tabs(["🔢 Coordinate Table", "🎯 Individual Planets", "📊 Data Summary"])
        
        with tab1:
            # Create comprehensive table
            table_data = []
            for planet in selected_planets:
                if planet in positions:
                    pos = positions[planet]
                    row_data = {
                        'Planet': f"🪐 {planet}",
                    }
                    
                    # Add geocentric coordinates if selected
                    if "Geocentric (RA/Dec)" in coord_systems:
                        row_data.update({
                            'RA (hours)': f"{pos['ra_hours']:.6f}",
                            'RA (h m s)': format_ra_hms(pos['ra_hours']),
                            'Dec (degrees)': f"{pos['dec_degrees']:.6f}°",
                            'Dec (° \' \")': format_dec_dms(pos['dec_degrees']),
                            'Geo Distance (AU)': f"{pos['distance_au']:.6f}",
                        })
                    
                    # Add heliocentric coordinates if selected
                    if "Heliocentric (Lon/Lat)" in coord_systems:
                        row_data.update({
                            'Helio Longitude': f"{pos['helio_longitude']:.6f}°",
                            'Helio Latitude': f"{pos['helio_latitude']:.6f}°",
                            'Helio Distance (AU)': f"{pos['helio_distance']:.6f}",
                        })
                    
                    # Add Cartesian heliocentric if selected
                    if "Cartesian Heliocentric" in coord_systems:
                        row_data.update({
                            'Helio X (AU)': f"{pos['helio_x']:.6f}",
                            'Helio Y (AU)': f"{pos['helio_y']:.6f}",
                            'Helio Z (AU)': f"{pos['helio_z']:.6f}",
                        })
                    
                    # Add magnitude if selected
                    if "Distance & Magnitude" in coord_systems:
                        row_data.update({
                            'Magnitude': f"{pos['magnitude']:.2f}"
                        })
                    
                    table_data.append(row_data)
            
            if table_data:
                df = pd.DataFrame(table_data)
                st.dataframe(df, use_container_width=True, hide_index=True)
        
        with tab2:
            # Display individual planet cards
            cols = st.columns(2)
            for i, planet in enumerate(selected_planets):
                if planet in positions:
                    pos = positions[planet]
                    
                    with cols[i % 2]:
                        geocentric_content = ""
                        heliocentric_content = ""
                        cartesian_content = ""
                        distance_content = ""
                        
                        if "Geocentric (RA/Dec)" in coord_systems:
                            geocentric_content = f"""
                            <div class='coord-value'><strong>Geocentric Coordinates (Earth-centered):</strong><br>
                            RA: {format_ra_hms(pos['ra_hours'])}<br>
                            Dec: {format_dec_dms(pos['dec_degrees'])}<br>
                            Distance: {pos['distance_au']:.6f} AU</div>
                            """
                        
                        if "Heliocentric (Lon/Lat)" in coord_systems:
                            heliocentric_content = f"""
                            <div class='coord-value'><strong>Heliocentric Coordinates (Sun-centered):</strong><br>
                            Longitude: {pos['helio_longitude']:.6f}°<br>
                            Latitude: {pos['helio_latitude']:.6f}°<br>
                            Distance: {pos['helio_distance']:.6f} AU</div>
                            """
                        
                        if "Cartesian Heliocentric" in coord_systems:
                            cartesian_content = f"""
                            <div class='coord-value'><strong>Cartesian Heliocentric (X,Y,Z):</strong><br>
                            X: {pos['helio_x']:.6f} AU<br>
                            Y: {pos['helio_y']:.6f} AU<br>
                            Z: {pos['helio_z']:.6f} AU</div>
                            """
                        
                        if "Distance & Magnitude" in coord_systems:
                            distance_content = f"""
                            <div class='coord-value'><strong>Observational Data:</strong><br>
                            Apparent Magnitude: {pos['magnitude']:.2f}<br>
                            Geocentric Distance: {pos['distance_au']:.6f} AU<br>
                            Heliocentric Distance: {pos['helio_distance']:.6f} AU</div>
                            """
                        
                        st.markdown(f"""
                        <div class="coord-container">
                            <div class="planet-header">🪐 {planet}</div>
                            {geocentric_content}
                            {heliocentric_content}
                            {cartesian_content}
                            {distance_content}
                        </div>
                        """, unsafe_allow_html=True)
        
        with tab3:
            # Summary statistics
            st.subheader("📊 Coordinate Summary")
            
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("Planets Calculated", len(selected_planets))
            
            with col2:
                avg_geo_distance = np.mean([positions[p]['distance_au'] for p in selected_planets if p in positions])
                st.metric("Avg Geo Distance (AU)", f"{avg_geo_distance:.3f}")
            
            with col3:
                avg_helio_distance = np.mean([positions[p]['helio_distance'] for p in selected_planets if p in positions])
                st.metric("Avg Helio Distance (AU)", f"{avg_helio_distance:.3f}")
            
            with col4:
                brightest = min([positions[p]['magnitude'] for p in selected_planets if p in positions])
                st.metric("Brightest Magnitude", f"{brightest:.2f}")
            
            # Additional metrics row
            col5, col6, col7, col8 = st.columns(4)
            
            with col5:
                st.metric("Julian Date", f"{jd:.3f}")
            
            with col6:
                helio_lon_range = max([positions[p]['helio_longitude'] for p in selected_planets if p in positions]) - \
                                 min([positions[p]['helio_longitude'] for p in selected_planets if p in positions])
                st.metric("Helio Lon Range", f"{helio_lon_range:.1f}°")
            
            with col7:
                max_helio_lat = max([abs(positions[p]['helio_latitude']) for p in selected_planets if p in positions])
                st.metric("Max Helio Latitude", f"±{max_helio_lat:.2f}°")
            
            with col8:
                farthest_from_sun = max([positions[p]['helio_distance'] for p in selected_planets if p in positions])
                st.metric("Farthest from Sun", f"{farthest_from_sun:.1f} AU")
            
            # Coordinate comparison tables
            st.subheader("🌍 Geocentric vs 🌞 Heliocentric Comparison")
            
            col_left, col_right = st.columns(2)
            
            with col_left:
                st.markdown("**Geocentric Coordinates (Earth-centered)**")
                geo_data = []
                for planet in selected_planets:
                    if planet in positions:
                        pos = positions[planet]
                        geo_data.append({
                            'Planet': planet,
                            'RA': f"{pos['ra_degrees']:.2f}°",
                            'Dec': f"{pos['dec_degrees']:.2f}°",
                            'Distance': f"{pos['distance_au']:.3f} AU"
                        })
                
                if geo_data:
                    st.dataframe(pd.DataFrame(geo_data), use_container_width=True, hide_index=True)
            
            with col_right:
                st.markdown("**Heliocentric Coordinates (Sun-centered)**")
                helio_data = []
                for planet in selected_planets:
                    if planet in positions:
                        pos = positions[planet]
                        helio_data.append({
                            'Planet': planet,
                            'Longitude': f"{pos['helio_longitude']:.2f}°",
                            'Latitude': f"{pos['helio_latitude']:.2f}°",
                            'Distance': f"{pos['helio_distance']:.3f} AU"
                        })
                
                if helio_data:
                    st.dataframe(pd.DataFrame(helio_data), use_container_width=True, hide_index=True)
            
            # 3D position visualization data
            st.subheader("🎯 3D Heliocentric Positions")
            cartesian_data = []
            for planet in selected_planets:
                if planet in positions:
                    pos = positions[planet]
                    cartesian_data.append({
                        'Planet': planet,
                        'X (AU)': f"{pos['helio_x']:.4f}",
                        'Y (AU)': f"{pos['helio_y']:.4f}",
                        'Z (AU)': f"{pos['helio_z']:.4f}",
                        'Distance from Sun': f"{pos['helio_distance']:.4f} AU"
                    })
            
            if cartesian_data:
                st.dataframe(pd.DataFrame(cartesian_data), use_container_width=True, hide_index=True)
    
    else:
        st.warning("Please select at least one planet to display coordinates.")
    
    # Footer information
    st.markdown("---")
    st.markdown("""
    **📝 Notes:**
    - Coordinates are calculated using simplified astronomical algorithms for demonstration
    - For high-precision applications, use JPL HORIZONS or similar professional ephemeris services
    - All times are in UTC
    - Distances are in Astronomical Units (AU)
    - Magnitudes are apparent visual magnitudes
    
    **📚 Coordinate Systems:**
    
    **🌍 Geocentric Coordinates (Earth-centered):**
    - **Right Ascension (RA)**: Celestial longitude (0-24 hours or 0-360°)
    - **Declination (Dec)**: Celestial latitude (-90° to +90°)
    - **Distance**: Distance from Earth in Astronomical Units
    
    **🌞 Heliocentric Coordinates (Sun-centered):**
    - **Heliocentric Longitude**: Angular position in orbital plane (0-360°)
    - **Heliocentric Latitude**: Angular distance from ecliptic plane (-90° to +90°)
    - **Heliocentric Distance**: Distance from Sun in Astronomical Units
    
    **📐 Cartesian Heliocentric:**
    - **X, Y, Z**: 3D coordinates relative to Sun center in AU
    - **Ecliptic plane**: Z=0 plane, X-axis toward vernal equinox
    - **Useful for**: Orbital mechanics, spacecraft navigation, 3D visualization
    
    **✨ Key Differences:**
    - **Geocentric**: How planets appear from Earth (observational astronomy)
    - **Heliocentric**: True positions in solar system (orbital mechanics)
    - **Cartesian**: 3D mathematical representation for calculations
    """)

def format_helio_lon(lon_degrees: float) -> str:
    """Format heliocentric longitude in degrees"""
    return f"{lon_degrees:.6f}°"

def format_helio_lat(lat_degrees: float) -> str:
    """Format heliocentric latitude in degrees"""
    sign = "+" if lat_degrees >= 0 else "-"
    return f"{sign}{abs(lat_degrees):.6f}°"

if __name__ == "__main__":
    main()
