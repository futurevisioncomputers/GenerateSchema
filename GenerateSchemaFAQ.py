import streamlit as st
import json

st.set_page_config(page_title="Course Schema Generator", layout="centered")

st.title("🎓 Course Schema Generator (JSON-LD)")
st.caption("Generate SEO + AI optimized schema markup for your courses with multiple branches and FAQs.")

# --- Course Information ---
st.header("🧾 Course Details")

course_name = st.text_input("Course Name", "MS Office Training")
course_desc = st.text_area(
    "Course Description",
    "Learn Microsoft Office (Word, Excel, PowerPoint) from beginner to advanced level with certification."
)
course_url = st.text_input("Course URL", "https://yourwebsite.com/ms-office")
course_duration = st.text_input("Course Duration", "3 Months")
course_fee = st.text_input("Course Fee", "₹5000")
course_mode = st.selectbox("Course Mode", ["Offline", "Online", "Both"])

# --- Provider Information ---
st.header("🏫 Institute Details")

provider_name = st.text_input("Institute Name", "Siddharth Computer Institute")
provider_url = st.text_input("Institute Website", "https://yourwebsite.com")
provider_logo = st.text_input("Institute Logo URL", "https://yourwebsite.com/logo.png")

# --- Branch Details (Fixed: 3 Branches) ---
st.header("📍 Branch Locations (3 Branches)")

branches = []
for i in range(3):
    st.subheader(f"🏢 Branch {i+1}")
    street = st.text_input(f"Street Address (Branch {i+1})", key=f"street_{i}")
    city = st.text_input(f"City (Branch {i+1})", key=f"city_{i}")
    region = st.text_input(f"State/Region (Branch {i+1})", key=f"region_{i}")
    postal = st.text_input(f"Postal Code (Branch {i+1})", key=f"postal_{i}")
    country = st.text_input(f"Country (Branch {i+1})", "IN", key=f"country_{i}")
    telephone = st.text_input(f"Phone (Branch {i+1})", key=f"phone_{i}")

    if street and city:
        branches.append({
            "@type": "Place",
            "name": f"{provider_name} - {city}",
            "address": {
                "@type": "PostalAddress",
                "streetAddress": street,
                "addressLocality": city,
                "addressRegion": region,
                "postalCode": postal,
                "addressCountry": country
            },
            "telephone": telephone
        })

# --- FAQ Section ---
st.header("💬 Course FAQs")

faq_list = []
num_faqs = st.number_input("Number of FAQs", min_value=1, max_value=10, value=3)

for i in range(int(num_faqs)):
    st.subheader(f"❓ FAQ {i+1}")
    question = st.text_input(f"Question {i+1}", key=f"q_{i}")
    answer = st.text_area(f"Answer {i+1}", key=f"a_{i}")
    if question and answer:
        faq_list.append({
            "@type": "Question",
            "name": question,
            "acceptedAnswer": {
                "@type": "Answer",
                "text": answer
            }
        })

# --- Generate JSON-LD ---
if st.button("✅ Generate Course Schema"):
    course_schema = {
        "@context": "https://schema.org",
        "@type": "Course",
        "name": course_name,
        "description": course_desc,
        "provider": {
            "@type": "Organization",
            "name": provider_name,
            "url": provider_url,
            "logo": provider_logo
        },
        "hasCourseInstance": {
            "@type": "CourseInstance",
            "courseMode": course_mode,
            "courseWorkload": course_duration,
            "offers": {
                "@type": "Offer",
                "price": course_fee,
                "priceCurrency": "INR",
                "availability": "https://schema.org/InStock",
                "url": course_url
            },
            "location": branches
        }
    }

    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": faq_list
    }

    full_schema = [course_schema, faq_schema]

    st.success("✅ JSON-LD Schema Generated Successfully!")
    st.code(json.dumps(full_schema, indent=2), language="json")

    # Download button
    st.download_button(
        label="⬇️ Download JSON-LD File",
        data=json.dumps(full_schema, indent=2),
        file_name=f"{course_name.lower().replace(' ', '_')}_schema.json",
        mime="application/json"
    )
