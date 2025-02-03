from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, 'Rohan Naagar - Resume', border=False, ln=True, align='C')
        self.ln(10)

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, ln=True, border=False, align='L')
        self.ln(5)

    def chapter_body(self, body):
        self.set_font('Arial', '', 11)
        self.multi_cell(0, 10, body)
        self.ln()

# Create a PDF instance
pdf = PDF()
pdf.add_page()

# Header Details
pdf.set_font('Arial', '', 11)
pdf.cell(0, 10, "🌍 Location: Gurgaon, Haryana, India", ln=True)
pdf.cell(0, 10, "✉️ Email: Rohan150907@gmail.com", ln=True)
pdf.cell(0, 10, "📞 Phone: +91 9466386495", ln=True)
pdf.cell(0, 10, "🔗 LinkedIn: Rohan Naagar", ln=True)
pdf.ln(10)

# Objective Section
pdf.chapter_title('🚀 Objective')
objective = ("Innovative and passionate Cybersecurity Engineer with a strong foundation in technology. "
             "I aim to utilize my expertise in cybersecurity and IT management to bolster organizational "
             "security, drive technological advancements, and create impactful solutions.")
pdf.chapter_body(objective)

# Education Section
pdf.chapter_title('🎓 Education')
education = ("📖 Master of Technology (M.Tech) in Cyber Security\n"
             "Gurgaon University, [Year of Graduation]\n\n"
             "📖 Bachelor of Technology (B.Tech) in Cyber Security\n"
             "Gurgaon University, [Year of Graduation]\n\n"
             "📖 12th Science\n"
             "Torch Bearer Convent School, [Year of Graduation]\n\n"
             "📖 10th Science\n"
             "Torch Bearer Convent School, [Year of Graduation]")
pdf.chapter_body(education)

# Professional Experience Section
pdf.chapter_title('💼 Professional Experience')
experience = ("🖥️ IT Head\n"
              "RxpexInfinity, Faridabad, Haryana\n"
              "September 2024 – Present\n"
              "- 💡 Spearheaded IT operations, delivering cutting-edge technology solutions.\n"
              "- 👨‍💻 Managed teams to enhance security systems and optimize IT processes.\n"
              "- 🔐 Designed and implemented robust cybersecurity protocols, protecting sensitive data.\n\n"
              "🔒 Founder & Cybersecurity Consultant\n"
              "RxpexInfinity, Faridabad, Haryana\n"
              "September 2024 – Present\n"
              "- 🌟 Established a forward-thinking tech solutions company.\n"
              "- 🤝 Partnered with clients to deliver customized cybersecurity strategies.\n"
              "- 🚀 Drove innovation by focusing on customer-centric solutions and emerging technologies.")
pdf.chapter_body(experience)

# Skills Section
pdf.chapter_title('💡 Skills & Expertise')
skills = ("Core Competencies\n"
          "🔐 Cybersecurity Strategies | 🖥️ IT Management | ⚖️ Risk Assessment & Management\n"
          "🌐 Network Security | 🚨 Incident Response | 📅 Project Management\n\n"
          "Programming Languages\n"
          "Python 🐍 | Java ☕ | JavaScript 🌐 | Rust 🦀 (learning) | C/C++ 💻\n"
          "SQL 📊 | HTML/CSS 📑 (Web Dev) | Bash/Shell scripting 🖥️\n"
          "Go | Ruby | Julia | PHP | Kotlin\n\n"
          "Tools & Technologies\n"
          "🛠️ JetBrains Suite (IntelliJ IDEA, WebStorm, PyCharm)\n"
          "🐳 Docker | ☸️ Kubernetes | 🔍 Wireshark | 🧑‍💻 John the Ripper\n"
          "☁️ AWS & Azure | 💣 Metasploit | 🕷️ Burp Suite")
pdf.chapter_body(skills)

# Certifications Section
pdf.chapter_title('📜 Certifications')
certifications = "[List relevant certifications here]"
pdf.chapter_body(certifications)

# Projects Section
pdf.chapter_title('📂 Projects')
projects = ("Project Name\n"
            "[Short description of your project, the technologies used, and key outcomes achieved.]\n\n"
            "Project Name\n"
            "[Short description of your project, the technologies used, and key outcomes achieved.]")
pdf.chapter_body(projects)

# Professional Affiliations Section
pdf.chapter_title('🤝 Professional Affiliations')
affiliations = "Member of [Relevant Professional Organizations]"
pdf.chapter_body(affiliations)

# References Section
pdf.chapter_title('📋 References')
references = "Available upon request."
pdf.chapter_body(references)

# Save the PDF
output_path = "/mnt/data/Rohan_Naagar_Resume.pdf"
pdf.output(output_path)

output_path
