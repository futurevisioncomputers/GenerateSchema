import streamlit as st
import json
from datetime import date

st.set_page_config(page_title="🎓 SEO + AEO + GEO + AIO Schema Generator", page_icon="🎓", layout="wide")

st.title("🎓 SEO + AEO + GEO + AIO Schema Generator")
st.caption("Generate fully optimized JSON-LD schema for Courses and Blogs — including FAQs, LocalBusiness, and AI-enhanced metadata.")

# Sidebar Navigation
page = st.sidebar.radio(
    "Select Schema Type",
    ["📘 Course Schema (Full SEO + AEO + GEO + AIO)", "📝 Education Article Schema (Full SEO + AEO + GEO + AIO)"]
)

# -------------------------------------------------------------------
# 📘 COURSE SCHEMA (FULL)
# -------------------------------------------------------------------
if page == "📘 Course Schema (Full SEO + AEO + GEO + AIO)":
    st.header("🏫 Institute Information")
    inst_name = st.text_input("Institute Name", "Future Vision Computer Institute")
    inst_url = st.text_input("Website URL", "https://futurevisioncomputers.com/")
    inst_logo = st.text_input("Logo URL", "")
    inst_phone = st.text_input("Phone Number", "+91-9825771678")
    inst_email = st.text_input("Institute Email", "info@futurevisioncomputers.com")
    inst_address = st.text_area("Full Address", "G-40, Navmanglam Complex, Citylight, Surat, Gujarat 395007, India")
    inst_lat = st.text_input("Latitude", "21.1702")
    inst_long = st.text_input("Longitude", "72.8311")
    inst_area = st.text_input("Area Served", "Surat, Gujarat, India")
    inst_map = st.text_input("Google Map URL", "https://goo.gl/maps/xyz")
    inst_social = st.text_area("Social Links (comma separated)", "https://facebook.com/fvcomputers, https://instagram.com/fvcomputers")

    st.subheader("⏰ Opening Hours")
    opens = st.text_input("Opens", "08:00")
    closes = st.text_input("Closes", "20:00")
    open_days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

    st.header("🎓 Course Information")
    course_name = st.text_input("Course Name", "MS Office Professional Training")
    course_code = st.text_input("Course Code / Identifier", "MSO-101")
    course_desc = st.text_area("Course Description", "A complete Microsoft Office course from beginner to expert level.")
    course_url = st.text_input("Course URL", "https://yourwebsite.com/courses/ms-office")
    course_fee = st.text_input("Course Fee", "₹5000")
    course_currency = st.text_input("Currency", "INR")
    course_duration = st.text_input("Duration (e.g., 3 Months / P3M)", "3 Months")
    course_mode = st.multiselect("Course Mode", ["Online", "Offline"], default=["Offline"])
    course_level = st.selectbox("Educational Level", ["Beginner", "Intermediate", "Advanced"])
    course_prereq = st.text_input("Prerequisites", "Basic computer knowledge")
    course_lang = st.text_input("Language (ISO code)", "en-IN")
    cert_award = st.text_input("Certification Awarded", "Certificate of Completion")

    st.header("📚 Learning Details")
    topics = st.text_area("Topics Covered", "MS Word, Excel, PowerPoint, Outlook")
    methods = st.text_area("Learning Methods", "Hands-on Practice, Assignments, Projects")
    outcomes = st.text_area("Learning Outcomes", "Create Excel dashboards, Design PowerPoint templates")

    st.header("🖼️ Course Images & Video")
    image_urls = st.text_area("Image URLs (comma separated)", "https://yourwebsite.com/images/ms-office.webp")
    video_url = st.text_input("Video URL (optional)", "")
    video_embed = st.text_input("Video Embed URL", "")

    st.header("👨‍🏫 Instructor & Author")
    instructor_name = st.text_input("Instructor Name", "Siddharth Parakh")
    instructor_desc = st.text_area("Instructor Bio", "Certified trainer with 20+ years of experience.")
    author_sameas = st.text_area("Author Social / Profile URLs (comma separated)", "https://linkedin.com/in/siddharthparakh")
    author_knows = st.text_area("Author Expertise (comma separated)", "Excel, Power BI, Computer Skills")

    st.header("🔗 SEO & Trust Signals")
    rating_value = st.text_input("Average Rating", "4.8")
    review_count = st.text_input("Review Count", "152")
    license_url = st.text_input("License / Terms URL", "https://yourwebsite.com/license")
    citations = st.text_area("Citations / References (comma separated)", "https://learn.microsoft.com/en-us/office/")
    keywords = st.text_input("Keywords", "MS Office, Excel, Computer Course, Job Oriented")
    about_tags = st.text_input("About Topics", "Microsoft Office, IT Training, Office Productivity")

    st.header("💬 FAQ Section")
    faqs = []
    n_faqs = st.number_input("Number of FAQs", 1, 10, 3)
    for i in range(n_faqs):
        q = st.text_input(f"Question {i+1}", "")
        a = st.text_area(f"Answer {i+1}", "")
        if q and a:
            faqs.append({
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a}
            })

    if st.button("✅ Generate Full Course Schema"):
        org_schema = {
            "@context": "https://schema.org",
            "@type": ["EducationalOrganization", "LocalBusiness"],
            "name": inst_name,
            "url": inst_url,
            "logo": inst_logo,
            "telephone": inst_phone,
            "email": inst_email,
            "address": inst_address,
            "areaServed": inst_area,
            "geo": {"@type": "GeoCoordinates", "latitude": inst_lat, "longitude": inst_long},
            "hasMap": inst_map,
            "openingHoursSpecification": [{
                "@type": "OpeningHoursSpecification",
                "dayOfWeek": open_days,
                "opens": opens,
                "closes": closes
            }],
            "sameAs": [s.strip() for s in inst_social.split(",")]
        }

        course_schema = {
            "@context": "https://schema.org",
            "@type": "Course",
            "identifier": {"@type": "PropertyValue", "propertyID": "CourseCode", "value": course_code},
            "name": course_name,
            "description": course_desc,
            "url": course_url,
            "image": [i.strip() for i in image_urls.split(",")],
            "video": {"@type": "VideoObject", "url": video_url, "embedUrl": video_embed} if video_url else None,
            "provider": {"@type": "EducationalOrganization", "name": inst_name, "url": inst_url},
            "educationalLevel": course_level,
            "coursePrerequisites": course_prereq,
            "educationalCredentialAwarded": cert_award,
            "inLanguage": course_lang,
            "timeRequired": course_duration,
            "teaches": [t.strip() for t in topics.split(",")],
            "learningResourceType": [m.strip() for m in methods.split(",")],
            "learningOutcome": [o.strip() for o in outcomes.split(",")],
            "aggregateRating": {"@type": "AggregateRating", "ratingValue": rating_value, "reviewCount": review_count},
            "author": {
                "@type": "Person",
                "name": instructor_name,
                "description": instructor_desc,
                "sameAs": [s.strip() for s in author_sameas.split(",")],
                "knowsAbout": [k.strip() for k in author_knows.split(",")],
                "worksFor": {"@type": "Organization", "name": inst_name}
            },
            "educationalAlignment": {
                "@type": "AlignmentObject",
                "alignmentType": "educationalLevel",
                "targetName": course_level
            },
            "potentialAction": {
                "@type": "EnrollAction",
                "target": f"{course_url}/enroll",
                "name": f"Enroll in {course_name}"
            },
            "license": license_url,
            "citation": [c.strip() for c in citations.split(",")],
            "keywords": [k.strip() for k in keywords.split(",")],
            "about": [a.strip() for a in about_tags.split(",")],
            "interactionStatistic": {
                "@type": "InteractionCounter",
                "interactionType": "https://schema.org/LikeAction",
                "userInteractionCount": "300"
            }
        }

        faq_schema = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": faqs}
        schema = [org_schema, course_schema, faq_schema]
        st.success("✅ Full SEO + AEO + GEO + AIO Course Schema Generated!")
        st.code(json.dumps(schema, indent=2), language="json")
        st.download_button("💾 Download JSON-LD", json.dumps(schema, indent=2), file_name="course_full_schema.json")

# -------------------------------------------------------------------
# 📝 BLOG SCHEMA (FULL)
# -------------------------------------------------------------------
elif page == "📝 Education Article Schema (Full SEO + AEO + GEO + AIO)":
    st.header("📰 Blog Details")
    headline = st.text_input("Headline", "Master Excel Formulas for Business Analytics")
    description = st.text_area("Description", "Learn essential Excel formulas every analyst should know.")
    blog_url = st.text_input("Blog URL", "https://yourdomain.com/blog/excel-formulas")
    image_url = st.text_input("Main Image URL (1200px)", "")
    date_published = st.date_input("Date Published", date.today())
    date_modified = st.date_input("Date Modified", date.today())
    author_name = st.text_input("Author Name", "Siddharth")
    author_sameas = st.text_area("Author Social Links", "https://linkedin.com/in/siddharthparakh")
    author_knows = st.text_area("Author Expertise", "Excel, Analytics, Data Visualization")
    pub_name = st.text_input("Publisher Name", "Future Vision Computer Institute")
    pub_logo = st.text_input("Publisher Logo", "")
    pub_social = st.text_area("Publisher Social Links", "https://facebook.com/fvcomputers, https://linkedin.com/company/fvcomputers")
    keywords = st.text_input("Keywords", "Excel, Education, Data Analytics")
    about_tags = st.text_input("About Topics", "Microsoft Excel, Business Analytics")
    word_count = st.number_input("Word Count", 300, 5000, 1200)
    license_url = st.text_input("License URL", "https://yourdomain.com/license")
    citations = st.text_area("Citations", "https://learn.microsoft.com/en-us/office/")
    free_access = st.checkbox("Is Accessible for Free?", True)

    st.header("🎥 Optional Video")
    video_url = st.text_input("Video URL", "")
    video_embed = st.text_input("Embed URL", "")
    video_duration = st.text_input("Video Duration (ISO e.g., PT5M30S)", "PT5M")

    st.header("💬 FAQ Section")
    faqs = []
    n_faq = st.number_input("Number of FAQs", 1, 10, 2)
    for i in range(n_faq):
        q = st.text_input(f"Question {i+1}", "")
        a = st.text_area(f"Answer {i+1}", "")
        if q and a:
            faqs.append({
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a}
            })

    if st.button("🚀 Generate Full Blog Schema"):
        blog_schema = {
            "@context": "https://schema.org",
            "@type": "BlogPosting",
            "headline": headline,
            "description": description,
            "url": blog_url,
            "image": image_url,
            "datePublished": str(date_published),
            "dateModified": str(date_modified),
            "isAccessibleForFree": free_access,
            "author": {
                "@type": "Person",
                "name": author_name,
                "sameAs": [s.strip() for s in author_sameas.split(",")],
                "knowsAbout": [k.strip() for k in author_knows.split(",")]
            },
            "publisher": {
                "@type": "Organization",
                "name": pub_name,
                "logo": {"@type": "ImageObject", "url": pub_logo},
                "sameAs": [s.strip() for s in pub_social.split(",")]
            },
            "keywords": [k.strip() for k in keywords.split(",")],
            "about": [a.strip() for a in about_tags.split(",")],
            "wordCount": word_count,
            "articleBody": description,
            "license": license_url,
            "citation": [c.strip() for c in citations.split(",")],
            "educationalAlignment": {
                "@type": "AlignmentObject",
                "alignmentType": "educationalLevel",
                "targetName": "Intermediate"
            },
            "speakable": {"@type": "SpeakableSpecification", "xpath": ["/html/head/title", "/html/body/h1"]},
            "audience": {"@type": "Audience", "audienceType": "Students and Professionals"},
            "isPartOf": {"@type": "Blog", "name": "Education Blog"},
            "potentialAction": {
                "@type": "ReadAction",
                "target": blog_url,
                "name": f"Read {headline}"
            }
        }

        if video_url:
            blog_schema["video"] = {
                "@type": "VideoObject",
                "url": video_url,
                "embedUrl": video_embed,
                "duration": video_duration
            }

        faq_schema = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": faqs}
        schema = [blog_schema, faq_schema]
        st.success("✅ Full SEO + AEO + GEO + AIO Blog Schema Generated!")
        st.code(json.dumps(schema, indent=2), language="json")
        st.download_button("💾 Download JSON-LD", json.dumps(schema, indent=2), file_name="blog_full_schema.json")
