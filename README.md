# Airbnb Clone Take-Home Task

Welcome to my submission for the Airbnb Clone take-home task. This project is a highly-accurate, pixel-perfect clone of the Airbnb listing page, built with modern web technologies. 

**Live Deployment (Vercel):** [INSERT VERCEL DEPLOYMENT LINK HERE]

## 🌟 Key Features
- **Pixel-Perfect UI:** Meticulous attention to layout, typography, colors, and spatial harmony mirroring the reference.
- **Dynamic Overlays:** 
  - **Amenities Modal:** A fully responsive scrolling overlay containing all 50 amenities.
  - **Photo Tour:** A full-screen masonry gallery categorized by room types with sticky header navigation.
  - **Lightbox:** Interactive single-image viewing with keyboard navigation and cross-fade animations.
- **Performance Optimized:** Clean component structure, purged unused CSS, and extremely lightweight bundled assets.

## 🛠️ Technology Stack
- **Frontend Framework:** React 18
- **Build Tool:** Vite
- **Language:** TypeScript
- **Styling:** Custom CSS (Semantic custom-class methodology)
- **Deployment:** Vercel (Edge Network)

## 🚀 Running the Project Locally

To run this project on your local machine, follow these steps:

1. **Install dependencies:**
   ```bash
   npm install
   ```

2. **Start the development server:**
   ```bash
   npm run dev
   ```

3. **Build for production:**
   ```bash
   npm run build
   ```

## 📐 Architecture Overview
Given the task constraints, I opted for a **Frontend-Focused Strategy**:
- **UI & State:** React manages all modal and lightbox state variables logically. 
- **Global CDN:** Deployed on Vercel to ensure sub-second global response times and edge caching.
- Please refer to `architecture_diagram.md` for a complete visual overview of the scaling and deployment strategy.

## 🤖 AI Development Workflow
This project was built using a hybrid workflow. I handled the core layout logic, DOM structure, CSS grid systems, and state management manually. AI was leveraged specifically for generating SVG assets, boilerplate configuration, and complex CSS transitions. Please refer to `ai_prompts.txt` for the exact sequence of 44 prompts utilized during the 5-hour development timeframe.
