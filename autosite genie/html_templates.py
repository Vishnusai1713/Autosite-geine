# HTML Template Generator
# Creates professional, responsive HTML for each profession

def generate_html(profession, name, theme):
    """Generate complete HTML for a profession"""
    
    title = theme.get("title", "Professional Portfolio")
    colors = theme.get("colors", {})
    
    # Extract colors with defaults
    primary = colors.get("primary", "#3498db")
    secondary = colors.get("secondary", "#ecf0f1")
    accent = colors.get("accent", "#2ecc71")
    text_color = colors.get("text", "#2c3e50")
    light_text = colors.get("light_text", "#7f8c8d")
    
    # Profession-specific content
    content_sections = get_profession_content(profession, name, primary, accent)
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&family=Playfair+Display:wght@700&display=swap" rel="stylesheet">
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Poppins', sans-serif;
            background-color: {secondary};
            color: {text_color};
            line-height: 1.6;
        }}
        
        header {{
            background: linear-gradient(135deg, {primary} 0%, {accent} 100%);
            color: white;
            padding: 60px 20px;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}
        
        header h1 {{
            font-family: 'Playfair Display', serif;
            font-size: 3em;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        }}
        
        header p {{
            font-size: 1.2em;
            opacity: 0.95;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 40px 20px;
        }}
        
        section {{
            margin: 40px 0;
            padding: 40px;
            background: white;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.08);
        }}
        
        section h2 {{
            color: {primary};
            font-size: 2em;
            margin-bottom: 30px;
            border-bottom: 3px solid {accent};
            padding-bottom: 15px;
        }}
        
        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 25px;
            margin-top: 20px;
        }}
        
        .card {{
            background: {secondary};
            padding: 25px;
            border-radius: 8px;
            border-left: 4px solid {accent};
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }}
        
        .card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }}
        
        .card h3 {{
            color: {primary};
            margin-bottom: 10px;
            font-size: 1.3em;
        }}
        
        .card p {{
            color: {light_text};
            font-size: 0.95em;
        }}
        
        .btn {{
            display: inline-block;
            background: linear-gradient(135deg, {primary} 0%, {accent} 100%);
            color: white;
            padding: 12px 30px;
            border-radius: 5px;
            text-decoration: none;
            font-weight: 600;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            border: none;
            cursor: pointer;
            font-size: 1em;
        }}
        
        .btn:hover {{
            transform: scale(1.05);
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }}
        
        .contact-form {{
            display: flex;
            flex-direction: column;
            gap: 15px;
            max-width: 500px;
        }}
        
        .contact-form input,
        .contact-form textarea {{
            padding: 12px;
            border: 2px solid {secondary};
            border-radius: 5px;
            font-family: 'Poppins', sans-serif;
            font-size: 1em;
            transition: border-color 0.3s ease;
        }}
        
        .contact-form input:focus,
        .contact-form textarea:focus {{
            outline: none;
            border-color: {primary};
        }}
        
        footer {{
            background: {primary};
            color: white;
            text-align: center;
            padding: 30px 20px;
            margin-top: 60px;
        }}
        
        footer p {{
            opacity: 0.9;
        }}
        
        .stats {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 20px;
            margin: 30px 0;
        }}
        
        .stat-box {{
            background: {secondary};
            padding: 20px;
            border-radius: 8px;
            text-align: center;
        }}
        
        .stat-box .number {{
            font-size: 2.5em;
            color: {accent};
            font-weight: 700;
        }}
        
        .stat-box .label {{
            color: {light_text};
            margin-top: 10px;
        }}
        
        @media (max-width: 768px) {{
            header h1 {{
                font-size: 2em;
            }}
            
            section {{
                padding: 20px;
            }}
            
            .grid {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>
</head>
<body>
    <header>
        <h1>{title}</h1>
        <p>Professional Online Presence</p>
    </header>
    
    <div class="container">
        {content_sections}
    </div>
    
    <footer>
        <p>Generated with AutoSite Genie | Professional Website Generator</p>
        <p>© 2025 All Rights Reserved</p>
    </footer>
    
    <script>
        // Smooth scroll for navigation
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {{
            anchor.addEventListener('click', function (e) {{
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {{
                    target.scrollIntoView({{ behavior: 'smooth' }});
                }}
            }});
        }});
        
        // Form submission handler
        const form = document.querySelector('.contact-form');
        if (form) {{
            form.addEventListener('submit', function(e) {{
                e.preventDefault();
                alert('Thank you for your message! We will get back to you soon.');
                this.reset();
            }});
        }}
    </script>
</body>
</html>"""
    
    return html

def get_profession_content(profession, name, primary, accent):
    """Generate profession-specific content sections"""
    
    name_text = f" - {name}" if name else ""
    
    content_map = {
        "doctor": f"""
        <section id="about">
            <h2>About Me</h2>
            <p>Dedicated healthcare professional with years of experience providing compassionate and comprehensive medical care. Committed to patient wellness and preventive health.</p>
        </section>
        
        <section id="services">
            <h2>Services Offered</h2>
            <div class="grid">
                <div class="card">
                    <h3>General Consultation</h3>
                    <p>Comprehensive health assessments and medical consultations for all ages.</p>
                </div>
                <div class="card">
                    <h3>Preventive Care</h3>
                    <p>Health screenings and preventive measures to maintain optimal wellness.</p>
                </div>
                <div class="card">
                    <h3>Chronic Disease Management</h3>
                    <p>Specialized care for managing long-term health conditions.</p>
                </div>
                <div class="card">
                    <h3>Emergency Care</h3>
                    <p>Prompt and professional emergency medical services.</p>
                </div>
            </div>
        </section>
        
        <section id="contact">
            <h2>Get in Touch</h2>
            <form class="contact-form" onsubmit="event.preventDefault(); alert('Appointment request received!');">
                <input type="text" placeholder="Your Name" required>
                <input type="email" placeholder="Your Email" required>
                <input type="tel" placeholder="Phone Number" required>
                <textarea placeholder="Message or Appointment Request" rows="5" required></textarea>
                <button type="submit" class="btn">Request Appointment</button>
            </form>
        </section>
        """,
        
        "mechanic": f"""
        <section id="about">
            <h2>About Our Shop</h2>
            <p>Professional automotive repair and maintenance services with certified technicians. We pride ourselves on quality workmanship and customer satisfaction.</p>
        </section>
        
        <section id="services">
            <h2>Services</h2>
            <div class="grid">
                <div class="card">
                    <h3>Engine Repair</h3>
                    <p>Complete engine diagnostics and repair services for all vehicle types.</p>
                </div>
                <div class="card">
                    <h3>Brake Service</h3>
                    <p>Professional brake inspection, repair, and replacement.</p>
                </div>
                <div class="card">
                    <h3>Transmission Work</h3>
                    <p>Expert transmission repair and maintenance services.</p>
                </div>
                <div class="card">
                    <h3>Oil Changes & Maintenance</h3>
                    <p>Regular maintenance to keep your vehicle running smoothly.</p>
                </div>
            </div>
        </section>
        
        <section id="contact">
            <h2>Contact Us</h2>
            <form class="contact-form" onsubmit="event.preventDefault(); alert('Service request received!');">
                <input type="text" placeholder="Your Name" required>
                <input type="email" placeholder="Your Email" required>
                <input type="text" placeholder="Vehicle Make & Model" required>
                <textarea placeholder="Describe the issue" rows="5" required></textarea>
                <button type="submit" class="btn">Request Service</button>
            </form>
        </section>
        """,
        
        "electrician": f"""
        <section id="about">
            <h2>About Our Services</h2>
            <p>Licensed and insured electrical contractor providing professional installation, repair, and maintenance services for residential and commercial properties.</p>
        </section>
        
        <section id="services">
            <h2>Electrical Services</h2>
            <div class="grid">
                <div class="card">
                    <h3>Residential Wiring</h3>
                    <p>Complete electrical installation and rewiring for homes.</p>
                </div>
                <div class="card">
                    <h3>Commercial Installation</h3>
                    <p>Professional electrical systems for businesses and commercial spaces.</p>
                </div>
                <div class="card">
                    <h3>Emergency Repairs</h3>
                    <p>24/7 emergency electrical repair services.</p>
                </div>
                <div class="card">
                    <h3>Panel Upgrades</h3>
                    <p>Electrical panel installation and upgrades for increased capacity.</p>
                </div>
            </div>
        </section>
        
        <section id="contact">
            <h2>Get a Free Quote</h2>
            <form class="contact-form" onsubmit="event.preventDefault(); alert('Quote request submitted!');">
                <input type="text" placeholder="Your Name" required>
                <input type="email" placeholder="Your Email" required>
                <input type="tel" placeholder="Phone Number" required>
                <textarea placeholder="Describe your electrical needs" rows="5" required></textarea>
                <button type="submit" class="btn">Request Quote</button>
            </form>
        </section>
        """,
        
        "architect": f"""
        <section id="about">
            <h2>About Our Studio</h2>
            <p>Award-winning architectural design studio specializing in innovative, sustainable, and functional design solutions for residential and commercial projects.</p>
        </section>
        
        <section id="portfolio">
            <h2>Featured Projects</h2>
            <div class="grid">
                <div class="card">
                    <h3>Modern Residential Complex</h3>
                    <p>Contemporary apartment building with sustainable design features and community spaces.</p>
                </div>
                <div class="card">
                    <h3>Corporate Office Building</h3>
                    <p>State-of-the-art office space designed for collaboration and productivity.</p>
                </div>
                <div class="card">
                    <h3>Retail Development</h3>
                    <p>Mixed-use retail and residential development in urban center.</p>
                </div>
                <div class="card">
                    <h3>Sustainable Housing</h3>
                    <p>Eco-friendly residential community with green building standards.</p>
                </div>
            </div>
        </section>
        
        <section id="contact">
            <h2>Start Your Project</h2>
            <form class="contact-form" onsubmit="event.preventDefault(); alert('Project inquiry received!');">
                <input type="text" placeholder="Your Name" required>
                <input type="email" placeholder="Your Email" required>
                <input type="text" placeholder="Project Type" required>
                <textarea placeholder="Tell us about your project vision" rows="5" required></textarea>
                <button type="submit" class="btn">Schedule Consultation</button>
            </form>
        </section>
        """,
        
        "gamer": f"""
        <section id="about">
            <h2>About Me</h2>
            <p>Professional gamer and content creator with years of competitive experience. Streaming daily and creating engaging gaming content for the community.</p>
        </section>
        
        <section id="stats">
            <h2>Gaming Stats</h2>
            <div class="stats">
                <div class="stat-box">
                    <div class="number">500K+</div>
                    <div class="label">Followers</div>
                </div>
                <div class="stat-box">
                    <div class="number">2.5M+</div>
                    <div class="label">Total Views</div>
                </div>
                <div class="stat-box">
                    <div class="number">50+</div>
                    <div class="label">Tournament Wins</div>
                </div>
                <div class="stat-box">
                    <div class="number">24/7</div>
                    <div class="label">Stream Schedule</div>
                </div>
            </div>
        </section>
        
        <section id="contact">
            <h2>Connect With Me</h2>
            <div style="text-align: center;">
                <p style="margin-bottom: 20px;">Follow me on social media and join the community!</p>
                <button class="btn" onclick="alert('Twitch: YourChannel')">Twitch</button>
                <button class="btn" onclick="alert('YouTube: YourChannel')" style="margin-left: 10px;">YouTube</button>
                <button class="btn" onclick="alert('Discord: YourServer')" style="margin-left: 10px;">Discord</button>
            </div>
        </section>
        """,
        
        "photographer": f"""
        <section id="about">
            <h2>About My Work</h2>
            <p>Professional photographer specializing in capturing life's most precious moments. With a keen eye for detail and passion for storytelling through images.</p>
        </section>
        
        <section id="gallery">
            <h2>Portfolio Gallery</h2>
            <div class="grid">
                <div class="card">
                    <h3>Weddings</h3>
                    <p>Capturing the love and joy of your special day with artistic vision.</p>
                </div>
                <div class="card">
                    <h3>Portraits</h3>
                    <p>Professional portrait photography that reveals personality and character.</p>
                </div>
                <div class="card">
                    <h3>Events</h3>
                    <p>Corporate and private event photography with comprehensive coverage.</p>
                </div>
                <div class="card">
                    <h3>Nature & Landscapes</h3>
                    <p>Stunning landscape and nature photography from around the world.</p>
                </div>
            </div>
        </section>
        
        <section id="contact">
            <h2>Book a Session</h2>
            <form class="contact-form" onsubmit="event.preventDefault(); alert('Booking inquiry received!');">
                <input type="text" placeholder="Your Name" required>
                <input type="email" placeholder="Your Email" required>
                <input type="text" placeholder="Session Type" required>
                <textarea placeholder="Tell me about your vision" rows="5" required></textarea>
                <button type="submit" class="btn">Request Booking</button>
            </form>
        </section>
        """,
        
        "programmer": f"""
        <section id="about">
            <h2>About Me</h2>
            <p>Full-stack developer with expertise in modern web technologies. Passionate about creating efficient, scalable, and user-friendly applications.</p>
        </section>
        
        <section id="skills">
            <h2>Technical Skills</h2>
            <div class="grid">
                <div class="card">
                    <h3>Frontend Development</h3>
                    <p>React, Vue.js, TypeScript, Tailwind CSS, and modern JavaScript frameworks.</p>
                </div>
                <div class="card">
                    <h3>Backend Development</h3>
                    <p>Node.js, Python, PostgreSQL, MongoDB, and RESTful API design.</p>
                </div>
                <div class="card">
                    <h3>DevOps & Cloud</h3>
                    <p>Docker, AWS, CI/CD pipelines, and cloud infrastructure management.</p>
                </div>
                <div class="card">
                    <h3>Mobile Development</h3>
                    <p>React Native and cross-platform mobile application development.</p>
                </div>
            </div>
        </section>
        
        <section id="contact">
            <h2>Let's Work Together</h2>
            <form class="contact-form" onsubmit="event.preventDefault(); alert('Message received!');">
                <input type="text" placeholder="Your Name" required>
                <input type="email" placeholder="Your Email" required>
                <input type="text" placeholder="Project Type" required>
                <textarea placeholder="Describe your project" rows="5" required></textarea>
                <button type="submit" class="btn">Send Message</button>
            </form>
        </section>
        """,
        
        "chef": f"""
        <section id="about">
            <h2>About My Cuisine</h2>
            <p>Professional chef with expertise in contemporary and traditional cuisine. Dedicated to creating memorable dining experiences with fresh, quality ingredients.</p>
        </section>
        
        <section id="menu">
            <h2>Signature Dishes</h2>
            <div class="grid">
                <div class="card">
                    <h3>Pan-Seared Salmon</h3>
                    <p>Fresh Atlantic salmon with seasonal vegetables and lemon butter sauce.</p>
                </div>
                <div class="card">
                    <h3>Truffle Risotto</h3>
                    <p>Creamy arborio rice with black truffle and parmesan cheese.</p>
                </div>
                <div class="card">
                    <h3>Beef Wellington</h3>
                    <p>Prime beef tenderloin wrapped in mushroom duxelles and puff pastry.</p>
                </div>
                <div class="card">
                    <h3>Chocolate Soufflé</h3>
                    <p>Decadent dark chocolate soufflé with vanilla bean ice cream.</p>
                </div>
            </div>
        </section>
        
        <section id="contact">
            <h2>Reserve Your Table</h2>
            <form class="contact-form" onsubmit="event.preventDefault(); alert('Reservation request received!');">
                <input type="text" placeholder="Your Name" required>
                <input type="email" placeholder="Your Email" required>
                <input type="tel" placeholder="Phone Number" required>
                <input type="date" required>
                <textarea placeholder="Special requests or dietary requirements" rows="4"></textarea>
                <button type="submit" class="btn">Make Reservation</button>
            </form>
        </section>
        """,
        
        "fitness": f"""
        <section id="about">
            <h2>About My Training</h2>
            <p>Certified fitness coach specializing in personalized training programs. Dedicated to helping clients achieve their health and fitness goals through expert guidance and motivation.</p>
        </section>
        
        <section id="services">
            <h2>Training Services</h2>
            <div class="grid">
                <div class="card">
                    <h3>Personal Training</h3>
                    <p>One-on-one customized workout programs tailored to your goals.</p>
                </div>
                <div class="card">
                    <h3>Group Classes</h3>
                    <p>High-energy group fitness classes including HIIT, yoga, and strength training.</p>
                </div>
                <div class="card">
                    <h3>Nutrition Coaching</h3>
                    <p>Personalized nutrition plans to complement your fitness journey.</p>
                </div>
                <div class="card">
                    <h3>Online Training</h3>
                    <p>Remote coaching and workout programs for busy schedules.</p>
                </div>
            </div>
        </section>
        
        <section id="contact">
            <h2>Start Your Transformation</h2>
            <form class="contact-form" onsubmit="event.preventDefault(); alert('Consultation request received!');">
                <input type="text" placeholder="Your Name" required>
                <input type="email" placeholder="Your Email" required>
                <input type="tel" placeholder="Phone Number" required>
                <textarea placeholder="Tell me about your fitness goals" rows="5" required></textarea>
                <button type="submit" class="btn">Book Free Consultation</button>
            </form>
        </section>
        """,
        
        "realtor": f"""
        <section id="about">
            <h2>About My Services</h2>
            <p>Professional real estate agent with extensive market knowledge. Dedicated to helping buyers and sellers achieve their real estate goals with integrity and expertise.</p>
        </section>
        
        <section id="listings">
            <h2>Featured Properties</h2>
            <div class="grid">
                <div class="card">
                    <h3>Modern Downtown Condo</h3>
                    <p>Luxury 2-bedroom condo in prime downtown location. $450,000</p>
                </div>
                <div class="card">
                    <h3>Suburban Family Home</h3>
                    <p>4-bedroom house with large yard and excellent schools. $550,000</p>
                </div>
                <div class="card">
                    <h3>Investment Property</h3>
                    <p>Multi-unit rental property with strong cash flow. $750,000</p>
                </div>
                <div class="card">
                    <h3>Waterfront Estate</h3>
                    <p>Luxury waterfront home with private beach access. $1,200,000</p>
                </div>
            </div>
        </section>
        
        <section id="contact">
            <h2>Find Your Dream Home</h2>
            <form class="contact-form" onsubmit="event.preventDefault(); alert('Inquiry received!');">
                <input type="text" placeholder="Your Name" required>
                <input type="email" placeholder="Your Email" required>
                <input type="tel" placeholder="Phone Number" required>
                <input type="text" placeholder="Budget Range" required>
                <textarea placeholder="What are you looking for?" rows="4" required></textarea>
                <button type="submit" class="btn">Schedule Showing</button>
            </form>
        </section>
        """
    }
    
    return content_map.get(profession, f"""
        <section id="about">
            <h2>Welcome</h2>
            <p>Professional portfolio website created with AutoSite Genie. Showcase your skills, services, and expertise to the world.</p>
        </section>
        
        <section id="contact">
            <h2>Get in Touch</h2>
            <form class="contact-form" onsubmit="event.preventDefault(); alert('Message received!');">
                <input type="text" placeholder="Your Name" required>
                <input type="email" placeholder="Your Email" required>
                <textarea placeholder="Your Message" rows="5" required></textarea>
                <button type="submit" class="btn">Send Message</button>
            </form>
        </section>
    """)
