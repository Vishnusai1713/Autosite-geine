# Professional Templates Configuration
# Defines all profession-specific templates with styling, content, and features

PROFESSIONS = {
    "doctor": {
        "title": "Medical Professional Portfolio",
        "description": "Professional healthcare provider website",
        "colors": {
            "primary": "#0066cc",
            "secondary": "#e8f4f8",
            "accent": "#00a86b",
            "text": "#1a1a1a",
            "light_text": "#666666"
        },
        "sections": ["about", "services", "qualifications", "contact"],
        "features": ["appointment_form", "services_grid", "testimonials"],
        "icon": "🏥"
    },
    "mechanic": {
        "title": "Automotive Mechanic Shop",
        "description": "Professional auto repair and maintenance services",
        "colors": {
            "primary": "#d32f2f",
            "secondary": "#fff3e0",
            "accent": "#ff6f00",
            "text": "#212121",
            "light_text": "#757575"
        },
        "sections": ["about", "services", "gallery", "contact"],
        "features": ["service_cards", "before_after_gallery", "pricing"],
        "icon": "🔧"
    },
    "electrician": {
        "title": "Electrical Services",
        "description": "Professional electrical installation and repair",
        "colors": {
            "primary": "#ffc107",
            "secondary": "#fff8e1",
            "accent": "#ff6f00",
            "text": "#212121",
            "light_text": "#666666"
        },
        "sections": ["about", "services", "projects", "contact"],
        "features": ["service_list", "project_showcase", "cta_button"],
        "icon": "⚡"
    },
    "architect": {
        "title": "Architectural Design Studio",
        "description": "Modern architecture and design portfolio",
        "colors": {
            "primary": "#2c3e50",
            "secondary": "#ecf0f1",
            "accent": "#3498db",
            "text": "#2c3e50",
            "light_text": "#7f8c8d"
        },
        "sections": ["about", "portfolio", "services", "contact"],
        "features": ["project_grid", "image_gallery", "testimonials"],
        "icon": "🏗️"
    },
    "gamer": {
        "title": "Gaming Profile & Portfolio",
        "description": "Professional gamer streaming and content portfolio",
        "colors": {
            "primary": "#1a1a2e",
            "secondary": "#16213e",
            "accent": "#0f3460",
            "text": "#eaeaea",
            "light_text": "#a0a0a0"
        },
        "sections": ["about", "achievements", "streams", "contact"],
        "features": ["stats_display", "achievement_badges", "social_links"],
        "icon": "🎮"
    },
    "photographer": {
        "title": "Photography Portfolio",
        "description": "Professional photography showcase",
        "colors": {
            "primary": "#ffffff",
            "secondary": "#f5f5f5",
            "accent": "#000000",
            "text": "#333333",
            "light_text": "#666666"
        },
        "sections": ["about", "gallery", "services", "contact"],
        "features": ["image_gallery", "lightbox", "pricing"],
        "icon": "📸"
    },
    "programmer": {
        "title": "Developer Portfolio",
        "description": "Software developer and tech professional",
        "colors": {
            "primary": "#1e1e2f",
            "secondary": "#16213e",
            "accent": "#00ffd5",
            "text": "#eaeaea",
            "light_text": "#a0a0a0"
        },
        "sections": ["about", "projects", "skills", "contact"],
        "features": ["project_cards", "skill_bars", "github_link"],
        "icon": "💻"
    },
    "chef": {
        "title": "Chef & Culinary Portfolio",
        "description": "Professional chef and restaurant services",
        "colors": {
            "primary": "#8b4513",
            "secondary": "#fff8dc",
            "accent": "#d2691e",
            "text": "#2f1f0f",
            "light_text": "#654321"
        },
        "sections": ["about", "menu", "gallery", "contact"],
        "features": ["menu_showcase", "food_gallery", "reservation_form"],
        "icon": "👨‍🍳"
    },
    "fitness": {
        "title": "Fitness Coach & Trainer",
        "description": "Personal training and fitness services",
        "colors": {
            "primary": "#ff6b6b",
            "secondary": "#ffe0e0",
            "accent": "#4ecdc4",
            "text": "#2d3436",
            "light_text": "#636e72"
        },
        "sections": ["about", "services", "testimonials", "contact"],
        "features": ["service_cards", "transformation_gallery", "pricing"],
        "icon": "💪"
    },
    "realtor": {
        "title": "Real Estate Agent",
        "description": "Property listings and real estate services",
        "colors": {
            "primary": "#2c5f2d",
            "secondary": "#e8f5e9",
            "accent": "#ff9800",
            "text": "#1b1b1b",
            "light_text": "#555555"
        },
        "sections": ["about", "listings", "services", "contact"],
        "features": ["property_cards", "search_filter", "contact_form"],
        "icon": "🏠"
    }
}

# Default theme for unknown professions
DEFAULT_THEME = {
    "title": "Professional Portfolio",
    "description": "Your professional online presence",
    "colors": {
        "primary": "#3498db",
        "secondary": "#ecf0f1",
        "accent": "#2ecc71",
        "text": "#2c3e50",
        "light_text": "#7f8c8d"
    },
    "sections": ["about", "services", "contact"],
    "features": ["basic_info", "contact_form"],
    "icon": "🌟"
}
