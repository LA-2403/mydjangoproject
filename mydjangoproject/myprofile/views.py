
from django.http import HttpResponse


def profile(request):
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Lavanya Jain R | Portfolio</title>

        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
                scroll-behavior: smooth;
            }

            body {
                font-family: 'Segoe UI', Arial, sans-serif;
                background: #f8f7fc;
                color: #29263d;
                line-height: 1.7;
            }

            nav {
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 20px 8%;
                background: #ffffff;
                box-shadow: 0 2px 15px #29263d0d;
                position: sticky;
                top: 0;
                z-index: 10;
                flex-wrap: wrap;
                gap: 12px;
            }

            .logo {
                font-size: 22px;
                font-weight: 800;
                color: #7655c9;
            }

            nav a {
                text-decoration: none;
                color: #49445c;
                margin-left: 18px;
                font-size: 14px;
                font-weight: 600;
            }

            nav a:hover {
                color: #7655c9;
            }

            .hero {
                padding: 100px 8%;
                display: flex;
                align-items: center;
                justify-content: space-between;
                gap: 50px;
                background: linear-gradient(135deg, #f0eaff, #fff8f5);
            }

            .hero-content {
                max-width: 700px;
            }

            .tag {
                display: inline-block;
                background: #e6dcff;
                color: #6542b2;
                padding: 7px 15px;
                border-radius: 30px;
                font-size: 13px;
                font-weight: 700;
                margin-bottom: 20px;
            }

            h1 {
                font-size: clamp(38px, 5vw, 64px);
                line-height: 1.15;
                margin-bottom: 20px;
            }

            .accent {
                color: #7655c9;
            }

            .hero p {
                color: #68637a;
                font-size: 17px;
                max-width: 580px;
            }

            .hero-buttons {
                margin-top: 30px;
                display: flex;
                flex-wrap: wrap;
                gap: 12px;
            }

            .btn {
                display: inline-block;
                text-decoration: none;
                padding: 12px 23px;
                border-radius: 9px;
                font-weight: 700;
                font-size: 14px;
            }

            .primary {
                background: #7655c9;
                color: white;
            }

            .secondary {
                border: 1px solid #7655c9;
                color: #7655c9;
            }

            .avatar {
                min-width: 190px;
                width: 230px;
                height: 230px;
                border-radius: 50%;
                background: linear-gradient(135deg, #d9caff, #f9dce8);
                border: 8px solid white;
                display: flex;
                align-items: center;
                justify-content: center;
                color: #6542b2;
                font-size: 64px;
                font-weight: 800;
                box-shadow: 0 15px 40px #7655c922;
            }

            section {
                padding: 75px 8%;
            }

            .section-heading {
                text-align: center;
                margin-bottom: 40px;
            }

            .section-heading h2 {
                font-size: 32px;
                margin-bottom: 8px;
            }

            .section-heading p {
                color: #777187;
            }

            .about {
                max-width: 850px;
                margin: auto;
                text-align: center;
                color: #68637a;
                font-size: 17px;
            }

            .skills-grid, .cards, .education-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
                gap: 22px;
            }

            .card {
                background: white;
                padding: 27px;
                border-radius: 16px;
                border: 1px solid #eee9f8;
                box-shadow: 0 8px 25px #29263d08;
                transition: transform 0.2s;
            }

            .card:hover {
                transform: translateY(-5px);
            }

            .card h3 {
                margin-bottom: 12px;
                color: #7655c9;
                font-size: 19px;
            }

            .card p, .card li {
                color: #6d687d;
                font-size: 14px;
            }

            .card ul {
                padding-left: 18px;
            }

            .skill-list {
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
                gap: 12px;
            }

            .skill {
                background: white;
                border: 1px solid #e6def8;
                color: #6542b2;
                border-radius: 30px;
                padding: 10px 18px;
                font-size: 14px;
                font-weight: 600;
            }

            .project-label {
                display: inline-block;
                background: #f0eaff;
                color: #6542b2;
                padding: 4px 10px;
                border-radius: 6px;
                font-size: 12px;
                margin-bottom: 12px;
            }

            .muted {
                color: #8a849b;
                font-size: 13px;
                margin-bottom: 12px;
            }

            .contact {
                text-align: center;
                background: #eee8ff;
            }

            .contact p {
                color: #68637a;
                margin: 10px auto 25px;
            }

            footer {
                text-align: center;
                padding: 25px;
                color: #777187;
                font-size: 13px;
                background: white;
            }

            @media (max-width: 700px) {
                nav {
                    justify-content: center;
                }

                nav a {
                    margin: 0 7px;
                }

                .hero {
                    padding: 65px 7%;
                    flex-direction: column-reverse;
                    text-align: center;
                }

                .hero-buttons {
                    justify-content: center;
                }

                .avatar {
                    width: 170px;
                    height: 170px;
                    min-width: 170px;
                    font-size: 48px;
                }

                section {
                    padding: 55px 7%;
                }
            }
        </style>
    </head>

    <body>

        <nav>
            <div class="logo">LJ.</div>
            <div>
                <a href="#about">About</a>
                <a href="#skills">Skills</a>
                <a href="#education">Education</a>
                <a href="#projects">Projects</a>
                <a href="#achievements">Achievements</a>
            </div>
        </nav>

        <header class="hero">
            <div class="hero-content">
                <span class="tag">COMPUTER SCIENCE STUDENT</span>
                <h1>Hi, I'm <span class="accent">Lavanya Jain R.</span></h1>
                <p>
                    A Computer Science Engineering student passionate about
                    technology, software development and building meaningful
                    solutions to real-world problems.
                </p>
                <div class="hero-buttons">
                    <a href="#projects" class="btn primary">Explore My Work</a>
                    <a href="#contact" class="btn secondary">Get In Touch</a>
                </div>
            </div>

            <div class="avatar" aria-label="Lavanya Jain initials">
                LJ
            </div>
        </header>

        <section id="about">
            <div class="section-heading">
                <h2>About Me</h2>
                <p>A little about my journey</p>
            </div>
            <div class="about">
                <p>
                    I'm pursuing a Bachelor of Engineering in Computer Science
                    and Engineering at Gopalan College of Engineering and
                    Management. I enjoy learning new technologies, solving
                    problems and collaborating with teams to turn ideas into
                    practical projects. Through projects and hackathons, I'm
                    continuously developing my technical and problem-solving
                    skills.
                </p>
            </div>
        </section>

        <section id="skills">
            <div class="section-heading">
                <h2>My Skills</h2>
                <p>Technologies and strengths I'm developing</p>
            </div>
            <div class="skill-list">
                <span class="skill">C Programming</span>
                <span class="skill">Python</span>
                <span class="skill">Problem Solving</span>
                <span class="skill">Teamwork</span>
                <span class="skill">Leadership</span>
                <span class="skill">Adaptability</span>
                <span class="skill">Flutter</span>
                <span class="skill">Dart</span>
                <span class="skill">FastAPI</span>
                <span class="skill">ChromaDB</span>
            </div>
        </section>

        <section id="education">
            <div class="section-heading">
                <h2>Education</h2>
                <p>My academic background</p>
            </div>
            <div class="education-grid">
                <div class="card">
                    <h3>B.E. Computer Science</h3>
                    <p>Gopalan College of Engineering and Management</p>
                    <p class="muted">2024 – 2028</p>
                </div>

                <div class="card">
                    <h3>Class XII — PCMB</h3>
                    <p>Charan's Pre University College</p>
                    <p class="muted">2022</p>
                </div>

                <div class="card">
                    <h3>Class X</h3>
                    <p>Holy Angels Public School</p>
                    <p class="muted">2020</p>
                </div>
            </div>
        </section>

        <section id="projects">
            <div class="section-heading">
                <h2>Featured Projects</h2>
                <p>Ideas I've worked on</p>
            </div>

            <div class="cards">
                <div class="card">
                    <span class="project-label">Mobile Application</span>
                    <h3>LibraryNest</h3>
                    <p class="muted">Flutter · Dart</p>
                    <p>
                        A library management application designed to provide
                        users with a convenient way to interact with library
                        services through a mobile interface.
                    </p>
                </div>

                <div class="card">
                    <span class="project-label">Artificial Intelligence</span>
                    <h3>Nyaya-Setu</h3>
                    <p class="muted">Python · FastAPI · ChromaDB</p>
                    <p>
                        An AI-powered legal assistance project designed to
                        help users understand legal information and support
                        the preparation of FIR and complaint drafts.
                    </p>
                </div>
            </div>
        </section>

        <section id="certifications">
            <div class="section-heading">
                <h2>Certifications</h2>
                <p>Courses and learning milestones</p>
            </div>

            <div class="cards">
                <div class="card">
                    <h3>Python Programming</h3>
                    <p>Infosys Springboard</p>
                </div>

                <div class="card">
                    <h3>Analysis and Design of Algorithms</h3>
                    <p>Coursera</p>
                </div>

                <div class="card">
                    <h3>Operating Systems</h3>
                    <p>Coursera</p>
                </div>

                <div class="card">
                    <h3>Data Structures</h3>
                    <p>Coursera</p>
                </div>
            </div>
        </section>

        <section id="achievements">
            <div class="section-heading">
                <h2>Achievements</h2>
                <p>Experiences that motivate me to keep growing</p>
            </div>

            <div class="cards">
                <div class="card">
                    <h3>GCEM Hacks 4.0</h3>
                    <p>
                        Secured 4th place in the hackathon, collaborating
                        to develop and present a project.
                    </p>
                </div>

                <div class="card">
                    <h3>BuildWithAI Hackathon</h3>
                    <p>
                        Achieved 4th place at the BuildWithAI Hackathon
                        held at Presidency University.
                    </p>
                </div>

                <div class="card">
                    <h3>Smart India Hackathon</h3>
                    <p>
                        Selected through the college's internal round
                        for the Smart India Hackathon.
                    </p>
                </div>
            </div>
        </section>

        <section id="contact" class="contact">
            <div class="section-heading">
                <h2>Let's Connect</h2>
            </div>
            <p>
                Interested in technology, collaboration and new opportunities?
                I'd love to connect.
            </p>
            <p>Lavanya Jain R · Computer Science Engineering</p>
        </section>

        <footer>
            <p>© 2026 Lavanya Jain R. Built with Django and Python.</p>
        </footer>

    </body>
    </html>
    """

    return HttpResponse(html)
