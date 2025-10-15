import streamlit as st
import json
from datetime import date

st.set_page_config(page_title="Course Schema Generator", page_icon="📘", layout="centered")

st.title("📘 JSON-LD Schema Generator for Courses")
st.write("Easily create Google & AI-friendly JSON-LD schema for your institute’s courses.")

# ---- Institute Info ----
st.header("🏫 Institute Information")
inst_name = st.text_input("Institute Name", "Future Computer Institute")
inst_url = st.text_input("Website URL", "https://futurevisioncomputers.com/")
inst_logo = st.text_input("Logo URL", "https://futurevisioncomputers.com/wp-content/uploads/2024/07/fv-logo-final-current.png")
inst_phone = st.text_input("Phone Number", "+91-9825771678")
inst_street = st.text_input("Street Address", "g-40, Navmanglam Complex, Citylight")
inst_city = st.text_input("City", "Surat")
inst_state = st.text_input("State", "Gujarat")
inst_pin = st.text_input("Postal Code", "395007")
inst_country = st.text_input("Country Code", "IN")
inst_social = st.text_area("Social Links (comma-separated)", 
                           "https://facebook.com/siddharthcomputers, https://instagram.com/siddharthcomputers")

# ---- Course Info ----
st.header("🎓 Course Information")
course_name = st.text_input("Course Name", "MS Office Professional Training")
course_code = st.text_input("Course Code", "MSO-101")
course_desc = st.text_area("Course Description", 
    "A complete Microsoft Office course covering Word, Excel, PowerPoint, and Outlook from beginner to advanced level.")
course_mode = st.multiselect("Course Mode", ["Online", "Offline"], default=["Offline"])
course_start = st.date_input("Start Date", date.today())
course_end = st.date_input("End Date")
course_duration = st.text_input("Duration (ISO Format)", "P2M")
course_fee = st.number_input("Course Fee (₹)", 0, 100000, 4500)
course_currency = st.text_input("Currency", "INR")
cert_award = st.text_input("Certification Awarded", "Certificate of Completion")

# ---- Curriculum ----
st.header("📚 Curriculum Details")
topics = st.text_area("Topics Covered (comma-separated)", 
                      "MS Word, MS Excel (Formulas, Charts, Functions, Data Analysis), MS PowerPoint, MS Outlook")
learning_methods = st.text_area("Learning Methods (comma-separated)", 
                                "Hands-on Practice, Assignments, Live Demos, Project Work")

# ---- Instructor ----
st.header("👨‍🏫 Instructor Details")
inst_name_instructor = st.text_input("Instructor Name", "Siddharth Patel")
inst_exp = st.text_area("Instructor Description", "Certified computer trainer with 10+ years of experience.")

# ---- Audience ----
st.header("🎯 Target Audience")
audience_type = st.text_input("Audience Type", "Students, Job Seekers, Working Professionals")

# ---- Generate JSON-LD ----
if st.button("🚀 Generate JSON-LD Schema"):
    schema = {
        "@context": "https://schema.org",
        "@type": "Course",
        "name": course_name,
        "alternateName": course_name,
        "courseCode": course_code,
        "description": course_desc,
        "provider": {
            "@type": "EducationalOrganization",
            "name": inst_name,
            "url": inst_url,
            "logo": inst_logo,
            "address": {
                "@type": "PostalAddress",
                "streetAddress": inst_street,
                "addressLocality": inst_city,
                "addressRegion": inst_state,
                "postalCode": inst_pin,
                "addressCountry": inst_country
            },
            "telephone": inst_phone,
            "sameAs": [link.strip() for link in inst_social.split(",")]
        },
        "hasCourseInstance": {
            "@type": "CourseInstance",
            "courseMode": course_mode,
            "startDate": str(course_start),
            "endDate": str(course_end),
            "duration": course_duration,
            "instructor": {
                "@type": "Person",
                "name": inst_name_instructor,
                "description": inst_exp
            },
            "location": {
                "@type": "Place",
                "name": f"{inst_name} - {inst_city}",
                "address": {
                    "@type": "PostalAddress",
                    "streetAddress": inst_street,
                    "addressLocality": inst_city,
                    "addressRegion": inst_state,
                    "postalCode": inst_pin,
                    "addressCountry": inst_country
                }
            },
            "offers": {
                "@type": "Offer",
                "price": str(course_fee),
                "priceCurrency": course_currency,
                "availability": "https://schema.org/InStock",
                "url": f"{inst_url}/courses/{course_name.replace(' ', '-').lower()}",
                "validFrom": str(date.today())
            }
        },
        "educationalCredentialAwarded": cert_award,
        "timeRequired": course_duration,
        "teaches": [topic.strip() for topic in topics.split(",")],
        "learningResourceType": [m.strip() for m in learning_methods.split(",")],
        "about": ["Computer Skills", "Office Productivity", "IT Training"],
        "audience": {
            "@type": "Audience",
            "audienceType": audience_type
        }
    }

    json_ld = json.dumps(schema, indent=2)
    st.subheader("✅ Generated JSON-LD Schema")
    st.code(f"<script type='application/ld+json'>\n{json_ld}\n</script>", language="html")

    st.download_button("💾 Download Schema as JSON", json_ld, file_name="course_schema.json")

st.info("💡 Tip: Copy and paste the JSON-LD script into the <head> or bottom of your course webpage.")

