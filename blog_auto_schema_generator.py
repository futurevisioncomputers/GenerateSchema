import streamlit as st
import json
from datetime import datetime
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup
import re
from collections import Counter

st.set_page_config(page_title="Smart Auto Blog Schema Generator v5 — Future Vision", layout="centered")
st.title("🧠 Smart Auto Blog Schema Generator v5 — Future Vision Computers")
st.markdown("Enter your blog URL and category. The app auto-generates a full SEO + AEO JSON-LD schema (BlogPosting + FAQ + Organization) — dynamically adapting `keywords`, `about`, and `FAQ` based on your category, title, and description.")

# --- Inputs ---
blog_url = st.text_input("Enter Blog URL", "https://futurevisioncomputers.com/fourth-word-in-excel-advanced-excel-for-finance-business-analytics/")
category = st.text_input("Enter Blog Category (e.g. Advanced Excel, Python, Data Analytics, Power BI, Finance)", "Advanced Excel")

if st.button("Generate Full Schema"):
    if not blog_url.strip():
        st.error("Please enter a valid blog URL.")
        st.stop()

    try:
        response = requests.get(blog_url, timeout=10, headers={'User-Agent':'Mozilla/5.0'})
        soup = BeautifulSoup(response.text, "html.parser")
    except Exception as e:
        st.error(f"Error fetching blog data: {e}")
        st.stop()

    # --- Extract metadata ---
    def meta(prop, attr="property"):
        tag = soup.find("meta", attrs={attr: prop})
        return tag["content"].strip() if tag and tag.has_attr("content") else None

    extracted = {
        "title": meta("og:title") or (soup.title.string.strip() if soup.title else None),
        "description": meta("og:description") or meta("description", "name"),
        "image": meta("og:image"),
        "author": meta("author", "name"),
        "published": meta("article:published_time"),
        "modified": meta("article:modified_time"),
        "keywords": meta("keywords", "name")
    }

    # --- Defaults ---
    defaults = {
        "title": "Untitled Blog Post",
        "description": "Educational blog post from Future Vision Computers.",
        "image": "https://futurevisioncomputers.com/wp-content/uploads/2025/10/default.jpg",
        "author": "Siddharth Parakh",
        "published": datetime.now().isoformat(),
        "modified": datetime.now().isoformat(),
        "keywords": category + ", Education, Training"
    }

    checklist = {}
    for key in defaults:
        if extracted.get(key):
            checklist[key] = f"✅ {key.title()} — Extracted from site"
        else:
            extracted[key] = defaults[key]
            checklist[key] = f"⚠️ {key.title()} — Default used (not found on page)"

    # --- Analyze Content ---
    content_text = soup.get_text(separator=" ").lower()
    words = re.findall(r"[a-zA-Z]{4,}", content_text)
    word_freq = Counter(words)
    common_terms = [w for w, c in word_freq.most_common(25)]

    # --- Enriched Keywords ---
    base_keywords = [k.strip().title() for k in (extracted["keywords"].split(",") if extracted["keywords"] else [])]
    derived_keywords = list(set(base_keywords + [category.title()] + [w.title() for w in common_terms[:10]]))
    checklist["keywords"] = f"✅ Keywords — Auto-updated from content + category"

    # --- Dynamic About Section ---
    about_items = [{"@type": "Thing", "name": category.title()}]
    for kw in derived_keywords[:6]:
        if kw.lower() not in [a["name"].lower() for a in about_items]:
            about_items.append({"@type": "Thing", "name": kw})
    checklist["about"] = f"✅ About — {', '.join([a['name'] for a in about_items])}"

    # --- Audience Detection ---
    audience_terms = ["students", "professionals", "analysts", "learners", "developers"]
    detected_audience = [a.title() for a in audience_terms if a in content_text]
    if not detected_audience:
        detected_audience = ["Students", "Professionals"]
    checklist["audience"] = f"✅ Audience — {', '.join(detected_audience)}"

    # --- Smart FAQ Generation ---
    faq_items = []
    faq_tags = soup.find_all(["h2", "h3", "strong", "details", "summary", "p"])
    for tag in faq_tags:
        text = tag.get_text().strip()
        if "?" in text or text.lower().startswith(("q:", "question")):
            next_tag = tag.find_next(["p", "div"])
            answer = next_tag.get_text().strip() if next_tag else "Answer not found."
            faq_items.append({"@type": "Question", "name": text, "acceptedAnswer": {"@type": "Answer", "text": answer}})

    if not faq_items:
        faq_items = [
            {"@type": "Question", "name": f"What is {category}?", "acceptedAnswer": {"@type": "Answer", "text": f"This blog explains {category} concepts with practical examples."}},
            {"@type": "Question", "name": f"Who should learn {category}?", "acceptedAnswer": {"@type": "Answer", "text": f"{category} is ideal for students and professionals in analytics, business, or technology."}},
            {"@type": "Question", "name": f"How does this blog help in {category}?", "acceptedAnswer": {"@type": "Answer", "text": f"This blog provides step-by-step {category} tutorials and use cases for real-world applications."}}
        ]
        checklist["faq"] = "✅ FAQ — Auto-created based on category and title"
    else:
        checklist["faq"] = f"✅ FAQ — {len(faq_items)} detected from page"

    # --- Build Schema ---
    parsed = urlparse(blog_url)
    base_url = f"{parsed.scheme}://{parsed.netloc}"

    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "BlogPosting",
                "@id": blog_url,
                "headline": extracted["title"],
                "description": extracted["description"],
                "image": {"@type": "ImageObject", "url": extracted["image"], "width": 1200, "height": 630},
                "author": {"@type": "Person", "name": extracted["author"], "url": base_url},
                "publisher": {
                    "@type": "Organization",
                    "@id": "#FutureVision",
                    "name": "Future Vision Computer Institute",
                    "url": "https://futurevisioncomputers.com/",
                    "logo": {"@type": "ImageObject", "url": "https://futurevisioncomputers.com/wp-content/uploads/2024/07/fv-logo-final-current.png", "width": 600, "height": 60}
                },
                "datePublished": extracted["published"],
                "dateModified": extracted["modified"],
                "isAccessibleForFree": True,
                "inLanguage": "en-IN",
                "isFamilyFriendly": True,
                "genre": category + " Blog",
                "keywords": derived_keywords,
                "audience": {"@type": "EducationalAudience", "educationalRole": "learner", "audienceType": ", ".join(detected_audience)},
                "about": about_items,
                "potentialAction": {"@type": "ReadAction", "target": blog_url},
                "mainEntityOfPage": {"@type": "WebPage", "@id": blog_url}
            },
            {
                "@type": "FAQPage",
                "@id": blog_url + "#faq",
                "mainEntity": faq_items
            },
            {
                "@type": "Organization",
                "@id": "#FutureVision",
                "name": "Future Vision Computer Institute",
                "url": "https://futurevisioncomputers.com/",
                "logo": "https://futurevisioncomputers.com/wp-content/uploads/2024/07/fv-logo-final-current.png",
                "image": "https://futurevisioncomputers.com/wp-content/uploads/2025/10/future-vision-campus.jpg",
                "description": "Future Vision Computers in Surat publishes educational blogs and tutorials on Advanced Excel, Power BI, Python, and Data Science.",
                "sameAs": [
                    "https://facebook.com/fvcomputers",
                    "https://linkedin.com/company/fvcomputers",
                    "https://instagram.com/fvcomputers"
                ],
                "address": {"@type": "PostalAddress", "streetAddress": "Citylight, Vesu, Pal Area", "addressLocality": "Surat", "addressRegion": "Gujarat", "postalCode": "395007", "addressCountry": "IN"},
                "telephone": "+91-9825771678",
                "location": {"@type": "Place", "geo": {"@type": "GeoCoordinates", "latitude": "21.1702", "longitude": "72.8311"}}
            }
        ]
    }

    # --- Output ---
    st.subheader("✅ Generated JSON-LD Schema")
    json_text = json.dumps(schema, indent=2, ensure_ascii=False)
    st.code(json_text, language="json")
    st.download_button("📥 Download JSON-LD File", json_text, file_name="blog_schema.json", mime="application/json")

    st.subheader("🧾 Field Update Checklist")
    for k, v in checklist.items():
        if "✅" in v:
            st.success(v)
        else:
            st.warning(v)
