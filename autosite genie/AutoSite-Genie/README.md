# AutoSite Genie - Professional Website Generator

A powerful Python-based tool that generates professional, responsive websites for various professions with beautiful designs and interactive features.

## Features

- **10 Professional Templates**: Doctor, Mechanic, Electrician, Architect, Gamer, Photographer, Programmer, Chef, Fitness Coach, and Realtor
- **Responsive Design**: Mobile-friendly websites that work on all devices
- **Professional Styling**: Modern gradients, smooth animations, and hover effects
- **Interactive Forms**: Contact forms with validation and submission handling
- **Easy to Use**: Simple GUI for selecting profession and generating websites
- **Customizable**: Easy to add new professions and modify existing templates

## Installation

1. Make sure you have Python 3.7+ installed
2. No external dependencies required - uses only Python's built-in `tkinter` library

## Usage

1. Run the application:
   \`\`\`bash
   python site_generator.py
   \`\`\`

2. Select a profession from the dropdown menu
3. Optionally enter your name
4. Click "Generate Website"
5. Your website will be saved in the `output` folder

## File Structure

\`\`\`
AutoSite-Genie/
├── site_generator.py      # Main GUI application
├── templates_config.py    # Profession configurations and themes
├── html_templates.py      # HTML template generator
├── output/                # Generated websites (created automatically)
└── README.md             # This file
\`\`\`

## Supported Professions

- Doctor (Medical Professional)
- Mechanic (Automotive Services)
- Electrician (Electrical Services)
- Architect (Design Studio)
- Gamer (Gaming Profile)
- Photographer (Photography Portfolio)
- Programmer (Developer Portfolio)
- Chef (Culinary Services)
- Fitness Coach (Personal Training)
- Realtor (Real Estate Agent)

## Customization

### Adding a New Profession

1. Open `templates_config.py`
2. Add a new entry to the `PROFESSIONS` dictionary with:
   - Title
   - Description
   - Color scheme (primary, secondary, accent, text colors)
   - Sections
   - Features
   - Icon

3. Open `html_templates.py`
4. Add profession-specific content to the `content_map` in `get_profession_content()` function

### Modifying Colors

Edit the color values in `templates_config.py` for any profession to customize the appearance.

## Generated Website Features

Each generated website includes:
- Professional header with gradient background
- Responsive grid layouts
- Interactive cards with hover effects
- Contact forms with validation
- Professional typography
- Mobile-responsive design
- Smooth scrolling navigation
- Footer with copyright information

## Technical Details

- **Frontend**: Pure HTML, CSS, and JavaScript (no frameworks)
- **Backend**: Python with Tkinter GUI
- **Styling**: CSS3 with gradients, animations, and media queries
- **Fonts**: Google Fonts (Poppins and Playfair Display)

## License

Free to use and modify for personal and commercial projects.

## Support

For issues or feature requests, feel free to modify the code and customize it to your needs!
