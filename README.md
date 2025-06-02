# 🌌 Planetary Positioning Coordinates

A comprehensive web application that displays real-time planetary coordinates in multiple coordinate systems, providing both geocentric (Earth-centered) and heliocentric (Sun-centered) perspectives.

![Planetary Coordinates App](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## 🚀 Live Demo

**🌐 [View Live Application](https://johncreson-planetary-coordinates-planetary-app-main.streamlit.app/)**

## ✨ Features

### 📍 Multiple Coordinate Systems
- **🌍 Geocentric Coordinates**: Earth-centered view (RA/Dec) for astronomical observations
- **🌞 Heliocentric Coordinates**: Sun-centered view (Longitude/Latitude) for orbital mechanics
- **📐 Cartesian Coordinates**: 3D mathematical representation (X/Y/Z) for space navigation

### 🪐 Comprehensive Planetary Data
- All major planets: Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune
- Real-time coordinate calculations
- Distance measurements from both Earth and Sun
- Visual magnitude calculations
- Professional astronomical formatting

### 🎛️ Interactive Features
- **Planet Selection**: Choose which planets to display
- **Time Controls**: Current time or custom date/time selection
- **Auto-Refresh**: Real-time updates every 30 seconds
- **Multiple Views**: Data table, individual planet cards, summary statistics
- **Coordinate Comparison**: Side-by-side geocentric vs heliocentric analysis

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **Data Processing**: Pandas, NumPy
- **Astronomical Calculations**: Custom algorithms based on orbital mechanics
- **Styling**: CSS with gradient themes and professional formatting

## 📊 Sample Output

```
🌍 GEOCENTRIC COORDINATES (Earth-centered)
Planet    | RA (°)     | Dec (°)    | Distance (AU)
Mercury   |     76.23  |    -22.15  |        0.724
Jupiter   |     87.12  |     23.45  |        5.967

🌞 HELIOCENTRIC COORDINATES (Sun-centered)  
Planet    | Longitude  | Latitude   | Distance (AU)
Mercury   |    125.40  |      2.10  |        0.387
Jupiter   |     89.10  |      0.80  |        5.203
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/johncreson/planetary-coordinates.git
   cd planetary-coordinates
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run planetary_app.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:8501`

## 📖 Usage Guide

### 🎯 Getting Started
1. **Select Planets**: Use the sidebar to choose which planets to display
2. **Choose Coordinate Systems**: Select from Geocentric, Heliocentric, or Cartesian coordinates
3. **Set Time**: Use current time or pick a custom date/time
4. **Explore Views**: Switch between table view, planet cards, and summary statistics

### 🔍 Understanding Coordinate Systems

#### 🌍 Geocentric (Earth-centered)
- **Right Ascension (RA)**: Celestial longitude (0-360° or 0-24h)
- **Declination (Dec)**: Celestial latitude (-90° to +90°)
- **Use Case**: Telescope pointing, astronomical observations

#### 🌞 Heliocentric (Sun-centered)
- **Longitude**: Angular position in orbital plane (0-360°)
- **Latitude**: Angular distance from ecliptic plane (±90°)
- **Use Case**: Orbital mechanics, space mission planning

#### 📐 Cartesian
- **X, Y, Z**: 3D coordinates relative to Sun center
- **Reference Frame**: Ecliptic plane, vernal equinox
- **Use Case**: Spacecraft navigation, mathematical calculations

## 🎨 Features Overview

### 📱 User Interface
- **Responsive Design**: Works on desktop and mobile
- **Professional Styling**: Gradient themes and astronomical color schemes
- **Intuitive Controls**: Easy-to-use sidebar and tabbed interface

### 📊 Data Visualization
- **Comprehensive Tables**: Sortable, copy-friendly coordinate data
- **Individual Planet Cards**: Detailed coordinate breakdown per planet
- **Summary Statistics**: Comparative analysis and key metrics

### ⚙️ Advanced Options
- **Auto-Refresh**: Real-time coordinate updates
- **Custom Time Selection**: Historical or future coordinate calculations
- **Multiple Export Formats**: Copy data for external use

## 🔬 Accuracy & Limitations

- **Calculation Method**: Simplified astronomical algorithms for demonstration
- **Accuracy**: Suitable for educational and general reference purposes
- **For High Precision**: Professional applications should use JPL HORIZONS or similar services
- **Time Range**: Optimized for dates around 2020-2030

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Commit your changes** (`git commit -m 'Add some AmazingFeature'`)
4. **Push to the branch** (`git push origin feature/AmazingFeature`)
5. **Open a Pull Request**

### 💡 Ideas for Contributions
- Integration with JPL HORIZONS API for higher precision
- Additional celestial objects (asteroids, comets)
- 3D visualization of planetary positions
- Historical coordinate plotting
- Export to astronomical software formats

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Astronomical Algorithms**: Based on standard orbital mechanics principles
- **Streamlit Community**: For the excellent web framework
- **NASA JPL**: For astronomical reference standards and ephemeris data concepts

## 📞 Contact

**John Creson** - [@johncreson](https://github.com/johncreson)

Project Link: [https://github.com/johncreson/planetary-coordinates](https://github.com/johncreson/planetary-coordinates)

---

⭐ If you found this project helpful, please give it a star on GitHub!

## 🔮 Future Enhancements

- [ ] Real JPL HORIZONS API integration
- [ ] 3D solar system visualization
- [ ] Asteroid and comet tracking
- [ ] Historical coordinate animations
- [ ] Mobile app version
- [ ] API endpoints for programmatic access